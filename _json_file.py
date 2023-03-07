import json

class Employee:
    def _init_(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

def main()
    with open('employee.json', 'r') as file:
        data = json.load(file)

    employee_list = []
    for employee_data in data['employees']:
        employee = Employee(employee_data['Name'], employee_data['DOB'], employee_data['Height'], employee_data['City'], employee_data['State'])
        employee_list.append(employee)

    for employee in employee_list:
        print(f"{employee.name} ({employee.dob}), {employee.height}cm, {employee.city}, {employee.state}")

    
    state_capital_dict = {
        "Andhra Pradesh": "Hyderabad",
        "Karnataka": "Bengaluru",
        "Kerala": "Thiruvananthapuram",
        "Maharashtra": "Mumbai",
        "Tamil Nadu": "Chennai",
        "Telangana": "Hyderabad",
        "Uttar Pradesh": "Lucknow"
    }

    with open('state_capitals.json', 'w') as file:
        json.dump(state_capital_dict, file)

if _name_ == '_main_':
    main()