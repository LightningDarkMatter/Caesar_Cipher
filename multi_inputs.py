#Function with more than one input
def greet_with_name (name, age):
    print ("Hello " + name)
    print ("How old are you? " + age)
    print ("Isn't the weather nice today?")

greet_with_name("John", "25")

#Function with more than one input and keyword arguments
def greet_with_name1 (name, age):
    print ("Hello " + name)
    print ("How old are you? " + age)
    print ("Isn't the weather nice today?")

greet_with_name1(age="25", name="John")