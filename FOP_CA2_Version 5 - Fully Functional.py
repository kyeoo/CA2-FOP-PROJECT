import os
import requests

SEPARATOR = "-" * 88
MID_LENGTH_SEPARATOR = "-" * 149
LONG_SEPARATOR = "-" * 174

IDX_NO = 0
IDX_NAME = 1
IDX_CAP = 2
IDX_QTY = 3
IDX_BUY = 4
IDX_CURRENT = 5

cryptoPortfolioDatabase = [
    [1, "Bitcoin", "High", 15, 38000, 62000],
    [2, "Ethereum", "High", 90, 4200, 3500],
    [3, "Solana", "Mid", 60, 260, 110],
    [4, "Decentraland", "Mid", 30000, 1.5, 5],
    [5, "The Sandbox", "Mid", 25000, 2, 4],
    [6, "Dogecoin", "Low", 55000, 0.4, 0.15]
]

liveCryptoPrices = {}


def mainMenu():
    print(SEPARATOR)
    print("Class: EL/EP0301/FT/01")
    print("1. Sherie Eyo Zi Xin")
    print("2. Nur Adhilla Binte Abdul Rahman")
    print(SEPARATOR)
    print("Crytocurrency Portfolio Application Main Menu".center(len(SEPARATOR)))
    print(SEPARATOR)
    print("1. Display Cryptocurrency")
    print("2. Add Cryptocurrency")
    print("3. Amend Cryptocurrency")
    print("4. Remove Cryptocurrency")
    print("5. Crypto Portfolio Statement")
    print("6. Portfolio Business Analysis (Live Data)")
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
    while True:
        print(SEPARATOR)
        print("Display Cryptocurrency".center(len(SEPARATOR)))
        print(SEPARATOR)
        print(f"{'No':<7}{'Name':<17}{'Capitalization':<19}{'Qty Bought':<15}{'Bought Price':<17}{'Current Price'}")
        print(SEPARATOR)

        for cryptoRecord in cryptoPortfolioDatabase:
            print(f"{formatNumber(cryptoRecord[IDX_NO]):<7}{cryptoRecord[IDX_NAME]:<17}{cryptoRecord[IDX_CAP]:<19}{formatNumber(cryptoRecord[IDX_QTY]):<15}{formatNumber(cryptoRecord[IDX_BUY]):<17}{formatNumber(cryptoRecord[IDX_CURRENT])}")

        print(SEPARATOR)
        exitOption = input("Enter E to exit : ")

        if exitOption.upper() == "E":
            break

        os.system('cls')


def addCrypto():
    print(SEPARATOR)
    print("Add Cryptocurrency".center(len(SEPARATOR)))
    print(SEPARATOR)
    newCryptoNumber = len(cryptoPortfolioDatabase) + 1

    while True:
        newCryptoName = input("Enter Cryptocurrency Name : ").strip()

        isDuplicateCryptoName = False
        for cryptoRecord in cryptoPortfolioDatabase:
            if cryptoRecord[IDX_NAME].lower() == newCryptoName.lower():
                isDuplicateCryptoName = True
                break

        if isDuplicateCryptoName:
            print("\033[31mError: This cryptocurrency already exists in your portfolio database.\033[0m\n")
        elif newCryptoName == "":
            print("\033[31mError: Cryptocurrency name cannot be blank. Please enter a valid name.\033[0m\n")
        else:
            break

    print()

    while True:
        newCryptoMarketCapitalization = input("Enter Market Cap of Crypto: High, Mid, Low : ")
        if (newCryptoMarketCapitalization.title() == "High" or newCryptoMarketCapitalization.title() == "Mid" or newCryptoMarketCapitalization.title() == "Low"):
            newCryptoMarketCapitalization = newCryptoMarketCapitalization.title()
            break
        else:
            print("\033[31mError: Invalid Narket Cap. Please enter High, Mid, or Low.\033[0m\n")

    print()

    while True:
        try:
            newCryptoQuantityBought = float(input("Enter Quantity of Crypto Bought = "))
            break
        except ValueError:
            print("\033[31mError: Invalid input. Please enter a numeric value (e.g., 12 or 12.5).\033[0m\n")

    print()

    while True:
        try:
            newCryptoBoughtPrice = float(input("Enter Buy In Price of Crypto = "))
            break
        except ValueError:
            print("\033[31mError: Invalid input. Please enter a numeric value (e.g., 12 or 12.5).\033[0m\n")

    print()

    while True:
        try:
            newCryptoCurrentMarketPrice = float(input("Enter Market Price of Crypto = "))
            break
        except ValueError:
            print("\033[31mError: Invalid input. Please enter a numeric value (e.g., 12 or 12.5).\033[0m\n")

    print(SEPARATOR)

    newCryptoRecord = [
        newCryptoNumber,
        newCryptoName,
        newCryptoMarketCapitalization,
        newCryptoQuantityBought,
        newCryptoBoughtPrice,
        newCryptoCurrentMarketPrice
    ]
    cryptoPortfolioDatabase.append(newCryptoRecord)


