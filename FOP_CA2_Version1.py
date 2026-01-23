import os

SEPARATOR = "-" * 87
LONG_SEPARATOR = "-" * 173

IDX_NO = 0
IDX_NAME = 1
IDX_CAP = 2
IDX_QTY = 3
IDX_BUY = 4
IDX_CURRENT = 5

cryptoPortfolioDB = [
    [1, "Bitcoin", "High", 15, 38000, 62000],
    [2, "Ethereum", "High", 90, 4200, 3500],
    [3, "Solana", "Mid", 60, 260, 110],
    [4, "Decentraland", "Mid", 30000, 1.5, 5],
    [5, "The Sandbox", "Mid", 25000, 2, 4],
    [6, "Dogecoin", "Low", 55000, 0.4, 0.15]
]

def mainMenu():
    print(SEPARATOR)
    print("Class: EL/EP0301/FT/01")
    print("1. Sherie Eyo Zi Xin")
    print("2. Nur Adhilla Binte Abdul Rahman")
    print(SEPARATOR)
    print("                    Crytocurrency Portfolio Application Main Menu")
    print(SEPARATOR)
    print("1. Display Cryptocurrency")
    print("2. Add Cryptocurrency")
    print("3. Amend Cryptocurrency")
    print("4. Remove Cryptocurrency")
    print("5. Crypto Portfolio Statement")
    print("6. <Student 1 to propose a new function>")
    print("7. <Student 2 to propose a new function>")
    print("E. Exit Main Menu")
    print(SEPARATOR)
    return input("Select an option: ")

def formatNumber(number):
    if number == int(number):
        return str(int(number))
    else:
        return f"{number:.2f}"
    
def displayCrypto():
    while(True):
        print(SEPARATOR)
        print(f"{'No':<7}{'Name':<17}{'Capitalization':<19}{'QtyBought':<14}{'Bought Price':<17}{'Current Price'}")
        print(SEPARATOR)
        for crypto in cryptoPortfolioDB:
            print(f"{formatNumber(crypto[IDX_NO]):<7}{crypto[IDX_NAME]:<17}{crypto[IDX_CAP]:<19}{formatNumber(crypto[IDX_QTY]):<14}{formatNumber(crypto[IDX_BUY]):<17}{formatNumber(crypto[IDX_CURRENT])}")
        print(SEPARATOR)
        exitOption = input("Enter E to exit : ")

        if exitOption.upper() == "E":
            break

        os.system('cls')

def addCrypto():
    print(SEPARATOR)
    cryptoNumber = len(cryptoPortfolioDB) + 1
    
    while(True):
        cryptoName = input("Enter Cryptocurrency Name : ").strip()

        exists = False
        for crypto in cryptoPortfolioDB:
            if crypto[IDX_NAME].lower() == cryptoName.lower():
                exists = True
                break

        if exists:
            print("\033[31mError: Cryptocurrency already exists in database.\033[0m")
        elif cryptoName == "":
            print("\033[31mError: Name cannot be empty.\033[0m")
        else:
            break

    while(True):
        marketCap = input("Enter Market Cap of Crypto: High, Mid, Low : ")
        if marketCap == "High" or marketCap == "Mid" or marketCap == "Low":
            break
        else:
            print("\033[31mError: Please enter a valid response.\033[0m")

    while(True):
        try:
            quantityBought = float(input("Enter Quantity of Crypto Bought = "))
            break
        except ValueError:
            print("\033[31mError: Please enter a valid number.\033[0m")

    while(True):
        try:
            boughtPrice = float(input("Enter Buy In Price of Crypto = "))
            break
        except ValueError:
            print("\033[31mError: Please enter a valid number.\033[0m")

    while(True):
        try:
            currentPrice = float(input("Enter Market Price of Crypto = "))
            break
        except ValueError:
            print("\033[31mError: Please enter a valid number.\033[0m")
    print(SEPARATOR)

    newCrypto = [cryptoNumber, cryptoName, marketCap, quantityBought, boughtPrice, currentPrice]
    cryptoPortfolioDB.append(newCrypto)
    
