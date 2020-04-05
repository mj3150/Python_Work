#!/usr/bin/python3

import pandas as pr 
import pandas_datareader as pdr
from time import sleep
symbols = "AMZN GOOG NFLX FB GLD SPY".split()

options = " Track Default List, Show Default List, Add to Default List, Edit Default List, Add new List, Quit".split(",")

def show_default(symbols):
    symbols.sort()
    return symbols

def add_to_default(symbols):
    print("Enter symbol into add: ")
    symbol = input().upper()
    while symbol != '':
        symbols.append(symbol) 
        symbol = input("Enter symbol to add: Hit enter to quit")

def edit_default(symbols):
    print("Select symbol to delete: ")
    for i in range(1, len(symbols) + 1):
        print("{} - {}".format(i, symbols[i-1]))
    remove = symbols.pop(int(input())-1)
    print("{} removed".format(remove))

def add_list():
    new_list = []
    print("Enter symbol to add: ")
    symbol = input().upper()
    while symbol != '':
        new_list.append(symbol)
        symbol = input("Enter symbol to add or enter to quit: ")
    while True:
        print(get_prices(new_list))
        print("CNTL + C to quit")
def get_prices(symbols):
    symbols.sort()
    return pdr.get_quote_yahoo(symbols)['price']

def main():
    run_program = True
    while run_program:
        print("Choose Option:")
        for i in range(len(options) + 1):
            print("{} - {}".format(i, options[i-1]))
        choice = int(input())
        
        if choice == 1:
            while True:
                print(get_prices(symbols))
                print("CNTL + C to quit")
                sleep(5)
            
        elif choice == 2:
            print(show_default(symbols))
        elif choice == 3:
            add_to_default(symbols)
        elif choice == 4:
            edit_default(symbols)
        elif choice == 5:
            add_list()
        elif choice == 6:
            run_program = False
        
        print(get_prices(symbols))
        print("CNTL + C to quit")
        sleep(5)
        
if __name__ == "__main__":
    main()
#print(pdr.get_quote_yahoo("AAPL")['price'])
