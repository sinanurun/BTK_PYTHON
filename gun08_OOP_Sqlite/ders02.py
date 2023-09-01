class Person:
  def __init__(self, name="Adsız", age=0):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

p2 = Person()

print(p2.name)
print(p2.age)