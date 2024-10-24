# class , object, constructor(__init__)

# class -> a class is a blueprint for creating objects(instances). class ke attributes aur methods uske sare objects ke bhi honge
# object/instance -> yeh class ka part hote hai

# constructor(__init__): yeh automatically call hojata hai jab ham ham kisi class ke object ko create karte hai.

class Car :
    def __init__(self,brand,year,type):
        self.brand = brand      # instance variable
        self.year = int(year)   # instance variable
        self.type = type        # instance variable

    def display_info(self):  #method
        print (f"car: {self.brand}, {self.year}, {self.type}")

# creating an object of the car class
car_1 = Car('toyota',2020, 'SUV')


car_1.display_info()
Car.display_info(car_1)




# INSTANCE VARIABLES, CLASS VARIABLES AND CLASS METHODS, STATIC METHODS


# instance variable --> these are varibles that are unique to each object

# class variable --> these variables are shared across all instances of class
# yeh sare methods ke bahar define hota hai aur class ko belong karte hai rather than any individual object.

# classmethods - woh method/function jo ki keval class me hi bound rahte hai and not objects of the class 
# declared with @classmethod decorator and take cls as first parameter

# staticmethods - inko class aur object dono se hi koi matlab nahi hai, they are normal functions but belong to class namespace


class Student:
    College_name = "AKGEC, gzb"      # class varibale ( shared by all objects)

    def __init__(self,first_name,last_name,age):
        self.first_name = first_name # instance varibale
        self.last_name = last_name   # instance varibale
        self.age = age               # instance varibale

    @classmethod
    def get_college_name(cls):       # class method
        return cls.College_name
    
# accessing class varible and class method
print(Student.get_college_name())


class Calculator:
    @staticmethod
    def add(a,b):
        return a + b
    
    @staticmethod
    def sub(a,b):
        return a-b
    
    @staticmethod
    def mul(a,b):
        return a * b
    
    @staticmethod
    def Div(a,b):
        return a / b
    
# calling static methods without directly creatng an object

print(Calculator.add(23,6))
print(Calculator.sub(23,6))
print(Calculator.mul(23,6))
print(Calculator.Div(23,6))

    
# INHERITANCE
# it allows one class(child class) to inherit attributes and methods from another class(parent class).

# POLYMORPHISM
# isme same methods ki different implementation ho sakti hai different classes me 
# used in context of inheritance

class Employee:  # Employee class
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def work (self):
        return f"{self.fname} {self.lname} is working."
    
    def get_salary(self):
        return f"{self.fname} {self.lname}'s salary is {self.salary}"
    

#(Child class) inheriting from Employee
class Manager(Employee):
    def __init__(self,fname,lname,salary,department):
        super().__init__(fname,lname,salary)
        self.department = department

    # Polymorphism: Overriding the work method
    def work(self):
        return f"{self.fname} {self.lname} is managing the {self.department} department"


# polymorphism
def employee_work(employee):
    print(employee.work())



# employee instance
emp_1 = Employee("Anagh","jaiswar",60000)
# Manager object (which inherits from employee)
mgr_1 = Manager("pradeep","Saxena",61000,"sales")


print(mgr_1.get_salary())
print(mgr_1.department)


# using polymorphism
employee_work(emp_1)
employee_work(mgr_1)

# When employee_work() is called, it takes either an Employee or a Manager object and 
# calls their respective work() method based on the actual type of the object. 


# ENCAPSULATION
# process of restricting access to certain attributes or methods in an object. 
# we can do this by using single underscore (_) or double underscore(__).

# ABSTRACTION
# it hides complex implementation detailsns exposes the essential essential feature.

class Account:
    def __init__(self,balance):
        self.__balance = balance   #private variable

    def deposit(self,amount):
        if amount>0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance


account = Account(500)
# print(account.__balance)  # not possible to access directly as it is private variable
account.deposit(1000)
print(account.get_balance())




# GENERATORS
# special  function that yeilds value one at a time ,we cn iterate over large data sets without consuming lots of memory.
# it returns an iterator that generates item lazily.


def countdown(n):
    while n>0:
        yield n  #yield pauses the function and return the value.
        n -= 1

for count in countdown(5):
    print(count)



# LIST COMPREHENSION
squares = [x**2 for x in range(5)]
print (squares)


# DICT COMPREHENSION
squares_dict = {x:x**2 for x in range (5)}
print(squares_dict)


# SET COMPREHENSION
square = {x**2 for x in range(10)}
print(square)



# HIGHER ORDER FUNCTIONS
# a function that takes another function as a argument

def add_five(x):
    return x + 5

def apply_twice(func,value):
    return func(func(value))

print(apply_twice(add_five,10))

# firstly apply twice fn. will be called and it will return add_five(add_five,10)
# then (add_five,10) will return 15. fn will become add_five(15) whichc returns 20.


# LAMBDA FUNCTIONS
# anonymous, inline functions for quick, throwaway operations.

add = lambda x,y : x+y
print(add(5,4))

# map() --> Applies a function to all items in an input list.
numbers = [1,2,3,4]
squared = map(lambda x : x**2 , numbers)
print(list(squared))

# filter --> Filters elements from a list based on a condition.
even_numbers = filter(lambda x: x%2 == 0 ,numbers)
print(list(even_numbers))

# reduce() --> cumulatively applies to function to all items, reducing the list to a single value

from functools import reduce
sum_of_numbers = reduce(lambda x,y: x+y,numbers)
print(sum_of_numbers)
