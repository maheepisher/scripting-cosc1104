"""
File Name: storage_tracking.py

Author: Maheep Isher Singh Chawla (100909435)

Date: 11 oct'2024

Description: This file contains code which takes user input users and required storage. various functions are performed like:
             Create an Account, Delete Account, Upload File, Show Accounts


"""


track = {}


def CreateAccount(username, req_storage):
    message = ""
    
    if username in track:
        message = "This user already exists."
    elif username.strip() == "":
        message = "Username cannot be blank."
    elif req_storage <= 0:
         message = "Storage should be greater than 0."
    else:
        track[username] = req_storage
        message = (f"New user added: {username} with {req_storage} GB of storage.")
    
    return message

def DeleteAccount(username):
    message = ""
    
    if username in track:
        del track[username]
        message = (f"Account with username {username} deleted.")
    else:
        message = (f"There is no account with username {username}.")
    
    return message


def UploadFile(username, filename, filesize):
    message = ""
    if username in track:
        if filename.strip() == "":
            message = "File name cannot be blank."
        elif filesize <= 0:
            message = "File size cannot be less than or equal to 0."
        elif track[username] < filesize:
            message = "Not enough storage space to upload this file."             
        else:
            message = (f"File: {filename} added for {username}.")
            track[username] = track[username] - filesize
    else:
        message = (f"There is no account with username {username}.")
    
    return message
    
def ShowAccounts():
    for key, value in track.items():
        print(f"User name: {key}, Available Storage: {value}\n")
    

if __name__ == "__main__":
    while True:
        option = int(input("1 - Create a new account.\n2 - Delete an account.\n3 - Upload file.\n4  - List accounts.\n5 - Exit.\nSelect an option (1-5):"))
        if option == 1:
            print("----Adding New User----")
            username = input("Enter username: ")
            req_storage = int(input("Enter storage required: "))
            message = CreateAccount(username, req_storage)
            print(message)
        elif option == 2:
            print("----Deleting Account----")
            username = input("Enter the username of the account that you want to delete: ")
            message = DeleteAccount(username)
            print(message)
        elif option == 3:
            print("----Uploading File----")
            username = input("Enter the username of the account to add a file: ")
            filename = input("Enter File Name: ")
            filesize = int(input("Enter file's size: "))
            message = UploadFile(username, filename, filesize)
            print(message)
        elif option == 4:
            print("----Account List----")
            ShowAccounts()
        elif option == 5:
            print("You chose to exit the menu.")
            break
        else:
            print("Invalid Option Selected.")