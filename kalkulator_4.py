import logging
operation = input("Podaj dziłanie, posługując się opdowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie:")


def calculation(operation, digit_1, digit_2):
    if operation == "1":
        logging.info("Dodaję %s i %s") % (digit_1, digit_2) 
        logging.info("Wynik to: " + (digit_1 + digit_2))
    elif operation == "2":
        logging.info("Odejmuję %s i %s") % (digit_1, digit_2)
        logging.info("Wynik to: " + (digit_1 - digit_2))
    elif operation == "3":
        logging.info("Mnoze %s i %s") % (digit_1, digit_2)
        logging.info("Wynik to: " + (digit_1 * digit_2))
    elif operation == "4":
        logging.info("Dzielę %s i %s") % (digit_1, digit_2)
        logging.info("Wynik to: " + (digit_1 / digit_2))
    else:
        logging.info("Podaj proszę liczbę z zakresu 1-4.")
    return

if __name__ == "__main__":
    
    digit_1 = input("Podaj składnik 1.")
    digit_2 = input("Podaj składnik 2.")
    wynik = calculation(operation, digit_1, digit_2)
print(wynik)