def amendCrypto():
    shouldExitAmendLoops = False

    print(SEPARATOR)
    print("Amend Cryptocurrency".center(len(SEPARATOR)))
    print(SEPARATOR)
    print("No - Cryptocurrency")
    print(SEPARATOR)

    for cryptoRecord in cryptoPortfolioDatabase:
        print(f"{cryptoRecord[IDX_NO] - 1} - {cryptoRecord[IDX_NAME]}")

    print(SEPARATOR)

    while True:
        selectedCryptoIndexToAmend = input(f"Enter 0 to {len(cryptoPortfolioDatabase) - 1} for your selection or E to exit : ")

        if selectedCryptoIndexToAmend.upper() == "E":
            break

        elif selectedCryptoIndexToAmend.isdigit():
            if (int(selectedCryptoIndexToAmend) >= 0 and int(selectedCryptoIndexToAmend) <= (len(cryptoPortfolioDatabase) - 1)):
                while True:
                    os.system('cls')
                    print(SEPARATOR)
                    print("Amend Cryptocurrency".center(len(SEPARATOR)))
                    print(SEPARATOR)
                    print(f"Index                       : {selectedCryptoIndexToAmend}")
                    print(f"1. Name                     : {cryptoPortfolioDatabase[int(selectedCryptoIndexToAmend)][IDX_NAME]}")
                    print(f"2. Market Cap               : {cryptoPortfolioDatabase[int(selectedCryptoIndexToAmend)][IDX_CAP]}")
                    print(f"3. Quantity Bought          : {cryptoPortfolioDatabase[int(selectedCryptoIndexToAmend)][IDX_QTY]}")
                    print(f"4. Buy In Price             : {cryptoPortfolioDatabase[int(selectedCryptoIndexToAmend)][IDX_BUY]}")
                    print(f"5. Market Price             : {cryptoPortfolioDatabase[int(selectedCryptoIndexToAmend)][IDX_CURRENT]}")
                    print(f"E. Edit Completed. Exit")
                    print(SEPARATOR)

                    while True:
                        selectedFieldToEdit = input("What do you want to edit : ")

                        if selectedFieldToEdit == "1":
                            print()

                            while True:
                                updatedCryptoName = input(f"({selectedFieldToEdit}) Enter new Cryptocurrency Name : ").strip()

                                isDuplicateCryptoName = False
                                for cryptoRecord in cryptoPortfolioDatabase:
                                    if cryptoRecord[IDX_NAME].lower() == updatedCryptoName.lower():
                                        isDuplicateCryptoName = True
                                        break

                                if isDuplicateCryptoName:
                                    print("\033[31mError: This cryptocurrency already exists in your portfolio database.\033[0m\n")
                                elif updatedCryptoName == "":
                                    print("\033[31mError: Cryptocurrency name cannot be blank. Please enter a valid name.\033[0m\n")
                                else:
                                    cryptoPortfolioDatabase[int(selectedCryptoIndexToAmend)][IDX_NAME] = updatedCryptoName
                                    break

                            break

                        elif selectedFieldToEdit == "2":
                            print()

                            while True:
                                updatedMarketCapitalization = input(f"({selectedFieldToEdit}) Enter new Market Cap of Crypto: High, Mid, Low : ")
                                if (updatedMarketCapitalization.title() == "High" or updatedMarketCapitalization.title() == "Mid" or updatedMarketCapitalization.title() == "Low"):
                                    cryptoPortfolioDatabase[int(selectedCryptoIndexToAmend)][IDX_CAP] = updatedMarketCapitalization.title()
                                    break
                                else:
                                    print("\033[31mError: Invalid Narket Cap. Please enter High, Mid, or Low.\033[0m\n")

                            break

                        elif selectedFieldToEdit == "3":
                            print()

                            while True:
                                try:
                                    cryptoPortfolioDatabase[int(selectedCryptoIndexToAmend)][IDX_QTY] = float(input(f"({selectedFieldToEdit}) Enter new Quantity of Crypto Bought = "))
                                    break
                                except ValueError:
                                    print("\033[31mError: Invalid input. Please enter a numeric value (e.g., 12 or 12.5).\033[0m\n")

                            break

                        elif selectedFieldToEdit == "4":
                            print()

                            while True:
                                try:
                                    cryptoPortfolioDatabase[int(selectedCryptoIndexToAmend)][IDX_BUY] = float(input(f"({selectedFieldToEdit}) Enter new Buy In Price of Crypto = "))
                                    break
                                except ValueError:
                                    print("\033[31mError: Invalid input. Please enter a numeric value (e.g., 12 or 12.5).\033[0m\n")

                            break

                        elif selectedFieldToEdit == "5":
                            print()

                            while True:
                                try:
                                    cryptoPortfolioDatabase[int(selectedCryptoIndexToAmend)][IDX_CURRENT] = float(input(f"({selectedFieldToEdit}) Enter new Market Price of Crypto = "))
                                    break
                                except ValueError:
                                    print("\033[31mError: Invalid input. Please enter a numeric value (e.g., 12 or 12.5).\033[0m\n")

                            break

                        elif selectedFieldToEdit.upper() == "E":
                            shouldExitAmendLoops = True
                            break

                        else:
                            print("\033[31mError: Invalid selection. Please try again.\033[0m\n")

                    if shouldExitAmendLoops:
                        break

            else:
                print("\033[31mError: Invalid selection. Please try again.\033[0m\n")

        else:
            print("\033[31mError: Invalid selection. Please try again.\033[0m\n")

        if shouldExitAmendLoops:
            break


def removeCrypto():
    print(SEPARATOR)
    print("Remove Cryptocurrency".center(len(SEPARATOR)))
    print(SEPARATOR)
    print("No - Cryptocurrency")
    print(SEPARATOR)

    for cryptoRecord in cryptoPortfolioDatabase:
        print(f"{cryptoRecord[IDX_NO] - 1} - {cryptoRecord[IDX_NAME]}")

    print(SEPARATOR)

    while True:
        selectedCryptoIndexToRemove = input(f"Enter 0 to {len(cryptoPortfolioDatabase) - 1} for your selection or E to exit : ")

        if selectedCryptoIndexToRemove.upper() == "E":
            break

        elif selectedCryptoIndexToRemove.isdigit():
            if (int(selectedCryptoIndexToRemove) >= 0 and int(selectedCryptoIndexToRemove) <= (len(cryptoPortfolioDatabase) - 1)):
                cryptoPortfolioDatabase.pop(int(selectedCryptoIndexToRemove))

                nextCryptoNumber = 1
                for cryptoRecord in cryptoPortfolioDatabase:
                    cryptoRecord[IDX_NO] = nextCryptoNumber
                    nextCryptoNumber += 1

                break
            else:
                print("\033[31mError: Invalid selection. Please try again.\033[0m\n")

        else:
            print("\033[31mError: Invalid selection. Please try again.\033[0m\n")