def amendCrypto():
    breakLoops = False

    print(SEPARATOR)
    print("No - Cryptocurrency")
    print(SEPARATOR)
    for crypto in cryptoPortfolioDB:
        print(f"{crypto[IDX_NO] - 1} - {crypto[IDX_NAME]}")
    print(SEPARATOR)

    while(True):
        amendOption = input(f"Enter 0 to {len(cryptoPortfolioDB) - 1} for your selection or E to exit : ")

        if amendOption.upper() == "E":
            break
        elif amendOption.isdigit():
            if int(amendOption) >= 0 and int(amendOption) <= (len(cryptoPortfolioDB) - 1):
                while(True):
                    os.system('cls') 
                    print(SEPARATOR)
                    print(f"Index                       : {amendOption}")
                    print(f"1. Name                     : {cryptoPortfolioDB[int(amendOption)][IDX_NAME]}")
                    print(f"2. Market Cap               : {cryptoPortfolioDB[int(amendOption)][IDX_CAP]}")
                    print(f"3. Quantity Bought          : {cryptoPortfolioDB[int(amendOption)][IDX_QTY]}")
                    print(f"4. Buy In Price             : {cryptoPortfolioDB[int(amendOption)][IDX_BUY]}")
                    print(f"5. Market Price             : {cryptoPortfolioDB[int(amendOption)][IDX_CURRENT]}")
                    print(f"E. Edit Completed. Exit")
                    print(SEPARATOR)
                    while(True):
                        editOption = input("What do you want to edit : ")

                        if editOption == "1":
                            while(True):
                                cryptoName = input(f"({editOption}) Enter new Cryptocurrency Name : ").strip()

                                exists = False
                                for crypto in cryptoPortfolioDB:
                                    if crypto[IDX_NAME].lower() == cryptoName.lower():
                                        exists = True
                                        break

                                if exists:
                                    print("\033[31mError: Cryptocurrency already exists in database.\033[0m")
                                elif cryptoName == "":
                                    print("\033[31mError: Name cannot be empty.\033[0m")
                                else:
                                    cryptoPortfolioDB[int(amendOption)][IDX_NAME] = cryptoName
                                    break
                            break                            

                        elif editOption == "2":
                            while(True):
                                marketCap = input(f"({editOption}) Enter new Market Cap of Crypto: High, Mid, Low : ")
                                if marketCap == "High" or marketCap == "Mid" or marketCap == "Low":
                                    cryptoPortfolioDB[int(amendOption)][IDX_CAP] = marketCap
                                    break
                                else:
                                    print("\033[31mError: Please enter a valid response.\033[0m")
                            break 

                        elif editOption == "3":
                            while(True):
                                try:
                                    cryptoPortfolioDB[int(amendOption)][IDX_QTY] = float(input(f"({editOption}) Enter new Quantity of Crypto Bought = "))
                                    break
                                except ValueError:
                                    print("\033[31mError: Please enter a valid number.\033[0m")
                            break 

                        elif editOption == "4":
                            while(True):
                                try:
                                    cryptoPortfolioDB[int(amendOption)][IDX_BUY] = float(input(f"({editOption}) Enter new Buy In Price of Crypto = "))
                                    break
                                except ValueError:
                                    print("\033[31mError: Please enter a valid number.\033[0m")    
                            break                     

                        elif editOption == "5":
                            while(True):
                                try:
                                    cryptoPortfolioDB[int(amendOption)][IDX_CURRENT] = float(input(f"({editOption}) Enter new Market Price of Crypto = "))
                                    break
                                except ValueError:
                                    print("\033[31mError: Please enter a valid number.\033[0m")     
                            break                         

                        elif editOption.upper() == "E":
                            breakLoops = True
                            break
                        
                        else:
                            print("\033[31mInvalid Option, please try again.\033[0m")      
                    if breakLoops:
                        break       
            else:
                print("\033[31mInvalid Option, please try again.\033[0m")
        else:
            print("\033[31mInvalid Option, please try again.\033[0m")

        if breakLoops:
            break     

