class Programmer:
     def __init__(self, name="Peter", age='20'):
          self.name = name
          self.age = age

     def set_name(self):
          name = input("Name? :")
          self.name = name

     def set_age(self):
          age = input("Age? :")
          self.age = age

     def get_name(self):
          print(name)

     def get_age(self):
          print(age)

def main():
     name = Programmer()
     name.set_name()
     name.set_age()
     print(name.get_name())
     print(name.get_age())

if __name__ == "__main__":
     main()