def cryptoPortfolioStatement():
    while True:
        totalInvestedValue = 0
        totalCurrentPortfolioValue = 0

        for cryptoRecord in cryptoPortfolioDatabase:
            totalInvestedValue += cryptoRecord[IDX_QTY] * cryptoRecord[IDX_BUY]
            totalCurrentPortfolioValue += cryptoRecord[IDX_QTY] * cryptoRecord[IDX_CURRENT]

        print(LONG_SEPARATOR)
        print("Crypto Portfolio Statement".center(len(LONG_SEPARATOR)))
        print(LONG_SEPARATOR)
        print(f"{'No':<6}{'Name':<16}{'Qty Bought':<14}{'Bought Price':<16}{'Current Price':<17}{'Total Invested':<18}{'Invested Portfolio Size':<27}{'Total Current Value':<23}{'Profit/Loss':<15}{'Current Portfolio Size'}")
        print(LONG_SEPARATOR)

        for cryptoRecord in cryptoPortfolioDatabase:
            cryptoQuantityBought = cryptoRecord[IDX_QTY]
            cryptoBoughtPrice = cryptoRecord[IDX_BUY]
            cryptoCurrentPrice = cryptoRecord[IDX_CURRENT]

            cryptoTotalInvestedValue = cryptoQuantityBought * cryptoBoughtPrice
            cryptoInvestedPortfolioPercentage = (cryptoTotalInvestedValue / totalInvestedValue) * 100

            cryptoTotalCurrentValue = cryptoQuantityBought * cryptoCurrentPrice

            cryptoProfitLossValue = cryptoTotalCurrentValue - cryptoTotalInvestedValue
            cryptoProfitLossFormatted = formatNumber(cryptoProfitLossValue)

            if cryptoProfitLossValue >= 0:
                cryptoProfitLossText = f"\033[32m{cryptoProfitLossFormatted:<15}\033[0m"
            else:
                cryptoProfitLossText = f"\033[31m{cryptoProfitLossFormatted:<15}\033[0m"

            cryptoCurrentPortfolioPercentage = (cryptoTotalCurrentValue / totalCurrentPortfolioValue) * 100

            print(f"{cryptoRecord[IDX_NO]:<6}{cryptoRecord[IDX_NAME]:<16}{cryptoQuantityBought:<14}{formatNumber(cryptoBoughtPrice):<16}{formatNumber(cryptoCurrentPrice):<17}{formatNumber(cryptoTotalInvestedValue):<18}{formatNumber(cryptoInvestedPortfolioPercentage) + '%':<27}{formatNumber(cryptoTotalCurrentValue):<23}{cryptoProfitLossText}{formatNumber(cryptoCurrentPortfolioPercentage) + '%'}")

        overallProfitLossValue = totalCurrentPortfolioValue - totalInvestedValue

        if overallProfitLossValue >= 0:
            overallProfitLossText = f"\033[32m{formatNumber(overallProfitLossValue)}\033[0m"
        else:
            overallProfitLossText = f"\033[31m{formatNumber(overallProfitLossValue)}\033[0m"

        print(LONG_SEPARATOR)
        print(f"{'SUM':<69}{formatNumber(totalInvestedValue):<45}{formatNumber(totalCurrentPortfolioValue):<23}{overallProfitLossText}")
        print(LONG_SEPARATOR)

        exitOption = input("Enter E to exit : ")

        if exitOption.upper() == "E":
            break

        os.system('cls')


def portfolioBusinessAnalysisMenu():
    print(SEPARATOR)
    print("Portfolio Business Analysis (Live Data)".center(len(SEPARATOR)))
    print(SEPARATOR)
    print("1. Live Price Comparison")
    print("2. Real-Time Portfolio Report")
    print("3. Market Volatility Risk Analysis")
    print("4. Live Market Scenario Simulation")
    print("5. Investment Recommendation")
    print("E. Exit to Main Menu")
    print(SEPARATOR)
    return input("Select an option: ")


def fetchLivePrices():
    global liveCryptoPrices
    liveCryptoPrices = {}

    coinGeckoDemoApiKey = "CG-HcdtNTwkUzhnzNP9yKCcRmWH"

    for cryptoRecord in cryptoPortfolioDatabase:
        cryptoName = cryptoRecord[IDX_NAME]

        coinGeckoCryptoId = cryptoName.lower().replace(" ", "-")

        coinGeckoApiUrl = f"https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids={coinGeckoCryptoId}&x_cg_demo_api_key={coinGeckoDemoApiKey}"

        try:
            apiResponse = requests.get(coinGeckoApiUrl, timeout=5)
            apiResponseData = apiResponse.json()

            if coinGeckoCryptoId in apiResponseData and "usd" in apiResponseData[coinGeckoCryptoId]:
                liveMarketPriceUsd = apiResponseData[coinGeckoCryptoId]["usd"]
                liveCryptoPrices[cryptoName] = liveMarketPriceUsd
            else:
                liveCryptoPrices[cryptoName] = "\033[90mNO LIVE DATA (N/A)\033[0m"

        except Exception as e:
            liveCryptoPrices[cryptoName] = "LIVE DATA ERROR (CoinGecko API)"


def livePriceComparison():
    while True:
        print(SEPARATOR)
        print("Live Price Comparison".center(len(SEPARATOR)))
        print(SEPARATOR)
        print(f"{'No':<10}{'Name':<20}{'Stored Price':<21}{'Live Price':<18}{'Change'}")
        print(SEPARATOR)

        for cryptoRecord in cryptoPortfolioDatabase:
            cryptoNumber = cryptoRecord[IDX_NO]
            cryptoName = cryptoRecord[IDX_NAME]
            storedCurrentPrice = cryptoRecord[IDX_CURRENT]
            liveMarketPrice = liveCryptoPrices.get(cryptoName)

            if isinstance(liveMarketPrice, (int, float)):
                priceDifference = liveMarketPrice - storedCurrentPrice

                if storedCurrentPrice != 0:
                    priceDifferencePercentage = (priceDifference / storedCurrentPrice) * 100
                else:
                    priceDifferencePercentage = 0

                priceChangeText = f"{priceDifference:+.2f} ({priceDifferencePercentage:+.2f}%)"

                if priceDifference >= 0:
                    priceChangeText = "\033[32m" + priceChangeText + "\033[0m"
                else:
                    priceChangeText = "\033[31m" + priceChangeText + "\033[0m"

                print(f"{formatNumber(cryptoNumber):<10}{cryptoName:<20}{formatNumber(storedCurrentPrice):<21}{formatNumber(liveMarketPrice):<18}{priceChangeText}")

            else:
                print(f"{formatNumber(cryptoNumber):<10}{cryptoName:<20}{formatNumber(storedCurrentPrice):<21}{'\033[90mN/A\033[0m':<27}{liveMarketPrice}")

        print(SEPARATOR)

        shouldUpdateStoredPrices = input("Update stored prices with live data? (Y/N): ")

        if shouldUpdateStoredPrices.upper() == "Y":
            for cryptoRecord in cryptoPortfolioDatabase:
                cryptoName = cryptoRecord[IDX_NAME]
                liveMarketPrice = liveCryptoPrices.get(cryptoName)

                if isinstance(liveMarketPrice, (int, float)):
                    cryptoRecord[IDX_CURRENT] = liveMarketPrice

            print("\033[33mUpdate complete: Stored prices have been refreshed using live market data.\033[0m")
            input("\nPress any Key to exit ")
            os.system('cls')
            break

        elif shouldUpdateStoredPrices.upper() == "N":
            print("\033[33mNo update performed: Stored prices remain unchanged.\033[0m")
            input("\nPress any Key to exit ")
            os.system('cls')
            break

        os.system('cls')


