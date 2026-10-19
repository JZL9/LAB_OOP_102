from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name:str, employee_id:int):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if not isinstance(employee_id, int) or employee_id <= 0:
            raise ValueError("Employee ID must be positive")
        self.name = name
        self.__employee_id = employee_id
    def get_employee_id(self):
        return self.__employee_id

    def display_info(self):
        print(f"Employee: {self.name} ID: {self.get_employee_id()}")

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        if not isinstance(monthly_salary, int) or monthly_salary <= 0:
            raise ValueError("Monthly salary must be a positive number")
        self.monthly_salary = monthly_salary
    def calculate_salary(self):
        return self.monthly_salary