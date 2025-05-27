class student: # Student is a class

     # Class variable
    School = "Vishesh High School" # This is a class variable shared by all instances of the class


    def __init__(self, name, age): # __init__ is a constructor method
        self.name = name
        self.age = age
        
    def display(self): # display is a method of the class
            print(f"Name: {self.name}, Age: {self.age}, School: {self.School}") # Displaying the student's information including the class variable School


    #Instance method to change the class variable
    def change_school(self, new_school):
        self.School = new_school  # This will change the class variable for this instance only
        student.School = new_school  # This will change the class variable for all instances of the class


    # Class method to change the class variable
    @classmethod
    def change_school_class(cls, new_school):
        cls.School = new_school  # This will change the class variable for all instances of the class

    # Static method to change the class variable
    @staticmethod
    def change_school_static(new_school):
        student.School = new_school  # This will change the class variable for all instances of the class






# Creating an instance of the student class
s1= student("Alice", 20) # Instance of student class with name "Alice" and age 20
s2= student("Bob", 22) # Instance of student class with name "Bob" and age 22
s1.age=23
s1.name="Kartheek"
s1.School="Karthik High School" # Changing the class variable for this instance
student.School="Karthik High School" # Changing the class variable for all instances of the class
# Displaying the class variable for both instances



# Calling the display method to show the student's information
s1.display() 
s2.display()
# Output: Name: Alice, Age: 20