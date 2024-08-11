def hi():
    print("hello sandro")


def good_luck():
    print("good luck")


def its_time(time):
    time = int(input("what time is it?"))
    if time == 11:
        print("Goa class has started")
    else:
        print("Do the Goa homework")


def greething(name):
    print("hello " + name)
name = input("Enter your name: ")


greething(name)


def test(age):
    if age >= 18:
        print("you are adult")
    else:
        print("you are't adult")
age = int(input("Enter your age: "))


test(age)


def money(Money):
    if Money >= 1000:
        print("you are not poor")
    else:
        print("you are poor")

Money = int(input("Enter your money: "))
money(Money)
