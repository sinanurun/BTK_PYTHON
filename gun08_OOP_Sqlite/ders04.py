# sınıf içinde method tanımlamak
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    #self.fAdYazdir()

  def fAdYazdir(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.fAdYazdir()