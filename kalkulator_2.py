import logging
logging.basicConfig(format ="",level=logging.DEBUG)

choice = int(input ("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
first_arg = int(input("Podaj składnik 1: "))
second_arg = int(input("Podaj składnik 2: "))

def add (a, b):
  return a+b
def substract (a, b):
  return a-b
def multiply (a, b):
  return a*b
def divide (a, b):
  return a/b

d = {1: add,
     2: substract,
     3: multiply,
     4: divide
}

function = d[choice]
result = function(first_arg, second_arg)

if choice == 1:
  logging.info("Dodaję: " + str(first_arg) + " i " + str(second_arg))
  print ("Wynik to " + str(result))
elif choice == 2:
  logging.info("Odejmuję: " + str(first_arg) + " i " + str(second_arg))
  print("Wynik to " + str(result))
elif choice == 3:
  logging.info("Mnożę: " + str(first_arg) + " i " + str(second_arg))
  print("Wynik to " + str(result))
elif choice == 4:
  logging.info("Dzielę: " + str(first_arg) + " i " + str(second_arg))
  print("Wynik to " + str(result))