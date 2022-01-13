import logging
logging.basicConfig(format ="",level=logging.DEBUG)
choice = str(input ("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))

a = int(input("Podaj składnik 1: "))
b = int(input("Podaj składnik 2: "))


def calculate(choice):
  return {
        "1": logging.info("Dodaję: " + str(a) + " i " + str(b) + " Wynik to " + int(a+b)), 
        "2": logging.info("Odejmuję: " + str(a) + " i " + str(b) + "/n" + "Wynik to " + int(a-b))
   }[choice]

calculate(choice)