def realTimePortfolioReport():
    while True:
        totalInvestedValue = 0
        totalLivePortfolioValue = 0
        missingLiveDataCount = 0

        print(MID_LENGTH_SEPARATOR)
        print("Real Time Portfolio Report".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)
        print(f"{'No':<10}{'Name':<20}{'Qty Bought':<17}{'Buy Price':<17}{'Total Invested':<22}{'Live Price':<18}{'Total Live Value':<24}{'Profit/Loss'}")
        print(MID_LENGTH_SEPARATOR)

        for cryptoRecord in cryptoPortfolioDatabase:
            cryptoNumber = cryptoRecord[IDX_NO]
            cryptoName = cryptoRecord[IDX_NAME]
            cryptoQuantityBought = cryptoRecord[IDX_QTY]
            cryptoBuyPrice = cryptoRecord[IDX_BUY]
            liveMarketPrice = liveCryptoPrices.get(cryptoName)

            investedValue = cryptoQuantityBought * cryptoBuyPrice

            if isinstance(liveMarketPrice, (int, float)):
                liveValue = cryptoQuantityBought * liveMarketPrice
                liveProfitLossValue = liveValue - investedValue
                liveReturnOnInvestmentPercentage = (liveProfitLossValue / investedValue) * 100 if investedValue != 0 else 0

                totalInvestedValue += investedValue
                totalLivePortfolioValue += liveValue

                livePerformanceText = f"{liveProfitLossValue:+.2f} ({liveReturnOnInvestmentPercentage:+.2f}%)"
                livePerformanceText = ("\033[32m" + livePerformanceText + "\033[0m" if liveProfitLossValue >= 0 else "\033[31m" + livePerformanceText + "\033[0m")

                print(f"{formatNumber(cryptoNumber):<10}{cryptoName:<20}{formatNumber(cryptoQuantityBought):<17}{formatNumber(cryptoBuyPrice):<17}{formatNumber(investedValue):<22}{formatNumber(liveMarketPrice):<18}{formatNumber(liveValue):<24}{livePerformanceText}")

            else:
                missingLiveDataCount += 1
                print(f"{formatNumber(cryptoNumber):<10}{cryptoName:<20}{formatNumber(cryptoQuantityBought):<17}{formatNumber(cryptoBuyPrice):<17}{formatNumber(investedValue):<22}{'\033[90mN/A\033[0m':<27}{'\033[90mN/A\033[0m':<33}{'\033[90mNO LIVE DATA (N/A)\033[0m'}")

        print(MID_LENGTH_SEPARATOR)

        totalProfitLossValue = totalLivePortfolioValue - totalInvestedValue
        totalReturnOnInvestmentPercentage = (totalProfitLossValue / totalInvestedValue) * 100 if totalInvestedValue != 0 else 0

        totalPerformanceText = f"{totalProfitLossValue:+.2f} ({totalReturnOnInvestmentPercentage:+.2f}%)"
        totalPerformanceText = ("\033[32m" + totalPerformanceText + "\033[0m" if totalProfitLossValue >= 0 else "\033[31m" + totalPerformanceText + "\033[0m")

        print(f"{'TOTAL':<64}{formatNumber(totalInvestedValue):<18}{'':<22}{formatNumber(totalLivePortfolioValue):<24}{totalPerformanceText}")
        print(MID_LENGTH_SEPARATOR)

        if missingLiveDataCount > 0:
            print(f"\033[33mNote: {missingLiveDataCount} crypto(s) had no live data and were excluded from the TOTAL calculations.\033[0m\n")

        exitOption = input("Enter E to exit : ")
        if exitOption.upper() == "E":
            break

        os.system('cls')


