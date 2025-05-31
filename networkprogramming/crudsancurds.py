import requests
import json

BASE_URL = 'https://q8qmdclj-5001.use.devtunnels.ms'  # Change to your API base URL if different

def create_employee(name, email, position):
    url = BASE_URL+"/employee"
    data = {
        "name": name,
        "email": email,
        "position": position
    }
    response = requests.post(url,json=data)
    if response.status_code == 201:
        print(f"Employee created: {name}")
    else:
        print(f"Failed to create employee: {response.json()}")

def get_employees():
    url = BASE_URL+"/employees"
    response = requests.get(url)
    if response.status_code == 200:
        employees = response.json()
        print(f"Employees: {json.dumps(employees, indent=2)}")
    else:
        print("Failed to get employees")
        
def getemployeebyid(employee_id):
    url = BASE_URL+f"/employee/{employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        employee = response.json()
        print(f"Employee: {json.dumps(employee, indent=2)}")
    else:
        print(f"Failed to get employee with ID {employee_id}: {response.json()}")
        
def update_employee(employee_id, name, email, position):
    url = BASE_URL+f"/employee/{employee_id}"
    data = {
        "name": name,
        "email": email,
        "position": position
    }
    response =requests.put(url,json=data)
    if response.status_code == 200:
        print(f"Employee with ID {employee_id} updated")
    else:
        print(f"Failed to update employee with ID {employee_id}: {response.json()}")

def delete_employee(employee_id):
    url = BASE_URL+f"/employee/{employee_id}"
    response = requests.delete(url)
    if response.status_code == 200:
        print(f"Employee with ID {employee_id} deleted")
    else:
        print(f"Failed to delete employee with ID {employee_id}: {response.json()}")

def download_employees_csv():
    url =BASE_URL+"/employee/download/csv"
    response = requests.get(url)
    if response.status_code == 200:
        with open('employees.csv', 'wb') as f:
            f.write(response.content)
        print("CSV file of employees downloaded as 'employees.csv'")
    else:
        print(f"Failed to download CSV: {response.json()}")
        
def main():
    # 1. Create Employees
    create_employee("Venom", "wearvenom@venom.com", "Is Venom")
    create_employee("Technoblade", "technoblade@gmail.com", "Is Technoblade")
    
    # 2. Get All Employees
    get_employees()
    
    # 3. Get Employee by ID
    requestsget_employee_by_id(1)  # Assuming employee with ID 1 exists

    # # 4. Update Employee
    # update_employee(1, "Alice Smith Updated", "alice.smith.updated@example.com", "Senior Software Developer")
    
    # # 5. Delete Employee
    # delete_employee(2)  # Assuming employee with ID 2 exists

    # # 6. Upload Profile Image for an Employee
    # # Note: Change the path to an actual image file you want to upload
    # #upload_profile_image(1, 'path_to_image.jpg')

    # # 7. Download Employees CSV
    # download_employees_csv()
    
if __name__=="__main__":
    # main()
    # getemployeebyid(7)
    # get_employees()
    # update_employee(7, "Technoblade", "technobladeneverdies@gmail.com", "Was Technoblade")
    # delete_employee(1)
    download_employees_csv()