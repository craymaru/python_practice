import csv

class Person:
    def say_something(self):
        print('hello')

class Animal:
     def say_something(self):
         print('くぁwせdrftgyふじこlp')

person = Person()
person.say_something()

animal = Animal()
animal.say_something()

class Person:
    def say_something(self):
        print('hello')

class Animal:
     def say_something(self):
         print('くぁwせdrftgyふじこlp')

person = Person()
person.say_something()

animal = Animal()
animal.say_something()



with open("test.csv", "w") as csv_file:
    fieldnames = ["Name", "Count"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Name": "A", "Count": "1"})
    writer.writerow({"Name": "B", "Count": "2"})
