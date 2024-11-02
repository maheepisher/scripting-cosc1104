"""
File Name: ec2_instances.py

Author: Maheep Isher Singh Chawla (100909435), Poorva Sharma (100934359)

Date: 1 Nov'2024

Description: This file takes input from user for min and max CPUs and Memory. It then compares elegible instances as per user's requirements with 
             the available instances in the json file and returns the relevant output.


"""


import json
import re

# Function to get valid integer input from user
def get_valid_integer(prompt, allow_none=False):
    while True:
        user_input = input(prompt)
        if allow_none and not user_input:
            return None
        try:
            return int(user_input)
        except ValueError:
            print("Please enter a valid integer.")

# Function to parse the vCPU count from the JSON data
def parse_vcpu_count(vcpu_str):
    match = re.search(r'(\d+)', vcpu_str)
    return int(match.group(1)) if match else 0

# Function to parse memory in GiB from the JSON data
def parse_memory_gib(memory_str):
    match = re.search(r'(\d+\.?\d*)', memory_str)
    return float(match.group(1)) if match else 0.0

# Function to filter EC2 instances based on CPU and memory requirements
def filter_ec2_instances(instances, min_cpu, max_cpu, min_memory, max_memory):
    filtered_instances = []
    for instance in instances:
        vcpu_count = parse_vcpu_count(instance["vcpu"])
        memory_gib = parse_memory_gib(instance["memory"])
        
        if (min_cpu is None or vcpu_count >= min_cpu) and \
           (max_cpu is None or vcpu_count <= max_cpu) and \
           (min_memory is None or memory_gib >= min_memory) and \
           (max_memory is None or memory_gib <= max_memory):
            filtered_instances.append(instance)
    
    return filtered_instances

    

if __name__ == "__main__":
    
    
    # Get the user's CPU and memory requirements
    min_cpu = get_valid_integer("Enter the minimum required CPU cores: ")
    max_cpu = get_valid_integer("Enter the maximum allowed CPU cores (optional): ", allow_none=True)
    min_memory = get_valid_integer("Enter the minimum required memory in GiB: ")
    max_memory = get_valid_integer("Enter the maximum allowed memory in GiB (optional): ", allow_none=True)

    # Load the JSON data
    with open('E:\Cloud Computing\Scripting\Repositories\scripting-cosc1104\in-class-4\ec2_instance_types.json', 'r') as jsonfile:
        ec2_instances = json.load(jsonfile)

    # Filter the instances based on user input
    matching_instances = filter_ec2_instances(ec2_instances, min_cpu, max_cpu, min_memory, max_memory)

    # Display the results
    if matching_instances:
        print("\nMatching EC2 Instance Types:")
        for instance in matching_instances:
            print(f"Name: {instance['name']}, CPU: {instance['vcpu']}, Memory: {instance['memory']}")
    else:
        print("No instances match your criteria.")