def marketVolatilityRiskAnalysis():
    while True:
        stableDeviationThresholdPercentage = 10
        volatileDeviationThresholdPercentage = 20

        stableAssetCount = 0
        volatileAssetCount = 0
        highlyVolatileAssetCount = 0
        missingLiveDataCount = 0

        totalLivePortfolioValue = 0
        stableAssetsLiveValue = 0
        highlyVolatileAssetsLiveValue = 0
        volatileAssetsLiveValue = 0

        liveHoldingValueList = []
        marketCapLiveValueTotals = {"High": 0, "Mid": 0, "Low": 0}

        print(SEPARATOR)
        print("Market Volatility Risk Analysis".center(len(SEPARATOR)))
        print(SEPARATOR)
        print(f"{'No':<8}{'Name':<18}{'Stored':<14}{'Live':<14}{'Deviation':<16}{'Risk Level'}")
        print(SEPARATOR)

        for cryptoRecord in cryptoPortfolioDatabase:
            cryptoNumber = cryptoRecord[IDX_NO]
            cryptoName = cryptoRecord[IDX_NAME]
            storedCurrentPrice = cryptoRecord[IDX_CURRENT]
            liveMarketPrice = liveCryptoPrices.get(cryptoName)

            if (isinstance(liveMarketPrice, (int, float)) and isinstance(storedCurrentPrice, (int, float)) and storedCurrentPrice != 0):
                deviationPercentage = abs(liveMarketPrice - storedCurrentPrice) / storedCurrentPrice * 100

                if deviationPercentage <= stableDeviationThresholdPercentage:
                    riskLabel = "STABLE"
                    stableAssetCount += 1
                    riskLabelText = f"\033[32m{riskLabel}\033[0m"
                elif deviationPercentage <= volatileDeviationThresholdPercentage:
                    riskLabel = "VOLATILE"
                    volatileAssetCount += 1
                    riskLabelText = f"\033[33m{riskLabel}\033[0m"
                else:
                    riskLabel = "HIGHLY VOLATILE"
                    highlyVolatileAssetCount += 1
                    riskLabelText = f"\033[31m{riskLabel} ⚠\033[0m"

                deviationText = f"{deviationPercentage:.2f}%"

                liveHoldingValue = cryptoRecord[IDX_QTY] * liveMarketPrice
                totalLivePortfolioValue += liveHoldingValue

                if riskLabel == "STABLE":
                    stableAssetsLiveValue += liveHoldingValue
                elif riskLabel == "VOLATILE":
                    volatileAssetsLiveValue += liveHoldingValue
                else:
                    highlyVolatileAssetsLiveValue += liveHoldingValue

                liveHoldingValueList.append((cryptoName, liveHoldingValue))
                marketCapitalizationCategory = cryptoRecord[IDX_CAP]
                if marketCapitalizationCategory in marketCapLiveValueTotals:
                    marketCapLiveValueTotals[marketCapitalizationCategory] += liveHoldingValue

                print(f"{formatNumber(cryptoNumber):<8}{cryptoName:<18}{formatNumber(storedCurrentPrice):<14}{formatNumber(liveMarketPrice):<14}{deviationText:<16}{riskLabelText}")
            else:
                missingLiveDataCount += 1
                print(f"{formatNumber(cryptoNumber):<8}{cryptoName:<18}{formatNumber(storedCurrentPrice):<14}{'\033[90mN/A\033[0m':<23}{'\033[90mN/A\033[0m':<25}\033[90mNO LIVE DATA (N/A)\033[0m")

        print(SEPARATOR)

        validLiveDataCryptoCount = stableAssetCount + volatileAssetCount + highlyVolatileAssetCount

        print("\n\n" + SEPARATOR)
        print("Summary".center(len(SEPARATOR)))
        print(SEPARATOR)
        print(f"{'Cryptos Analysed (with Live Data)':<34}: {validLiveDataCryptoCount}")
        print(f"{f'Stable (≤{stableDeviationThresholdPercentage}%)':<34}: {stableAssetCount}")
        print(f"{f'Volatile ({stableDeviationThresholdPercentage}%–{volatileDeviationThresholdPercentage}%)':<34}: {volatileAssetCount}")
        print(f"{f'Highly volatile (>{volatileDeviationThresholdPercentage}%)':<34}: {highlyVolatileAssetCount}")
        if missingLiveDataCount > 0:
            print(f"\033[33m{'Note':<34}: {missingLiveDataCount} crypto(s) excluded (no live data)\033[0m")

        if totalLivePortfolioValue > 0:
            stableExposurePercentage = (stableAssetsLiveValue / totalLivePortfolioValue) * 100
            volatileExposurePercentage = (volatileAssetsLiveValue / totalLivePortfolioValue) * 100
            highlyVolatileExposurePercentage = (highlyVolatileAssetsLiveValue / totalLivePortfolioValue) * 100

            print(SEPARATOR)
            print(f"{'Stable exposure':<24} : {stableExposurePercentage:>6.2f}%")
            print(f"{'Volatile exposure':<24} : {volatileExposurePercentage:>6.2f}%")
            print(f"{'Highly volatile exposure':<24} : {highlyVolatileExposurePercentage:>6.2f}%")
            print(SEPARATOR)

            print("\n\n" + SEPARATOR)
            print("Business Interpretation (Decision Support)".center(len(SEPARATOR)))
            print(SEPARATOR)

            if highlyVolatileExposurePercentage >= 50:
                riskPostureText = "\033[31mVERY AGGRESSIVE\033[0m"
                riskPostureExplanation = "High exposure to swing assets; large day-to-day price movements expected."
            elif highlyVolatileExposurePercentage >= 30:
                riskPostureText = "\033[33mAGGRESSIVE\033[0m"
                riskPostureExplanation = "Portfolio is sensitive to sentiment; upside exists but drawdowns can be steep."
            elif highlyVolatileExposurePercentage >= 15:
                riskPostureText = "\033[33mMODERATE\033[0m"
                riskPostureExplanation = "Moderate volatility; regular monitoring advised."
            else:
                riskPostureText = "\033[32mMANAGED / CONSERVATIVE\033[0m"
                riskPostureExplanation = "Low high-volatility exposure; portfolio is relatively stable."

            print(f"1) Risk Posture : {riskPostureText}")
            print(f"   - {riskPostureExplanation}")

            liveHoldingValueList.sort(key=lambda x: x[1], reverse=True)
            if len(liveHoldingValueList) > 0:
                largestHoldingName, largestHoldingLiveValue = liveHoldingValueList[0]
                largestHoldingPercentage = (largestHoldingLiveValue / totalLivePortfolioValue) * 100

                topTwoHoldingsName, topTwoHoldingsPercentage = "", largestHoldingPercentage
                if len(liveHoldingValueList) > 1:
                    secondLargestHoldingName, secondLargestHoldingLiveValue = liveHoldingValueList[1]
                    topTwoHoldingsName = secondLargestHoldingName
                    topTwoHoldingsPercentage = ((largestHoldingLiveValue + secondLargestHoldingLiveValue) / totalLivePortfolioValue) * 100

                print("\n2) Concentration Risk")
                print(f"   - Largest holding : {largestHoldingName} ({largestHoldingPercentage:.2f}%)")
                if topTwoHoldingsName:
                    print(f"   - Top 2 holdings  : {largestHoldingName} + {topTwoHoldingsName} ({topTwoHoldingsPercentage:.2f}%)")

                if largestHoldingPercentage >= 60:
                    print("   - \033[31mHIGH concentration risk\033[0m (outcome depends heavily on one asset).")
                elif topTwoHoldingsPercentage >= 75:
                    print("   - \033[33mMODERATE concentration risk\033[0m (two assets drive most performance).")
                else:
                    print("   - \033[32mHealthier diversification\033[0m (single-asset shocks reduced).")

            highCapExposurePercentage = (marketCapLiveValueTotals["High"] / totalLivePortfolioValue) * 100
            midCapExposurePercentage = (marketCapLiveValueTotals["Mid"] / totalLivePortfolioValue) * 100
            lowCapExposurePercentage = (marketCapLiveValueTotals["Low"] / totalLivePortfolioValue) * 100

            print("\n3) Market Cap Mix")
            print(f"   - High-cap : {highCapExposurePercentage:.2f}%")
            print(f"   - Mid-cap  : {midCapExposurePercentage:.2f}%")
            print(f"   - Low-cap  : {lowCapExposurePercentage:.2f}%")

            if (midCapExposurePercentage + lowCapExposurePercentage) >= 60:
                print("   - \033[33mGrowth-focused\033[0m (higher upside, more vulnerable to downturns).")
            else:
                print("   - \033[32mStability-focused\033[0m (typically more resilient in volatility spikes).")

            print("\n4) Recommended Actions")
            recommendedActions = []
            if highlyVolatileExposurePercentage >= 40:
                recommendedActions.append("Rebalance: Reduce highly volatile exposure to stabilise portfolio swings.")
            if volatileExposurePercentage >= 50:
                recommendedActions.append("Monitoring: Set alerts and review volatile positions more frequently.")
            if len(liveHoldingValueList) > 0 and largestHoldingPercentage >= 60:
                recommendedActions.append("Diversify: Reduce reliance on one dominant holding to control concentration risk.")
            if (midCapExposurePercentage + lowCapExposurePercentage) >= 70:
                recommendedActions.append("Risk posture: Increase high-cap allocation to improve resilience during volatility spikes.")
            if not recommendedActions:
                recommendedActions.append("Maintain: Risk mix is balanced; continue monitoring and stay diversified.")

            for actionNumber, actionText in enumerate(recommendedActions, 1):
                print(f"   {actionNumber}. {actionText}")

        print(SEPARATOR)

        exitOption = input("Enter E to exit : ")
        if exitOption.upper() == "E":
            break

        os.system('cls')


