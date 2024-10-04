"""
File Name: provisioning_loops.py

Author: Maheep Isher Singh Chawla (100909435), Poorva Sharma (100934359)

Date: 27 September'2024

Description: This file contains code which takes user input for required no. of CPU cores and memory
             for multiple users and checks if the resources are available based on total available limits 
             for each user. If resources are available, they are provisioned otherwise users and their requests
             are displayed in a pending request queue. Also, remaining resources are displayed with each request.


"""

# Defining Constants
CORES_AVAILABLE = 64                            # Number of CPU cores available
MEMORY_AVAILABLE_GB = 1000.0                    # Total amount of memory available in GB

# Declare lists for allocated resources, pending requests
allocated_resources = []
requests_pending = []

# Resoureces used initially
cpu_cores_used = 0
memory_used = 0.0

while True:
    user_name = input("Please enter username:")
    try: 
        cpu_cores_required = int(input("Enter the required no. of CPU cores: "))
        memory_gb_required = float(input("Enter the required memory in GB: "))    
    except ValueError:
        print('Please enter a valid integer input for cores and float input for memory.')
        continue

    if (cpu_cores_required <= (CORES_AVAILABLE - cpu_cores_used)) and (memory_gb_required <= (MEMORY_AVAILABLE_GB - memory_used)):
       
        # Allocate resources
        allocated_resources.append({
            'User': user_name,
            'CPU Cores': cpu_cores_required,
            'Memory': memory_gb_required
        })
        cpu_cores_used += cpu_cores_required
        memory_used += memory_gb_required
        
    else:
        # Add to pending requests
        requests_pending.append({
            'User': user_name,
            'CPU Cores': cpu_cores_required,
            'Memory': memory_gb_required
        })
        
    # New Request?
    another_request = input("Do you want to make another request? (yes/no): ").lower()
    if another_request != 'yes':
        break
        
# Result
print("\nAllocated Resources:")
for resource in allocated_resources:
    print(resource)

print("\nPending Requests:")
for request in requests_pending:
    print(request)

