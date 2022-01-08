import logging
logging.basicConfig(format ="",level=logging.DEBUG)
choice = int(input ("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
if choice > 4:
    print("Podaj proszę liczbę od 1 do 4!")
    exit(1)
a = int(input("Podaj składnik 1: "))
b = int(input("Podaj składnik 2: "))

if choice == 1:
  logging.info("Dodaję: " + str(a) + " i " + str(b))
  result = a + b
  print ("Wynik to " + str(result))
elif choice == 2:
  logging.info("Odejmuję: " + str(a) + " i " + str(b))
  result = a - b
  print("Wynik to " + str(result))
elif choice == 3:
  logging.info("Mnożę: " + str(a) + " i " + str(b))
  result = a * b
  print("Wynik to " + str(result))
elif choice == 4:
  logging.info("Dzielę: " + str(a) + " i " + str(b))
  result = a / b
  print("Wynik to " + str(result))