def liveMarketScenarioSimulationMenu():
    while True:
        print(SEPARATOR)
        print("Live Market Scenario Simulation".center(len(SEPARATOR)))
        print(SEPARATOR)
        print("1. Bull Market (+10%)")
        print("2. Bear Market (-10%)")
        print("3. Market Crash (-30%)")
        print("4. Custom Scenario (Enter your own %)")
        print("E. Exit")
        print(SEPARATOR)

        scenarioMenuOption = input("Select an option: ").strip()

        if scenarioMenuOption.upper() == "E":
            break

        if scenarioMenuOption == "1":
            scenarioName = "Bull Market (+10%)"
            scenarioPercentageChange = 10
            os.system('cls')
            liveMarketScenarioSimulation(scenarioName, scenarioPercentageChange)

        elif scenarioMenuOption == "2":
            scenarioName = "Bear Market (-10%)"
            scenarioPercentageChange = -10
            os.system('cls')
            liveMarketScenarioSimulation(scenarioName, scenarioPercentageChange)

        elif scenarioMenuOption == "3":
            scenarioName = "Market Crash (-30%)"
            scenarioPercentageChange = -30
            os.system('cls')
            liveMarketScenarioSimulation(scenarioName, scenarioPercentageChange)

        elif scenarioMenuOption == "4":
            while True:
                try:
                    scenarioPercentageChange = float(input("Enter scenario % change : "))
                    scenarioName = f"Custom Scenario ({scenarioPercentageChange:+.2f}%)"
                    break
                except ValueError:
                    print("\033[31mError: Invalid input. Please enter a numeric percentage (e.g., 10, -10, 2.5).\033[0m\n")

            os.system('cls')
            liveMarketScenarioSimulation(scenarioName, scenarioPercentageChange)

        os.system('cls')


def liveMarketScenarioSimulation(scenarioName, scenarioPercentageChange):
    while True:
        scenarioMultiplier = 1 + (scenarioPercentageChange / 100)

        totalBaseLivePortfolioValue = 0
        totalSimulatedPortfolioValue = 0
        missingLiveDataCount = 0

        print(MID_LENGTH_SEPARATOR)
        print(f"Scenario: {scenarioName}".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)
        print(f"{'No':<8}{'Name':<19}{'Qty Bought':<18}{'Live Price':<18}{'Simulation Price':<22}{'Live Value':<18}{'Simulation Value':<24}{'Impact'}")
        print(MID_LENGTH_SEPARATOR)

        for cryptoRecord in cryptoPortfolioDatabase:
            cryptoNumber = cryptoRecord[IDX_NO]
            cryptoName = cryptoRecord[IDX_NAME]
            cryptoQuantityBought = cryptoRecord[IDX_QTY]
            liveMarketPrice = liveCryptoPrices.get(cryptoName)

            if isinstance(liveMarketPrice, (int, float)):
                baseLiveValue = cryptoQuantityBought * liveMarketPrice
                simulatedPrice = liveMarketPrice * scenarioMultiplier
                simulatedValue = cryptoQuantityBought * simulatedPrice

                valueImpact = simulatedValue - baseLiveValue
                impactText = f"{valueImpact:+.2f}"

                if valueImpact >= 0:
                    impactText = "\033[32m" + impactText + "\033[0m"
                else:
                    impactText = "\033[31m" + impactText + "\033[0m"

                totalBaseLivePortfolioValue += baseLiveValue
                totalSimulatedPortfolioValue += simulatedValue

                print(f"{formatNumber(cryptoNumber):<8}{cryptoName:<19}{formatNumber(cryptoQuantityBought):<18}{formatNumber(liveMarketPrice):<18}{formatNumber(simulatedPrice):<22}{formatNumber(baseLiveValue):<18}{formatNumber(simulatedValue):<24}{impactText}")
            else:
                missingLiveDataCount += 1
                print(f"{formatNumber(cryptoNumber):<8}{cryptoName:<19}{formatNumber(cryptoQuantityBought):<18}{'\033[90mN/A\033[0m':<27}{'\033[90mN/A\033[0m':<31}{'\033[90mN/A\033[0m':<27}{'\033[90mN/A\033[0m':<33}{'\033[90mNO LIVE DATA (N/A)\033[0m'}")

        print(MID_LENGTH_SEPARATOR)

        if totalBaseLivePortfolioValue > 0:
            portfolioValueImpact = totalSimulatedPortfolioValue - totalBaseLivePortfolioValue
            portfolioImpactPercentage = (portfolioValueImpact / totalBaseLivePortfolioValue) * 100

            portfolioImpactText = f"{portfolioValueImpact:+.2f} ({portfolioImpactPercentage:+.2f}%)"
            if portfolioValueImpact >= 0:
                portfolioImpactText = "\033[32m" + portfolioImpactText + "\033[0m"
            else:
                portfolioImpactText = "\033[31m" + portfolioImpactText + "\033[0m"

            print(f"{'TOTAL':<85}{formatNumber(totalBaseLivePortfolioValue):<18}{formatNumber(totalSimulatedPortfolioValue):<24}{portfolioImpactText}")
            print(MID_LENGTH_SEPARATOR)

        if missingLiveDataCount > 0:
            print(f"\033[33mNote: {missingLiveDataCount} crypto(s) had no live data and were excluded from the scenario TOTAL calculations.\033[0m\n")

        exitOption = input("Enter E to exit : ")
        if exitOption.upper() == "E":
            break

        os.system('cls')


