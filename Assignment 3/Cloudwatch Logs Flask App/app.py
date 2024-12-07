'''
File Name:   app.py
Author:      Maheep isher Singh Chawla - 100909435
Date:        6 Dec'2024
Description: This file is the entrypoint for flask application which incorporates login, logs methods 
             
'''


from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from flask_session import Session
import json
import os

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Data for log events using log groups and log streams
LOG_EVENTS = []

def get_cloudwatch_client(access_key, secret_key, region):
    """
    Creates a CloudWatch Logs client using provided credentials.
    Returns the client or an error message.
    """
    try:
        client = boto3.client(
            "logs",
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region,
        )
        
        # Test connection by calling describe_log_groups
        client.describe_log_groups(limit=1)
        return client, None
    except (BotoCoreError, ClientError) as e:
        return None, str(e)
    
def get_client_from_session():
    client = boto3.client(
            "logs",
            aws_access_key_id=session["access_key"],
            aws_secret_access_key=session["secret_key"],
            region_name=session["region"],
        )
    return client

def get_log_events(log_group_name, log_stream_name):
    client = get_client_from_session()
    
    response = client.get_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        limit=10,
        startFromHead=True
    )

    LOG_EVENTS.clear()
    
    for event in response['events']:
        map = {"Timestamp" : event["timestamp"], "Message" : event["message"]}
        LOG_EVENTS.append(map)
        #print(f'Timestamp: {event["timestamp"]}, Message: {event["message"]}')

def get_log_group_details():
    client = get_client_from_session()
    
    response1 = client.describe_log_groups()
    log_groups = response1['logGroups']

    logGroupDetails = {}
    logGroups = []
    
    for group in log_groups:
        logGroups.append(group['logGroupName'])
        response2 = client.describe_log_streams(logGroupName=group['logGroupName'])
        log_streams = response2['logStreams']

        logStreams = []
        
        for stream in log_streams:
            logStreams.append(stream['logStreamName'])
        
        logGroupDetails[group['logGroupName']] = logStreams
        
    return logGroups, logGroupDetails
        

@app.route("/", methods=["GET", "POST"])
def login():
    
    #Login page to enter AWS credentials.
    
    if request.method == "POST":
        
        try:
            access_key = request.form.get("access_key")
            secret_key = request.form.get("secret_key")
            awsregion = request.form.get("region")

            client, error_message = get_cloudwatch_client(access_key, secret_key, awsregion)
            if client:
                session["access_key"] = access_key
                session["secret_key"] = secret_key
                session["region"] = awsregion
                
                return redirect(url_for("dashboard"))
            else:
                return render_template("login.html", error=error_message)
        
        except Exception as e:
            # Log the exception (if logging is set up) and redirect to the error page
            error_message = str(e)
            return render_template("error.html", error_message=error_message)


    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    
    #Dashboard with Home, Logs & Logout tab.
    
    return render_template("dashboard.html")


@app.route("/logs",  methods=["GET", "POST"])
def logs():
    
    try:
        if request.method == "POST":
            
            #Get Selected log group and log stream from form
            selected_log_group = request.form.get("logGroup")
            selected_log_stream = request.form.get("logStream")
                
            if not selected_log_group or not selected_log_stream:
                flash("Invalid selection. Please choose a valid log group and stream.", "danger")
                return redirect(url_for("logs"))

            # Fetch log events and save to a file
            get_log_events(selected_log_group, selected_log_stream)

            filename = f"{selected_log_group}_{selected_log_stream}.json"
            filepath = os.path.join("files", filename)  

            os.makedirs("files", exist_ok=True)  # Create directory if it doesn't exist

            with open(filepath, "w") as file:
                json.dump(LOG_EVENTS, file)

            # Provide feedback to the user
            flash(f"File downloaded successfully at: {filepath}", "success")
            return redirect(url_for("logs"))
            
        else:
            
            logGrpList, logGrpDetailsMap = get_log_group_details()
            if not logGrpList:
                logGrpList = None  # Mark log_groups as None if empty for template logic
            return render_template("logs.html", log_groups=logGrpList, log_group_details=logGrpDetailsMap)

    except Exception as e:
        # Catch any unexpected errors and redirect to the error page
        error_message = f"An error occurred while processing your request: {str(e)}"
        return render_template("error.html", error_message=error_message)

@app.route("/error", methods=["GET"])
def error():
    return render_template("error.html", error_message="An unexpected error occurred.")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
