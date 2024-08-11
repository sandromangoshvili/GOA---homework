def greething(name,lastname):
   return"hello " + name + " " + lastname
name = input("Enter your name: ")
lastname = input("Enter your lastname: ")


print(greething(name,lastname))

print("gio jemaliko")


def money(Money):
   if Money >= 10000:
      return "you are rich"
   elif Money >= 5000:
      return "you are okey"
   else:
      return "you are poor"
Money = int(input("Enter your niga money: "))
money(Money)
      