def investmentRecommendation():
    while True:
        stableDeviationThresholdPercentage = 10
        volatileDeviationThresholdPercentage = 20

        highVolatilityExposureAlertPercentage = 40
        concentrationAlertPercentage = 60
        topTwoHoldingsAlertPercentage = 75
        midLowMarketCapAlertPercentage = 70
        strongGainAlertPercentage = 15
        bigLossAlertPercentage = -20

        totalInvestedValue = 0
        totalLivePortfolioValue = 0
        missingLiveDataCount = 0

        stableAssetsLiveValue = 0
        volatileAssetsLiveValue = 0
        highlyVolatileAssetsLiveValue = 0

        marketCapLiveValueTotals = {"High": 0, "Mid": 0, "Low": 0}

        liveHoldingValueList = []
        liveRoiMoversList = []

        print(MID_LENGTH_SEPARATOR)
        print("Investment Recommendation".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)

        for cryptoRecord in cryptoPortfolioDatabase:
            cryptoName = cryptoRecord[IDX_NAME]
            cryptoQuantityBought = cryptoRecord[IDX_QTY]
            cryptoBuyPrice = cryptoRecord[IDX_BUY]
            storedCurrentPrice = cryptoRecord[IDX_CURRENT]
            marketCapitalizationCategory = cryptoRecord[IDX_CAP]
            liveMarketPrice = liveCryptoPrices.get(cryptoName)

            investedValue = cryptoQuantityBought * cryptoBuyPrice

            if isinstance(liveMarketPrice, (int, float)) and investedValue != 0:
                liveValue = cryptoQuantityBought * liveMarketPrice
                liveProfitLossValue = liveValue - investedValue
                liveReturnOnInvestmentPercentage = (liveProfitLossValue / investedValue) * 100

                totalInvestedValue += investedValue
                totalLivePortfolioValue += liveValue

                if isinstance(storedCurrentPrice, (int, float)) and storedCurrentPrice != 0:
                    deviationPercentage = abs(liveMarketPrice - storedCurrentPrice) / storedCurrentPrice * 100
                else:
                    deviationPercentage = 0

                if deviationPercentage <= stableDeviationThresholdPercentage:
                    stableAssetsLiveValue += liveValue
                elif deviationPercentage <= volatileDeviationThresholdPercentage:
                    volatileAssetsLiveValue += liveValue
                else:
                    highlyVolatileAssetsLiveValue += liveValue

                if marketCapitalizationCategory in marketCapLiveValueTotals:
                    marketCapLiveValueTotals[marketCapitalizationCategory] += liveValue

                liveHoldingValueList.append((cryptoName, liveValue))
                liveRoiMoversList.append((cryptoName, liveReturnOnInvestmentPercentage, liveProfitLossValue, marketCapitalizationCategory))
            else:
                missingLiveDataCount += 1

        if totalLivePortfolioValue == 0 or totalInvestedValue == 0:
            print("\033[33mNo live data available to generate investment recommendations.\033[0m")
            if missingLiveDataCount > 0:
                print(f"\033[33mNote: {missingLiveDataCount} crypto(s) could not be analysed due to missing live data.\033[0m")
            print(MID_LENGTH_SEPARATOR)
            exitOption = input("Enter E to exit : ")
            if exitOption.upper() == "E":
                break
            os.system('cls')
            continue

        totalProfitLossValue = totalLivePortfolioValue - totalInvestedValue
        totalReturnOnInvestmentPercentage = (totalProfitLossValue / totalInvestedValue) * 100

        totalProfitLossText = f"{totalProfitLossValue:+.2f} ({totalReturnOnInvestmentPercentage:+.2f}%)"
        totalProfitLossText = (("\033[32m" + totalProfitLossText + "\033[0m") if totalProfitLossValue >= 0 else ("\033[31m" + totalProfitLossText + "\033[0m"))

        stableExposurePercentage = (stableAssetsLiveValue / totalLivePortfolioValue) * 100
        volatileExposurePercentage = (volatileAssetsLiveValue / totalLivePortfolioValue) * 100
        highlyVolatileExposurePercentage = (highlyVolatileAssetsLiveValue / totalLivePortfolioValue) * 100

        highCapExposurePercentage = (marketCapLiveValueTotals["High"] / totalLivePortfolioValue) * 100
        midCapExposurePercentage = (marketCapLiveValueTotals["Mid"] / totalLivePortfolioValue) * 100
        lowCapExposurePercentage = (marketCapLiveValueTotals["Low"] / totalLivePortfolioValue) * 100
        midLowCapExposurePercentage = midCapExposurePercentage + lowCapExposurePercentage

        liveHoldingValueList.sort(key=lambda x: x[1], reverse=True)
        largestHoldingName, largestHoldingLiveValue = liveHoldingValueList[0]
        largestHoldingPercentage = (largestHoldingLiveValue / totalLivePortfolioValue) * 100

        topTwoHoldingsPercentage = largestHoldingPercentage
        secondLargestHoldingName = ""
        if len(liveHoldingValueList) > 1:
            secondLargestHoldingName, secondLargestHoldingLiveValue = liveHoldingValueList[1]
            topTwoHoldingsPercentage = ((largestHoldingLiveValue + secondLargestHoldingLiveValue) / totalLivePortfolioValue) * 100

        liveRoiMoversList.sort(key=lambda x: x[1], reverse=True)

        gainersOnlyList = [m for m in liveRoiMoversList if m[1] > 0]
        losersOnlyList = [m for m in liveRoiMoversList if m[1] < 0]

        topGainersList = gainersOnlyList[:2]
        topLosersList = sorted(losersOnlyList, key=lambda x: x[1])[:2]

        print(f"{'Live Portfolio Value':<28}: {formatNumber(totalLivePortfolioValue)}")
        print(f"{'Total Invested Value':<28}: {formatNumber(totalInvestedValue)}")
        print(f"{'Unrealised P/L & ROI':<28}: {totalProfitLossText}")
        print(MID_LENGTH_SEPARATOR)

        if missingLiveDataCount > 0:
            print(f"\033[33mNote: {missingLiveDataCount} crypto(s) were excluded from analysis due to missing live data.\033[0m")
            print(MID_LENGTH_SEPARATOR)

        print("\n\n" + MID_LENGTH_SEPARATOR)
        print("Risk & Allocation Snapshot".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)
        print(f"{'Stable exposure':<28}: {stableExposurePercentage:>.2f}%")
        print(f"{'Volatile exposure':<28}: {volatileExposurePercentage:>.2f}%")
        print(f"{'Highly volatile exposure':<28}: {highlyVolatileExposurePercentage:>.2f}%")
        print(MID_LENGTH_SEPARATOR)
        print(f"{'High-cap exposure':<28}: {highCapExposurePercentage:>.2f}%")
        print(f"{'Mid-cap exposure':<28}: {midCapExposurePercentage:>.2f}%")
        print(f"{'Low-cap exposure':<28}: {lowCapExposurePercentage:>.2f}%")
        print(MID_LENGTH_SEPARATOR)
        print(f"{'Largest holding':<28}: {largestHoldingName} ({largestHoldingPercentage:.2f}%)")
        if secondLargestHoldingName:
            print(f"{'Top 2 holdings':<28}: {largestHoldingName} + {secondLargestHoldingName} ({topTwoHoldingsPercentage:.2f}%)")
        print(MID_LENGTH_SEPARATOR)

        print("\n\n" + MID_LENGTH_SEPARATOR)
        print("Top Movers (Live ROI)".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)

        print("\033[32mTop Gainers\033[0m")
        if len(topGainersList) == 0:
            print("- None (no profitable assets)")
        else:
            for cryptoName, roiPercentage, liveProfitLossValue, marketCapitalizationCategory in topGainersList:
                roiText = f"{roiPercentage:+.2f}%"
                profitLossText = f"({liveProfitLossValue:+.2f})"
                print(f"- {cryptoName:<14} {roiText:<10} {profitLossText:<14} [{marketCapitalizationCategory}]")

        print("\n\033[31mTop Losers\033[0m")
        if len(topLosersList) == 0:
            print("- None (no losing assets)")
        else:
            for cryptoName, roiPercentage, liveProfitLossValue, marketCapitalizationCategory in topLosersList:
                roiText = f"{roiPercentage:+.2f}%"
                profitLossText = f"({liveProfitLossValue:+.2f})"
                print(f"- {cryptoName:<14} {roiText:<10} {profitLossText:<14} [{marketCapitalizationCategory}]")

        print(MID_LENGTH_SEPARATOR)

        print("\n\n" + MID_LENGTH_SEPARATOR)
        print("Recommendation Summary".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)

        recommendationList = []
        recommendationReasonList = []

        if totalReturnOnInvestmentPercentage >= strongGainAlertPercentage:
            recommendationList.append("Profit discipline: Consider taking partial profits on your strongest gainers.")
            recommendationReasonList.append(f"Portfolio ROI is strong ({totalReturnOnInvestmentPercentage:+.2f}%); locking in gains helps reduce reversal risk.")
        elif totalReturnOnInvestmentPercentage <= bigLossAlertPercentage:
            recommendationList.append("Defensive posture: Reduce exposure to highly volatile assets and review your allocation.")
            recommendationReasonList.append(f"Portfolio drawdown is significant ({totalReturnOnInvestmentPercentage:+.2f}%); risk control should be the priority.")
        else:
            recommendationList.append("Hold & monitor: Maintain positions, but keep risk checks and reviews active.")
            recommendationReasonList.append(f"Portfolio ROI is moderate ({totalReturnOnInvestmentPercentage:+.2f}%); focus on risk control and diversification.")

        if highlyVolatileExposurePercentage >= highVolatilityExposureAlertPercentage:
            recommendationList.append("Risk reduction: Rebalance to reduce highly volatile exposure.")
            recommendationReasonList.append(f"Highly volatile exposure is high ({highlyVolatileExposurePercentage:.2f}%); portfolio value may experience sharp swings.")

        if largestHoldingPercentage >= concentrationAlertPercentage:
            recommendationList.append("Diversification: Reduce reliance on the largest holding to manage concentration risk.")
            recommendationReasonList.append(f"{largestHoldingName} dominates ({largestHoldingPercentage:.2f}%); a single-asset shock could heavily impact overall performance.")
        elif topTwoHoldingsPercentage >= topTwoHoldingsAlertPercentage:
            recommendationList.append("Diversification: Spread allocation across more assets to reduce dependency on top holdings.")
            recommendationReasonList.append(f"Top 2 holdings dominate ({topTwoHoldingsPercentage:.2f}%); overall performance depends heavily on them.")

        if midLowCapExposurePercentage >= midLowMarketCapAlertPercentage:
            recommendationList.append("Stability shift: Consider increasing high-cap allocation to improve portfolio resilience.")
            recommendationReasonList.append(f"Mid/Low-cap exposure is high ({midLowCapExposurePercentage:.2f}%); these assets typically carry higher risk and volatility.")

        recommendationList.append("Action focus: Review top losers for risk control, and apply profit rules to top gainers.")
        recommendationReasonList.append("Prioritise the biggest movers to manage downside risk and lock in gains systematically.")

        seenRecommendations = set()
        finalRecommendationList = []
        for recommendationText in recommendationList:
            if recommendationText not in seenRecommendations:
                finalRecommendationList.append(recommendationText)
                seenRecommendations.add(recommendationText)

        for recommendationNumber, recommendationText in enumerate(finalRecommendationList, 1):
            print(f"{recommendationNumber}. {recommendationText}")

        print(MID_LENGTH_SEPARATOR)
        print("Why these recommendations?".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)
        for reasonText in recommendationReasonList[:6]:
            print(f"- {reasonText}")

        print(MID_LENGTH_SEPARATOR)
        exitOption = input("Enter E to exit : ")
        if exitOption.upper() == "E":
            break

        os.system('cls')


