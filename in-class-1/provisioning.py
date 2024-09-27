"""
File Name: provisioning.py

Author: Maheep Isher Singh Chawla (100909435), Poorva Sharma (100934359)

Date: 27 September'2024

Description: This file contains code which takes user input for required no. of CPU cores and memory
             and checks if the resources are available based on total available limits. 
             If resources are available, they are provisioned and remaining resources are displayed.


"""

# Defining Constants
CORES_AVAILABLE = 64                            # Number of CPU cores available
MEMORY_AVAILABLE_GB = 1000.0                    # Total amount of memory available in GB

# User's Input and validation
while True:
    try: 
        cpu_cores_required = int(input("Enter the required no. of CPU cores: "))
        break    
    except ValueError:
        print('Please enter a valid integer input.')
        continue

while True:
    try: 
        memory_gb_required= float(input("Enter the required memory in GB: "))
        break    
    except ValueError:
        print('Please enter a valid float input.')
        continue

# Check if resources are available 
if cpu_cores_required <= CORES_AVAILABLE and memory_gb_required <= MEMORY_AVAILABLE_GB:
    print("Resources provisioned successfully.")
    remaining_cpu_cores = CORES_AVAILABLE - cpu_cores_required
    remaining_memory_gb = MEMORY_AVAILABLE_GB - memory_gb_required
else:
    print("Resource request exceeds capacity. Provisioning failed.")
    remaining_cpu_cores = CORES_AVAILABLE
    remaining_memory_gb = MEMORY_AVAILABLE_GB

# Resources remaining after allocation
print(f"CPU Cores remaining: {remaining_cpu_cores}")
print(f"Memory remaining: {remaining_memory_gb} GB")