class Employee:
    name = "name"
    language = "python"
    salary = 72000

    # just like Constructor
    def __init__(self, name="harry", salary = 23000, language = "React"): # Dundder method which is automatically called
        print("Hello, Umair.")
        self.name = name
        self.salary = salary
        self.language = language

    def getInfo(self):
        print(f"The language is {self.language}. \nThe name is {self.name}")

    def greet(self):
        print(f"Hello, {self.name}!")
    
     # now you can use method without using self
    @staticmethod
    def hello():
        print("Hello")

harry = Employee("harry", 1200000, "JavaScript")
harry.getInfo()
harry.greet()
harry.hello()