def functionSeven():
    return


def launchApplication():
    os.system('cls')

    while True:
        selectedMainMenuOption = mainMenu()

        if selectedMainMenuOption == "1":
            os.system('cls')
            displayCrypto()
            os.system('cls')

        elif selectedMainMenuOption == "2":
            os.system('cls')
            addCrypto()
            os.system('cls')

        elif selectedMainMenuOption == "3":
            os.system('cls')
            amendCrypto()
            os.system('cls')

        elif selectedMainMenuOption == "4":
            os.system('cls')
            removeCrypto()
            os.system('cls')

        elif selectedMainMenuOption == "5":
            os.system('cls')
            cryptoPortfolioStatement()
            os.system('cls')

        elif selectedMainMenuOption == "6":
            os.system('cls')

            while True:
                selectedBusinessAnalysisMenuOption = portfolioBusinessAnalysisMenu()

                if selectedBusinessAnalysisMenuOption == "1":
                    os.system('cls')
                    fetchLivePrices()
                    livePriceComparison()
                    os.system('cls')

                elif selectedBusinessAnalysisMenuOption == "2":
                    os.system('cls')
                    fetchLivePrices()
                    realTimePortfolioReport()
                    os.system('cls')

                elif selectedBusinessAnalysisMenuOption == "3":
                    os.system('cls')
                    fetchLivePrices()
                    marketVolatilityRiskAnalysis()
                    os.system('cls')

                elif selectedBusinessAnalysisMenuOption == "4":
                    os.system('cls')
                    fetchLivePrices()
                    liveMarketScenarioSimulationMenu()
                    os.system('cls')

                elif selectedBusinessAnalysisMenuOption == "5":
                    os.system('cls')
                    fetchLivePrices()
                    investmentRecommendation()
                    os.system('cls')

                elif selectedBusinessAnalysisMenuOption.upper() == "E":
                    os.system('cls')
                    break

                else:
                    os.system('cls')

        elif selectedMainMenuOption == "7":
            os.system('cls')
            functionSeven()
            os.system('cls')

        elif selectedMainMenuOption.upper() == "E":
            os.system('cls')
            break

        else:
            os.system('cls')


launchApplication()