def removeCrypto():
    print(SEPARATOR)
    print("No - Cryptocurrency")
    print(SEPARATOR)
    for crypto in cryptoPortfolioDB:
        print(f"{crypto[IDX_NO] - 1} - {crypto[IDX_NAME]}")
    print(SEPARATOR)

    while(True):
        removeOption = input(f"Enter 0 to {len(cryptoPortfolioDB) - 1} for your selection or E to exit : ")

        if removeOption.upper() == "E":
            break

        elif removeOption.isdigit():
            if int(removeOption) >= 0 and int(removeOption) <= (len(cryptoPortfolioDB) - 1):
                cryptoPortfolioDB.pop(int(removeOption))

                indexUpdater = 1
                for crypto in cryptoPortfolioDB:
                    crypto[IDX_NO] = indexUpdater
                    indexUpdater += 1

                break
            else:
                print("\033[31mInvalid Option, please try again.\033[0m")

        else:
            print("\033[31mInvalid Option, please try again.\033[0m")

def cryptoPortfolioStatement():
    while True:
        totalInvested = 0
        totalCurrentValue = 0
        
        for crypto in cryptoPortfolioDB:
            totalInvested += crypto[IDX_QTY] * crypto[IDX_BUY]
            totalCurrentValue += crypto[IDX_QTY] * crypto[IDX_CURRENT]
        
        print(LONG_SEPARATOR)
        print(f"{'No':<6}{'Name':<16}{'QtyBought':<13}{'Bought Price':<16}{'Current Price':<17}"
              f"{'Total Invested':<18}{'Invested Portfolio Size':<27}{'Total Current Value':<23}{'Profit/Loss':<15}{'Current Portfolio Size'}")
        print(LONG_SEPARATOR)
        
        for crypto in cryptoPortfolioDB:
            quantity = crypto[IDX_QTY]
            boughtPrice = crypto[IDX_BUY]
            currentPrice = crypto[IDX_CURRENT]
            
            totalInvestedCrypto = quantity * boughtPrice
            investedPercentage = (totalInvestedCrypto / totalInvested) * 100
            
            totalCurrentCrypto = quantity * currentPrice
            profitLoss = totalCurrentCrypto - totalInvestedCrypto
            currentPercentage = (totalCurrentCrypto / totalCurrentValue) * 100
            
            print(f"{crypto[IDX_NO]:<6}{crypto[IDX_NAME]:<16}{quantity:<13}{formatNumber(boughtPrice):<16}"
                f"{formatNumber(currentPrice):<17}{formatNumber(totalInvestedCrypto):<18}"
                f"{formatNumber(investedPercentage) + '%':<27}{formatNumber(totalCurrentCrypto):<23}"
                f"{formatNumber(profitLoss):<15}{formatNumber(currentPercentage) + '%'}")
        
        print(LONG_SEPARATOR)
        print(f"{'SUM':<68}{formatNumber(totalInvested):<45}{formatNumber(totalCurrentValue):<23}{formatNumber(totalCurrentValue - totalInvested)}")
        print(LONG_SEPARATOR)
        exitOption = input("Enter E to exit : ")

        if exitOption.upper() == "E":
            break

        os.system('cls')

def functionSix():
    return

def functionSeven():
    return

def launchApplication():
    os.system('cls')

    while(True):
        option = mainMenu()
        
        if option == "1":
            os.system('cls')
            displayCrypto()
            os.system('cls')
        elif option == "2":
            os.system('cls')
            addCrypto()
            os.system('cls')
        elif option == "3":
            os.system('cls')
            amendCrypto()   
            os.system('cls') 
        elif option == "4":
            os.system('cls')
            removeCrypto()  
            os.system('cls') 
        elif option == "5":
            os.system('cls')
            cryptoPortfolioStatement() 
            os.system('cls')
        elif option == "6":
            os.system('cls')
            functionSix()     
            os.system('cls')
        elif option == "7":
            os.system('cls')
            functionSeven()
            os.system('cls')
        elif option.upper() == "E":
            os.system('cls')
            break   
        else:
            os.system('cls') 

launchApplication()