import os
import time
import requests

COIN_GECKO_DEMO_API_KEY = "CG-HcdtNTwkUzhnzNP9yKCcRmWH"

SEPARATOR = "-" * 88
MID_LENGTH_SEPARATOR = "-" * 149
LONG_SEPARATOR = "-" * 174

IDX_NO = 0
IDX_NAME = 1
IDX_CAP = 2
IDX_QTY = 3
IDX_BUY = 4
IDX_CURRENT = 5

player_money = 1000
streak = 0

crypto_portfolio_database = [
    [1, "Bitcoin", "High", 15, 38000, 62000],
    [2, "Ethereum", "High", 90, 4200, 3500],
    [3, "Solana", "Mid", 60, 260, 110],
    [4, "Decentraland", "Mid", 30000, 1.5, 5],
    [5, "The Sandbox", "Mid", 25000, 2, 4],
    [6, "Dogecoin", "Low", 55000, 0.4, 0.15]
]

live_crypto_prices = {}


def main_menu():
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
    print("7. Crypto Trading Game")
    print("E. Exit Main Menu")
    print(SEPARATOR)
    return input("Select an option: ")


def format_number(number):
    if number == int(number):
        return str(int(number))
    else:
        return f"{number:.2f}"


def display_crypto():
    while True:
        print(SEPARATOR)
        print("Display Cryptocurrency".center(len(SEPARATOR)))
        print(SEPARATOR)
        print(f"{'No':<7}{'Name':<17}{'Capitalization':<19}{'Qty Bought':<15}{'Bought Price':<17}{'Current Price'}")
        print(SEPARATOR)

        for crypto_record in crypto_portfolio_database:
            print(f"{format_number(crypto_record[IDX_NO]):<7}{crypto_record[IDX_NAME]:<17}{crypto_record[IDX_CAP]:<19}{format_number(crypto_record[IDX_QTY]):<15}{format_number(crypto_record[IDX_BUY]):<17}{format_number(crypto_record[IDX_CURRENT])}")

        print(SEPARATOR)
        exit_option = input("Enter E to exit : ")

        if exit_option.upper() == "E":
            break

        os.system('cls')


def add_crypto():
    print(SEPARATOR)
    print("Add Cryptocurrency".center(len(SEPARATOR)))
    print(SEPARATOR)
    new_crypto_number = len(crypto_portfolio_database) + 1

    while True:
        new_crypto_name = input("Enter Cryptocurrency Name : ").strip()

        is_duplicate_crypto_name = False
        for crypto_record in crypto_portfolio_database:
            if crypto_record[IDX_NAME].lower() == new_crypto_name.lower():
                is_duplicate_crypto_name = True
                break

        if is_duplicate_crypto_name:
            print("\033[31mError: This cryptocurrency already exists in your portfolio database.\033[0m\n")
        elif new_crypto_name == "":
            print("\033[31mError: Cryptocurrency name cannot be blank. Please enter a valid name.\033[0m\n")
        else:
            break

    print()

    while True:
        new_crypto_market_capitalization = input("Enter Market Cap of Crypto: High, Mid, Low : ")
        if (new_crypto_market_capitalization.title() == "High" or new_crypto_market_capitalization.title() == "Mid" or new_crypto_market_capitalization.title() == "Low"):
            new_crypto_market_capitalization = new_crypto_market_capitalization.title()
            break
        else:
            print("\033[31mError: Invalid Narket Cap. Please enter High, Mid, or Low.\033[0m\n")

    print()

    while True:
        try:
            new_crypto_quantity_bought = float(input("Enter Quantity of Crypto Bought = "))
            break
        except ValueError:
            print("\033[31mError: Invalid input. Please enter a numeric value (e.g., 12 or 12.5).\033[0m\n")

    print()

    while True:
        try:
            new_crypto_bought_price = float(input("Enter Buy In Price of Crypto = "))
            break
        except ValueError:
            print("\033[31mError: Invalid input. Please enter a numeric value (e.g., 12 or 12.5).\033[0m\n")

    print()

    while True:
        try:
            new_crypto_current_market_price = float(input("Enter Market Price of Crypto = "))
            break
        except ValueError:
            print("\033[31mError: Invalid input. Please enter a numeric value (e.g., 12 or 12.5).\033[0m\n")

    print(SEPARATOR)

    new_crypto_record = [
        new_crypto_number,
        new_crypto_name,
        new_crypto_market_capitalization,
        new_crypto_quantity_bought,
        new_crypto_bought_price,
        new_crypto_current_market_price
    ]
    crypto_portfolio_database.append(new_crypto_record)


def amend_crypto():
    should_exit_amend_loops = False

    print(SEPARATOR)
    print("Amend Cryptocurrency".center(len(SEPARATOR)))
    print(SEPARATOR)
    print("No - Cryptocurrency")
    print(SEPARATOR)

    for crypto_record in crypto_portfolio_database:
        print(f"{crypto_record[IDX_NO] - 1} - {crypto_record[IDX_NAME]}")

    print(SEPARATOR)

    while True:
        selected_crypto_index_to_amend = input(f"Enter 0 to {len(crypto_portfolio_database) - 1} for your selection or E to exit : ")

        if selected_crypto_index_to_amend.upper() == "E":
            break

        elif selected_crypto_index_to_amend.isdigit():
            if (int(selected_crypto_index_to_amend) >= 0 and int(selected_crypto_index_to_amend) <= (len(crypto_portfolio_database) - 1)):
                while True:
                    os.system('cls')
                    print(SEPARATOR)
                    print("Amend Cryptocurrency".center(len(SEPARATOR)))
                    print(SEPARATOR)
                    print(f"Index                       : {selected_crypto_index_to_amend}")
                    print(f"1. Name                     : {crypto_portfolio_database[int(selected_crypto_index_to_amend)][IDX_NAME]}")
                    print(f"2. Market Cap               : {crypto_portfolio_database[int(selected_crypto_index_to_amend)][IDX_CAP]}")
                    print(f"3. Quantity Bought          : {crypto_portfolio_database[int(selected_crypto_index_to_amend)][IDX_QTY]}")
                    print(f"4. Buy In Price             : {crypto_portfolio_database[int(selected_crypto_index_to_amend)][IDX_BUY]}")
                    print(f"5. Market Price             : {crypto_portfolio_database[int(selected_crypto_index_to_amend)][IDX_CURRENT]}")
                    print(f"E. Edit Completed. Exit")
                    print(SEPARATOR)

                    while True:
                        selected_field_to_edit = input("What do you want to edit : ")

                        if selected_field_to_edit == "1":
                            print()

                            while True:
                                updated_crypto_name = input(f"({selected_field_to_edit}) Enter new Cryptocurrency Name : ").strip()

                                is_duplicate_crypto_name = False
                                for crypto_record in crypto_portfolio_database:
                                    if crypto_record[IDX_NAME].lower() == updated_crypto_name.lower():
                                        is_duplicate_crypto_name = True
                                        break

                                if is_duplicate_crypto_name:
                                    print("\033[31mError: This cryptocurrency already exists in your portfolio database.\033[0m\n")
                                elif updated_crypto_name == "":
                                    print("\033[31mError: Cryptocurrency name cannot be blank. Please enter a valid name.\033[0m\n")
                                else:
                                    crypto_portfolio_database[int(selected_crypto_index_to_amend)][IDX_NAME] = updated_crypto_name
                                    break

                            break

                        elif selected_field_to_edit == "2":
                            print()

                            while True:
                                updated_market_capitalization = input(f"({selected_field_to_edit}) Enter new Market Cap of Crypto: High, Mid, Low : ")
                                if (updated_market_capitalization.title() == "High" or updated_market_capitalization.title() == "Mid" or updated_market_capitalization.title() == "Low"):
                                    crypto_portfolio_database[int(selected_crypto_index_to_amend)][IDX_CAP] = updated_market_capitalization.title()
                                    break
                                else:
                                    print("\033[31mError: Invalid Narket Cap. Please enter High, Mid, or Low.\033[0m\n")

                            break

                        elif selected_field_to_edit == "3":
                            print()

                            while True:
                                try:
                                    crypto_portfolio_database[int(selected_crypto_index_to_amend)][IDX_QTY] = float(input(f"({selected_field_to_edit}) Enter new Quantity of Crypto Bought = "))
                                    break
                                except ValueError:
                                    print("\033[31mError: Invalid input. Please enter a numeric value (e.g., 12 or 12.5).\033[0m\n")

                            break

                        elif selected_field_to_edit == "4":
                            print()

                            while True:
                                try:
                                    crypto_portfolio_database[int(selected_crypto_index_to_amend)][IDX_BUY] = float(input(f"({selected_field_to_edit}) Enter new Buy In Price of Crypto = "))
                                    break
                                except ValueError:
                                    print("\033[31mError: Invalid input. Please enter a numeric value (e.g., 12 or 12.5).\033[0m\n")

                            break

                        elif selected_field_to_edit == "5":
                            print()

                            while True:
                                try:
                                    crypto_portfolio_database[int(selected_crypto_index_to_amend)][IDX_CURRENT] = float(input(f"({selected_field_to_edit}) Enter new Market Price of Crypto = "))
                                    break
                                except ValueError:
                                    print("\033[31mError: Invalid input. Please enter a numeric value (e.g., 12 or 12.5).\033[0m\n")

                            break

                        elif selected_field_to_edit.upper() == "E":
                            should_exit_amend_loops = True
                            break

                        else:
                            print("\033[31mError: Invalid selection. Please try again.\033[0m\n")

                    if should_exit_amend_loops:
                        break

            else:
                print("\033[31mError: Invalid selection. Please try again.\033[0m\n")

        else:
            print("\033[31mError: Invalid selection. Please try again.\033[0m\n")

        if should_exit_amend_loops:
            break


def remove_crypto():
    print(SEPARATOR)
    print("Remove Cryptocurrency".center(len(SEPARATOR)))
    print(SEPARATOR)
    print("No - Cryptocurrency")
    print(SEPARATOR)

    for crypto_record in crypto_portfolio_database:
        print(f"{crypto_record[IDX_NO] - 1} - {crypto_record[IDX_NAME]}")

    print(SEPARATOR)

    while True:
        selected_crypto_index_to_remove = input(f"Enter 0 to {len(crypto_portfolio_database) - 1} for your selection or E to exit : ")

        if selected_crypto_index_to_remove.upper() == "E":
            break

        elif selected_crypto_index_to_remove.isdigit():
            if (int(selected_crypto_index_to_remove) >= 0 and int(selected_crypto_index_to_remove) <= (len(crypto_portfolio_database) - 1)):
                crypto_portfolio_database.pop(int(selected_crypto_index_to_remove))

                next_crypto_number = 1
                for crypto_record in crypto_portfolio_database:
                    crypto_record[IDX_NO] = next_crypto_number
                    next_crypto_number += 1

                break
            else:
                print("\033[31mError: Invalid selection. Please try again.\033[0m\n")

        else:
            print("\033[31mError: Invalid selection. Please try again.\033[0m\n")


def crypto_portfolio_statement():
    while True:
        total_invested_value = 0
        total_current_portfolio_value = 0

        for crypto_record in crypto_portfolio_database:
            total_invested_value += crypto_record[IDX_QTY] * crypto_record[IDX_BUY]
            total_current_portfolio_value += crypto_record[IDX_QTY] * crypto_record[IDX_CURRENT]

        print(LONG_SEPARATOR)
        print("Crypto Portfolio Statement".center(len(LONG_SEPARATOR)))
        print(LONG_SEPARATOR)
        print(f"{'No':<6}{'Name':<16}{'Qty Bought':<14}{'Bought Price':<16}{'Current Price':<17}{'Total Invested':<18}{'Invested Portfolio Size':<27}{'Total Current Value':<23}{'Profit/Loss':<15}{'Current Portfolio Size'}")
        print(LONG_SEPARATOR)

        for crypto_record in crypto_portfolio_database:
            crypto_quantity_bought = crypto_record[IDX_QTY]
            crypto_bought_price = crypto_record[IDX_BUY]
            crypto_current_price = crypto_record[IDX_CURRENT]

            crypto_total_invested_value = crypto_quantity_bought * crypto_bought_price
            crypto_invested_portfolio_percentage = (crypto_total_invested_value / total_invested_value) * 100

            crypto_total_current_value = crypto_quantity_bought * crypto_current_price

            crypto_profit_loss_value = crypto_total_current_value - crypto_total_invested_value
            crypto_profit_loss_formatted = format_number(crypto_profit_loss_value)

            if crypto_profit_loss_value >= 0:
                crypto_profit_loss_text = f"\033[32m{crypto_profit_loss_formatted:<15}\033[0m"
            else:
                crypto_profit_loss_text = f"\033[31m{crypto_profit_loss_formatted:<15}\033[0m"

            crypto_current_portfolio_percentage = (crypto_total_current_value / total_current_portfolio_value) * 100

            print(f"{crypto_record[IDX_NO]:<6}{crypto_record[IDX_NAME]:<16}{crypto_quantity_bought:<14}{format_number(crypto_bought_price):<16}{format_number(crypto_current_price):<17}{format_number(crypto_total_invested_value):<18}{format_number(crypto_invested_portfolio_percentage) + '%':<27}{format_number(crypto_total_current_value):<23}{crypto_profit_loss_text}{format_number(crypto_current_portfolio_percentage) + '%'}")

        overall_profit_loss_value = total_current_portfolio_value - total_invested_value

        if overall_profit_loss_value >= 0:
            overall_profit_loss_text = f"\033[32m{format_number(overall_profit_loss_value)}\033[0m"
        else:
            overall_profit_loss_text = f"\033[31m{format_number(overall_profit_loss_value)}\033[0m"

        print(LONG_SEPARATOR)
        print(f"{'SUM':<69}{format_number(total_invested_value):<45}{format_number(total_current_portfolio_value):<23}{overall_profit_loss_text}")
        print(LONG_SEPARATOR)

        exit_option = input("Enter E to exit : ")

        if exit_option.upper() == "E":
            break

        os.system('cls')


def portfolio_business_analysis_menu():
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


def fetch_live_prices():
    global COIN_GECKO_DEMO_API_KEY, live_crypto_prices
    live_crypto_prices = {}

    print("\nRetrieving live crypto prices...\n")

    for crypto_record in crypto_portfolio_database:
        crypto_name = crypto_record[IDX_NAME]

        coin_gecko_crypto_id = crypto_name.lower().replace(" ", "-")

        coin_gecko_api_url = f"https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd&ids={coin_gecko_crypto_id}&x_cg_demo_api_key={COIN_GECKO_DEMO_API_KEY}"

        try:
            api_response = requests.get(coin_gecko_api_url, timeout=5)
            api_response_data = api_response.json()

            if coin_gecko_crypto_id in api_response_data and "usd" in api_response_data[coin_gecko_crypto_id]:
                live_market_price_usd = api_response_data[coin_gecko_crypto_id]["usd"]
                live_crypto_prices[crypto_name] = live_market_price_usd
            else:
                live_crypto_prices[crypto_name] = "\033[90mNO LIVE DATA (N/A)\033[0m"

        except Exception as e:
            live_crypto_prices[crypto_name] = "LIVE DATA ERROR (CoinGecko API)"

    os.system('cls')


def live_price_comparison():
    while True:
        print(SEPARATOR)
        print("Live Price Comparison".center(len(SEPARATOR)))
        print(SEPARATOR)
        print(f"{'No':<10}{'Name':<20}{'Stored Price':<21}{'Live Price':<18}{'Change'}")
        print(SEPARATOR)

        for crypto_record in crypto_portfolio_database:
            crypto_number = crypto_record[IDX_NO]
            crypto_name = crypto_record[IDX_NAME]
            stored_current_price = crypto_record[IDX_CURRENT]
            live_market_price = live_crypto_prices.get(crypto_name)

            if isinstance(live_market_price, (int, float)):
                price_difference = live_market_price - stored_current_price

                if stored_current_price != 0:
                    price_difference_percentage = (price_difference / stored_current_price) * 100
                else:
                    price_difference_percentage = 0

                price_change_text = f"{price_difference:+.2f} ({price_difference_percentage:+.2f}%)"

                if price_difference >= 0:
                    price_change_text = "\033[32m" + price_change_text + "\033[0m"
                else:
                    price_change_text = "\033[31m" + price_change_text + "\033[0m"

                print(f"{format_number(crypto_number):<10}{crypto_name:<20}{format_number(stored_current_price):<21}{format_number(live_market_price):<18}{price_change_text}")

            else:
                print(f"{format_number(crypto_number):<10}{crypto_name:<20}{format_number(stored_current_price):<21}{'\033[90mN/A\033[0m':<27}{live_market_price}")

        print(SEPARATOR)

        should_update_stored_prices = input("Update stored prices with live data? (Y/N): ")

        if should_update_stored_prices.upper() == "Y":
            for crypto_record in crypto_portfolio_database:
                crypto_name = crypto_record[IDX_NAME]
                live_market_price = live_crypto_prices.get(crypto_name)

                if isinstance(live_market_price, (int, float)):
                    crypto_record[IDX_CURRENT] = live_market_price

            print("\033[33mUpdate complete: Stored prices have been refreshed using live market data.\033[0m")
            input("\nPress enter to exit ")
            os.system('cls')
            break

        elif should_update_stored_prices.upper() == "N":
            print("\033[33mNo update performed: Stored prices remain unchanged.\033[0m")
            input("\nPress enter to exit ")
            os.system('cls')
            break

        os.system('cls')


def real_time_portfolio_report():
    while True:
        total_invested_value = 0
        total_live_portfolio_value = 0
        missing_live_data_count = 0

        print(MID_LENGTH_SEPARATOR)
        print("Real Time Portfolio Report".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)
        print(f"{'No':<10}{'Name':<20}{'Qty Bought':<17}{'Buy Price':<17}{'Total Invested':<22}{'Live Price':<18}{'Total Live Value':<24}{'Profit/Loss'}")
        print(MID_LENGTH_SEPARATOR)

        for crypto_record in crypto_portfolio_database:
            crypto_number = crypto_record[IDX_NO]
            crypto_name = crypto_record[IDX_NAME]
            crypto_quantity_bought = crypto_record[IDX_QTY]
            crypto_buy_price = crypto_record[IDX_BUY]
            live_market_price = live_crypto_prices.get(crypto_name)

            invested_value = crypto_quantity_bought * crypto_buy_price

            if isinstance(live_market_price, (int, float)):
                live_value = crypto_quantity_bought * live_market_price
                live_profit_loss_value = live_value - invested_value
                live_return_on_investment_percentage = (live_profit_loss_value / invested_value) * 100 if invested_value != 0 else 0

                total_invested_value += invested_value
                total_live_portfolio_value += live_value

                live_performance_text = f"{live_profit_loss_value:+.2f} ({live_return_on_investment_percentage:+.2f}%)"
                live_performance_text = ("\033[32m" + live_performance_text + "\033[0m" if live_profit_loss_value >= 0 else "\033[31m" + live_performance_text + "\033[0m")

                print(f"{format_number(crypto_number):<10}{crypto_name:<20}{format_number(crypto_quantity_bought):<17}{format_number(crypto_buy_price):<17}{format_number(invested_value):<22}{format_number(live_market_price):<18}{format_number(live_value):<24}{live_performance_text}")

            else:
                missing_live_data_count += 1
                print(f"{format_number(crypto_number):<10}{crypto_name:<20}{format_number(crypto_quantity_bought):<17}{format_number(crypto_buy_price):<17}{format_number(invested_value):<22}{'\033[90mN/A\033[0m':<27}{'\033[90mN/A\033[0m':<33}{'\033[90mNO LIVE DATA (N/A)\033[0m'}")

        print(MID_LENGTH_SEPARATOR)

        total_profit_loss_value = total_live_portfolio_value - total_invested_value
        total_return_on_investment_percentage = (total_profit_loss_value / total_invested_value) * 100 if total_invested_value != 0 else 0

        total_performance_text = f"{total_profit_loss_value:+.2f} ({total_return_on_investment_percentage:+.2f}%)"
        total_performance_text = ("\033[32m" + total_performance_text + "\033[0m" if total_profit_loss_value >= 0 else "\033[31m" + total_performance_text + "\033[0m")

        print(f"{'TOTAL':<64}{format_number(total_invested_value):<18}{'':<22}{format_number(total_live_portfolio_value):<24}{total_performance_text}")
        print(MID_LENGTH_SEPARATOR)

        if missing_live_data_count > 0:
            print(f"\033[33mNote: {missing_live_data_count} crypto(s) had no live data and were excluded from the TOTAL calculations.\033[0m\n")

        exit_option = input("Enter E to exit : ")
        if exit_option.upper() == "E":
            break

        os.system('cls')


def market_volatility_risk_analysis():
    while True:
        stable_deviation_threshold_percentage = 10
        volatile_deviation_threshold_percentage = 20

        stable_asset_count = 0
        volatile_asset_count = 0
        highly_volatile_asset_count = 0
        missing_live_data_count = 0

        total_live_portfolio_value = 0
        stable_assets_live_value = 0
        highly_volatile_assets_live_value = 0
        volatile_assets_live_value = 0

        live_holding_value_list = []
        market_cap_live_value_totals = {"High": 0, "Mid": 0, "Low": 0}

        print(SEPARATOR)
        print("Market Volatility Risk Analysis".center(len(SEPARATOR)))
        print(SEPARATOR)
        print(f"{'No':<8}{'Name':<18}{'Stored':<14}{'Live':<14}{'Deviation':<16}{'Risk Level'}")
        print(SEPARATOR)

        for crypto_record in crypto_portfolio_database:
            crypto_number = crypto_record[IDX_NO]
            crypto_name = crypto_record[IDX_NAME]
            stored_current_price = crypto_record[IDX_CURRENT]
            live_market_price = live_crypto_prices.get(crypto_name)

            if (isinstance(live_market_price, (int, float)) and isinstance(stored_current_price, (int, float)) and stored_current_price != 0):
                deviation_percentage = abs(live_market_price - stored_current_price) / stored_current_price * 100

                if deviation_percentage <= stable_deviation_threshold_percentage:
                    risk_label = "STABLE"
                    stable_asset_count += 1
                    risk_label_text = f"\033[32m{risk_label}\033[0m"
                elif deviation_percentage <= volatile_deviation_threshold_percentage:
                    risk_label = "VOLATILE"
                    volatile_asset_count += 1
                    risk_label_text = f"\033[33m{risk_label}\033[0m"
                else:
                    risk_label = "HIGHLY VOLATILE"
                    highly_volatile_asset_count += 1
                    risk_label_text = f"\033[31m{risk_label} ⚠\033[0m"

                deviation_text = f"{deviation_percentage:.2f}%"

                live_holding_value = crypto_record[IDX_QTY] * live_market_price
                total_live_portfolio_value += live_holding_value

                if risk_label == "STABLE":
                    stable_assets_live_value += live_holding_value
                elif risk_label == "VOLATILE":
                    volatile_assets_live_value += live_holding_value
                else:
                    highly_volatile_assets_live_value += live_holding_value

                live_holding_value_list.append((crypto_name, live_holding_value))
                market_capitalization_category = crypto_record[IDX_CAP]
                if market_capitalization_category in market_cap_live_value_totals:
                    market_cap_live_value_totals[market_capitalization_category] += live_holding_value

                print(f"{format_number(crypto_number):<8}{crypto_name:<18}{format_number(stored_current_price):<14}{format_number(live_market_price):<14}{deviation_text:<16}{risk_label_text}")
            else:
                missing_live_data_count += 1
                print(f"{format_number(crypto_number):<8}{crypto_name:<18}{format_number(stored_current_price):<14}{'\033[90mN/A\033[0m':<23}{'\033[90mN/A\033[0m':<25}\033[90mNO LIVE DATA (N/A)\033[0m")

        print(SEPARATOR)

        valid_live_data_crypto_count = stable_asset_count + volatile_asset_count + highly_volatile_asset_count

        print("\n\n" + SEPARATOR)
        print("Summary".center(len(SEPARATOR)))
        print(SEPARATOR)
        print(f"{'Cryptos Analysed (with Live Data)':<34}: {valid_live_data_crypto_count}")
        print(f"{f'Stable (≤{stable_deviation_threshold_percentage}%)':<34}: {stable_asset_count}")
        print(f"{f'Volatile ({stable_deviation_threshold_percentage}%–{volatile_deviation_threshold_percentage}%)':<34}: {volatile_asset_count}")
        print(f"{f'Highly volatile (>{volatile_deviation_threshold_percentage}%)':<34}: {highly_volatile_asset_count}")
        if missing_live_data_count > 0:
            print(f"\033[33m{'Note':<34}: {missing_live_data_count} crypto(s) excluded (no live data)\033[0m")

        if total_live_portfolio_value > 0:
            stable_exposure_percentage = (stable_assets_live_value / total_live_portfolio_value) * 100
            volatile_exposure_percentage = (volatile_assets_live_value / total_live_portfolio_value) * 100
            highly_volatile_exposure_percentage = (highly_volatile_assets_live_value / total_live_portfolio_value) * 100

            print(SEPARATOR)
            print(f"{'Stable exposure':<24} : {stable_exposure_percentage:>6.2f}%")
            print(f"{'Volatile exposure':<24} : {volatile_exposure_percentage:>6.2f}%")
            print(f"{'Highly volatile exposure':<24} : {highly_volatile_exposure_percentage:>6.2f}%")
            print(SEPARATOR)

            print("\n\n" + SEPARATOR)
            print("Business Interpretation (Decision Support)".center(len(SEPARATOR)))
            print(SEPARATOR)

            if highly_volatile_exposure_percentage >= 50:
                risk_posture_text = "\033[31mVERY AGGRESSIVE\033[0m"
                risk_posture_explanation = "High exposure to swing assets; large day-to-day price movements expected."
            elif highly_volatile_exposure_percentage >= 30:
                risk_posture_text = "\033[33mAGGRESSIVE\033[0m"
                risk_posture_explanation = "Portfolio is sensitive to sentiment; upside exists but drawdowns can be steep."
            elif highly_volatile_exposure_percentage >= 15:
                risk_posture_text = "\033[33mMODERATE\033[0m"
                risk_posture_explanation = "Moderate volatility; regular monitoring advised."
            else:
                risk_posture_text = "\033[32mMANAGED / CONSERVATIVE\033[0m"
                risk_posture_explanation = "Low high-volatility exposure; portfolio is relatively stable."

            print(f"1) Risk Posture : {risk_posture_text}")
            print(f"   - {risk_posture_explanation}")

            live_holding_value_list.sort(key=lambda x: x[1], reverse=True)
            if len(live_holding_value_list) > 0:
                largest_holding_name, largest_holding_live_value = live_holding_value_list[0]
                largest_holding_percentage = (largest_holding_live_value / total_live_portfolio_value) * 100

                top_two_holdings_name, top_two_holdings_percentage = "", largest_holding_percentage
                if len(live_holding_value_list) > 1:
                    second_largest_holding_name, second_largest_holding_live_value = live_holding_value_list[1]
                    top_two_holdings_name = second_largest_holding_name
                    top_two_holdings_percentage = ((largest_holding_live_value + second_largest_holding_live_value) / total_live_portfolio_value) * 100

                print("\n2) Concentration Risk")
                print(f"   - Largest holding : {largest_holding_name} ({largest_holding_percentage:.2f}%)")
                if top_two_holdings_name:
                    print(f"   - Top 2 holdings  : {largest_holding_name} + {top_two_holdings_name} ({top_two_holdings_percentage:.2f}%)")

                if largest_holding_percentage >= 60:
                    print("   - \033[31mHIGH concentration risk\033[0m (outcome depends heavily on one asset).")
                elif top_two_holdings_percentage >= 75:
                    print("   - \033[33mMODERATE concentration risk\033[0m (two assets drive most performance).")
                else:
                    print("   - \033[32mHealthier diversification\033[0m (single-asset shocks reduced).")

            high_cap_exposure_percentage = (market_cap_live_value_totals["High"] / total_live_portfolio_value) * 100
            mid_cap_exposure_percentage = (market_cap_live_value_totals["Mid"] / total_live_portfolio_value) * 100
            low_cap_exposure_percentage = (market_cap_live_value_totals["Low"] / total_live_portfolio_value) * 100

            print("\n3) Market Cap Mix")
            print(f"   - High-cap : {high_cap_exposure_percentage:.2f}%")
            print(f"   - Mid-cap  : {mid_cap_exposure_percentage:.2f}%")
            print(f"   - Low-cap  : {low_cap_exposure_percentage:.2f}%")

            if (mid_cap_exposure_percentage + low_cap_exposure_percentage) >= 60:
                print("   - \033[33mGrowth-focused\033[0m (higher upside, more vulnerable to downturns).")
            else:
                print("   - \033[32mStability-focused\033[0m (typically more resilient in volatility spikes).")

            print("\n4) Recommended Actions")
            recommended_actions = []
            if highly_volatile_exposure_percentage >= 40:
                recommended_actions.append("Rebalance: Reduce highly volatile exposure to stabilise portfolio swings.")
            if volatile_exposure_percentage >= 50:
                recommended_actions.append("Monitoring: Set alerts and review volatile positions more frequently.")
            if len(live_holding_value_list) > 0 and largest_holding_percentage >= 60:
                recommended_actions.append("Diversify: Reduce reliance on one dominant holding to control concentration risk.")
            if (mid_cap_exposure_percentage + low_cap_exposure_percentage) >= 70:
                recommended_actions.append("Risk posture: Increase high-cap allocation to improve resilience during volatility spikes.")
            if not recommended_actions:
                recommended_actions.append("Maintain: Risk mix is balanced; continue monitoring and stay diversified.")

            for action_number, action_text in enumerate(recommended_actions, 1):
                print(f"   {action_number}. {action_text}")

        print(SEPARATOR)

        exit_option = input("Enter E to exit : ")
        if exit_option.upper() == "E":
            break

        os.system('cls')


def live_market_scenario_simulation_menu():
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

        scenario_menu_option = input("Select an option: ").strip()

        if scenario_menu_option.upper() == "E":
            break

        if scenario_menu_option == "1":
            scenario_name = "Bull Market (+10%)"
            scenario_percentage_change = 10
            os.system('cls')
            live_market_scenario_simulation(scenario_name, scenario_percentage_change)

        elif scenario_menu_option == "2":
            scenario_name = "Bear Market (-10%)"
            scenario_percentage_change = -10
            os.system('cls')
            live_market_scenario_simulation(scenario_name, scenario_percentage_change)

        elif scenario_menu_option == "3":
            scenario_name = "Market Crash (-30%)"
            scenario_percentage_change = -30
            os.system('cls')
            live_market_scenario_simulation(scenario_name, scenario_percentage_change)

        elif scenario_menu_option == "4":
            while True:
                try:
                    scenario_percentage_change = float(input("Enter scenario % change : "))
                    scenario_name = f"Custom Scenario ({scenario_percentage_change:+.2f}%)"
                    break
                except ValueError:
                    print("\033[31mError: Invalid input. Please enter a numeric percentage (e.g., 10, -10, 2.5).\033[0m\n")

            os.system('cls')
            live_market_scenario_simulation(scenario_name, scenario_percentage_change)

        os.system('cls')


def live_market_scenario_simulation(scenario_name, scenario_percentage_change):
    while True:
        scenario_multiplier = 1 + (scenario_percentage_change / 100)

        total_base_live_portfolio_value = 0
        total_simulated_portfolio_value = 0
        missing_live_data_count = 0

        print(MID_LENGTH_SEPARATOR)
        print(f"Scenario: {scenario_name}".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)
        print(f"{'No':<8}{'Name':<19}{'Qty Bought':<18}{'Live Price':<18}{'Simulation Price':<22}{'Live Value':<18}{'Simulation Value':<24}{'Impact'}")
        print(MID_LENGTH_SEPARATOR)

        for crypto_record in crypto_portfolio_database:
            crypto_number = crypto_record[IDX_NO]
            crypto_name = crypto_record[IDX_NAME]
            crypto_quantity_bought = crypto_record[IDX_QTY]
            live_market_price = live_crypto_prices.get(crypto_name)

            if isinstance(live_market_price, (int, float)):
                base_live_value = crypto_quantity_bought * live_market_price
                simulated_price = live_market_price * scenario_multiplier
                simulated_value = crypto_quantity_bought * simulated_price

                value_impact = simulated_value - base_live_value
                impact_text = f"{value_impact:+.2f}"

                if value_impact >= 0:
                    impact_text = "\033[32m" + impact_text + "\033[0m"
                else:
                    impact_text = "\033[31m" + impact_text + "\033[0m"

                total_base_live_portfolio_value += base_live_value
                total_simulated_portfolio_value += simulated_value

                print(f"{format_number(crypto_number):<8}{crypto_name:<19}{format_number(crypto_quantity_bought):<18}{format_number(live_market_price):<18}{format_number(simulated_price):<22}{format_number(base_live_value):<18}{format_number(simulated_value):<24}{impact_text}")
            else:
                missing_live_data_count += 1
                print(f"{format_number(crypto_number):<8}{crypto_name:<19}{format_number(crypto_quantity_bought):<18}{'\033[90mN/A\033[0m':<27}{'\033[90mN/A\033[0m':<31}{'\033[90mN/A\033[0m':<27}{'\033[90mN/A\033[0m':<33}{'\033[90mNO LIVE DATA (N/A)\033[0m'}")

        print(MID_LENGTH_SEPARATOR)

        if total_base_live_portfolio_value > 0:
            portfolio_value_impact = total_simulated_portfolio_value - total_base_live_portfolio_value
            portfolio_impact_percentage = (portfolio_value_impact / total_base_live_portfolio_value) * 100

            portfolio_impact_text = f"{portfolio_value_impact:+.2f} ({portfolio_impact_percentage:+.2f}%)"
            if portfolio_value_impact >= 0:
                portfolio_impact_text = "\033[32m" + portfolio_impact_text + "\033[0m"
            else:
                portfolio_impact_text = "\033[31m" + portfolio_impact_text + "\033[0m"

            print(f"{'TOTAL':<85}{format_number(total_base_live_portfolio_value):<18}{format_number(total_simulated_portfolio_value):<24}{portfolio_impact_text}")
            print(MID_LENGTH_SEPARATOR)

        if missing_live_data_count > 0:
            print(f"\033[33mNote: {missing_live_data_count} crypto(s) had no live data and were excluded from the scenario TOTAL calculations.\033[0m\n")

        exit_option = input("Enter E to exit : ")
        if exit_option.upper() == "E":
            break

        os.system('cls')


def investment_recommendation():
    while True:
        stable_deviation_threshold_percentage = 10
        volatile_deviation_threshold_percentage = 20

        high_volatility_exposure_alert_percentage = 40
        concentration_alert_percentage = 60
        top_two_holdings_alert_percentage = 75
        mid_low_market_cap_alert_percentage = 70
        strong_gain_alert_percentage = 15
        big_loss_alert_percentage = -20

        total_invested_value = 0
        total_live_portfolio_value = 0
        missing_live_data_count = 0

        stable_assets_live_value = 0
        volatile_assets_live_value = 0
        highly_volatile_assets_live_value = 0

        market_cap_live_value_totals = {"High": 0, "Mid": 0, "Low": 0}

        live_holding_value_list = []
        live_roi_movers_list = []

        print(MID_LENGTH_SEPARATOR)
        print("Investment Recommendation".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)

        for crypto_record in crypto_portfolio_database:
            crypto_name = crypto_record[IDX_NAME]
            crypto_quantity_bought = crypto_record[IDX_QTY]
            crypto_buy_price = crypto_record[IDX_BUY]
            stored_current_price = crypto_record[IDX_CURRENT]
            market_capitalization_category = crypto_record[IDX_CAP]
            live_market_price = live_crypto_prices.get(crypto_name)

            invested_value = crypto_quantity_bought * crypto_buy_price

            if isinstance(live_market_price, (int, float)) and invested_value != 0:
                live_value = crypto_quantity_bought * live_market_price
                live_profit_loss_value = live_value - invested_value
                live_return_on_investment_percentage = (live_profit_loss_value / invested_value) * 100

                total_invested_value += invested_value
                total_live_portfolio_value += live_value

                if isinstance(stored_current_price, (int, float)) and stored_current_price != 0:
                    deviation_percentage = abs(live_market_price - stored_current_price) / stored_current_price * 100
                else:
                    deviation_percentage = 0

                if deviation_percentage <= stable_deviation_threshold_percentage:
                    stable_assets_live_value += live_value
                elif deviation_percentage <= volatile_deviation_threshold_percentage:
                    volatile_assets_live_value += live_value
                else:
                    highly_volatile_assets_live_value += live_value

                if market_capitalization_category in market_cap_live_value_totals:
                    market_cap_live_value_totals[market_capitalization_category] += live_value

                live_holding_value_list.append((crypto_name, live_value))
                live_roi_movers_list.append((crypto_name, live_return_on_investment_percentage, live_profit_loss_value, market_capitalization_category))
            else:
                missing_live_data_count += 1

        if total_live_portfolio_value == 0 or total_invested_value == 0:
            print("\033[33mNo live data available to generate investment recommendations.\033[0m")
            if missing_live_data_count > 0:
                print(f"\033[33mNote: {missing_live_data_count} crypto(s) could not be analysed due to missing live data.\033[0m")
            print(MID_LENGTH_SEPARATOR)
            exit_option = input("Enter E to exit : ")
            if exit_option.upper() == "E":
                break
            os.system('cls')
            continue

        total_profit_loss_value = total_live_portfolio_value - total_invested_value
        total_return_on_investment_percentage = (total_profit_loss_value / total_invested_value) * 100

        total_profit_loss_text = f"{total_profit_loss_value:+.2f} ({total_return_on_investment_percentage:+.2f}%)"
        total_profit_loss_text = (("\033[32m" + total_profit_loss_text + "\033[0m") if total_profit_loss_value >= 0 else ("\033[31m" + total_profit_loss_text + "\033[0m"))

        stable_exposure_percentage = (stable_assets_live_value / total_live_portfolio_value) * 100
        volatile_exposure_percentage = (volatile_assets_live_value / total_live_portfolio_value) * 100
        highly_volatile_exposure_percentage = (highly_volatile_assets_live_value / total_live_portfolio_value) * 100

        high_cap_exposure_percentage = (market_cap_live_value_totals["High"] / total_live_portfolio_value) * 100
        mid_cap_exposure_percentage = (market_cap_live_value_totals["Mid"] / total_live_portfolio_value) * 100
        low_cap_exposure_percentage = (market_cap_live_value_totals["Low"] / total_live_portfolio_value) * 100
        mid_low_cap_exposure_percentage = mid_cap_exposure_percentage + low_cap_exposure_percentage

        live_holding_value_list.sort(key=lambda x: x[1], reverse=True)
        largest_holding_name, largest_holding_live_value = live_holding_value_list[0]
        largest_holding_percentage = (largest_holding_live_value / total_live_portfolio_value) * 100

        top_two_holdings_percentage = largest_holding_percentage
        second_largest_holding_name = ""
        if len(live_holding_value_list) > 1:
            second_largest_holding_name, second_largest_holding_live_value = live_holding_value_list[1]
            top_two_holdings_percentage = ((largest_holding_live_value + second_largest_holding_live_value) / total_live_portfolio_value) * 100

        live_roi_movers_list.sort(key=lambda x: x[1], reverse=True)

        gainers_only_list = [m for m in live_roi_movers_list if m[1] > 0]
        losers_only_list = [m for m in live_roi_movers_list if m[1] < 0]

        top_gainers_list = gainers_only_list[:2]
        top_losers_list = sorted(losers_only_list, key=lambda x: x[1])[:2]

        print(f"{'Live Portfolio Value':<28}: {format_number(total_live_portfolio_value)}")
        print(f"{'Total Invested Value':<28}: {format_number(total_invested_value)}")
        print(f"{'Unrealised P/L & ROI':<28}: {total_profit_loss_text}")
        print(MID_LENGTH_SEPARATOR)

        if missing_live_data_count > 0:
            print(f"\033[33mNote: {missing_live_data_count} crypto(s) were excluded from analysis due to missing live data.\033[0m")
            print(MID_LENGTH_SEPARATOR)

        print("\n\n" + MID_LENGTH_SEPARATOR)
        print("Risk & Allocation Snapshot".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)
        print(f"{'Stable exposure':<28}: {stable_exposure_percentage:>.2f}%")
        print(f"{'Volatile exposure':<28}: {volatile_exposure_percentage:>.2f}%")
        print(f"{'Highly volatile exposure':<28}: {highly_volatile_exposure_percentage:>.2f}%")
        print(MID_LENGTH_SEPARATOR)
        print(f"{'High-cap exposure':<28}: {high_cap_exposure_percentage:>.2f}%")
        print(f"{'Mid-cap exposure':<28}: {mid_cap_exposure_percentage:>.2f}%")
        print(f"{'Low-cap exposure':<28}: {low_cap_exposure_percentage:>.2f}%")
        print(MID_LENGTH_SEPARATOR)
        print(f"{'Largest holding':<28}: {largest_holding_name} ({largest_holding_percentage:.2f}%)")
        if second_largest_holding_name:
            print(f"{'Top 2 holdings':<28}: {largest_holding_name} + {second_largest_holding_name} ({top_two_holdings_percentage:.2f}%)")
        print(MID_LENGTH_SEPARATOR)

        print("\n\n" + MID_LENGTH_SEPARATOR)
        print("Top Movers (Live ROI)".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)

        print("\033[32mTop Gainers\033[0m")
        if len(top_gainers_list) == 0:
            print("- None (no profitable assets)")
        else:
            for crypto_name, roi_percentage, live_profit_loss_value, market_capitalization_category in top_gainers_list:
                roi_text = f"{roi_percentage:+.2f}%"
                profit_loss_text = f"({live_profit_loss_value:+.2f})"
                print(f"- {crypto_name:<14} {roi_text:<10} {profit_loss_text:<14} [{market_capitalization_category}]")

        print("\n\033[31mTop Losers\033[0m")
        if len(top_losers_list) == 0:
            print("- None (no losing assets)")
        else:
            for crypto_name, roi_percentage, live_profit_loss_value, market_capitalization_category in top_losers_list:
                roi_text = f"{roi_percentage:+.2f}%"
                profit_loss_text = f"({live_profit_loss_value:+.2f})"
                print(f"- {crypto_name:<14} {roi_text:<10} {profit_loss_text:<14} [{market_capitalization_category}]")

        print(MID_LENGTH_SEPARATOR)

        print("\n\n" + MID_LENGTH_SEPARATOR)
        print("Recommendation Summary".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)

        recommendation_list = []
        recommendation_reason_list = []

        if total_return_on_investment_percentage >= strong_gain_alert_percentage:
            recommendation_list.append("Profit discipline: Consider taking partial profits on your strongest gainers.")
            recommendation_reason_list.append(f"Portfolio ROI is strong ({total_return_on_investment_percentage:+.2f}%); locking in gains helps reduce reversal risk.")
        elif total_return_on_investment_percentage <= big_loss_alert_percentage:
            recommendation_list.append("Defensive posture: Reduce exposure to highly volatile assets and review your allocation.")
            recommendation_reason_list.append(f"Portfolio drawdown is significant ({total_return_on_investment_percentage:+.2f}%); risk control should be the priority.")
        else:
            recommendation_list.append("Hold & monitor: Maintain positions, but keep risk checks and reviews active.")
            recommendation_reason_list.append(f"Portfolio ROI is moderate ({total_return_on_investment_percentage:+.2f}%); focus on risk control and diversification.")

        if highly_volatile_exposure_percentage >= high_volatility_exposure_alert_percentage:
            recommendation_list.append("Risk reduction: Rebalance to reduce highly volatile exposure.")
            recommendation_reason_list.append(f"Highly volatile exposure is high ({highly_volatile_exposure_percentage:.2f}%); portfolio value may experience sharp swings.")

        if largest_holding_percentage >= concentration_alert_percentage:
            recommendation_list.append("Diversification: Reduce reliance on the largest holding to manage concentration risk.")
            recommendation_reason_list.append(f"{largest_holding_name} dominates ({largest_holding_percentage:.2f}%); a single-asset shock could heavily impact overall performance.")
        elif top_two_holdings_percentage >= top_two_holdings_alert_percentage:
            recommendation_list.append("Diversification: Spread allocation across more assets to reduce dependency on top holdings.")
            recommendation_reason_list.append(f"Top 2 holdings dominate ({top_two_holdings_percentage:.2f}%); overall performance depends heavily on them.")

        if mid_low_cap_exposure_percentage >= mid_low_market_cap_alert_percentage:
            recommendation_list.append("Stability shift: Consider increasing high-cap allocation to improve portfolio resilience.")
            recommendation_reason_list.append(f"Mid/Low-cap exposure is high ({mid_low_cap_exposure_percentage:.2f}%); these assets typically carry higher risk and volatility.")

        recommendation_list.append("Action focus: Review top losers for risk control, and apply profit rules to top gainers.")
        recommendation_reason_list.append("Prioritise the biggest movers to manage downside risk and lock in gains systematically.")

        seen_recommendations = set()
        final_recommendation_list = []
        for recommendation_text in recommendation_list:
            if recommendation_text not in seen_recommendations:
                final_recommendation_list.append(recommendation_text)
                seen_recommendations.add(recommendation_text)

        for recommendation_number, recommendation_text in enumerate(final_recommendation_list, 1):
            print(f"{recommendation_number}. {recommendation_text}")

        print(MID_LENGTH_SEPARATOR)
        print("Why these recommendations?".center(len(MID_LENGTH_SEPARATOR)))
        print(MID_LENGTH_SEPARATOR)
        for reason_text in recommendation_reason_list[:6]:
            print(f"- {reason_text}")

        print(MID_LENGTH_SEPARATOR)
        exit_option = input("Enter E to exit : ")
        if exit_option.upper() == "E":
            break

        os.system('cls')


# API function to get crypto price
def get_crypto_price(crypto_id):
    global COIN_GECKO_DEMO_API_KEY

    # this url gives us crypto price in USD
    # crypto_id can be: bitcoin, ethereum, solana, dogecoin
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd&x_cg_demo_api_key={COIN_GECKO_DEMO_API_KEY}"

    try:
        # get data from internet
        response = requests.get(url)

        # convert to python dictionary
        data = response.json()

        # extract the price
        price = data[crypto_id]['usd']

        return price
    except:
        # if error, return None
        return None


# API function to get price history
def get_price_history(crypto_id):
    global COIN_GECKO_DEMO_API_KEY
    # this url gives us past 7 days of crypto prices
    # crypto_id can be: bitcoin, ethereum, solana, dogecoin
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart?vs_currency=usd&days=7&x_cg_demo_api_key={COIN_GECKO_DEMO_API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        # get prices from data
        all_prices = data['prices']

        # we only want 7 prices (one per day)
        history = []
        step = len(all_prices) // 7

        for i in range(7):
            idx = i * step
            if idx < len(all_prices):
                history.append(all_prices[idx][1])

        return history
    except:
        return None


def crypto_trading_game():
    """
    CRYPTO TRADING GAME
    By: [NUR ADHILLA BINTE ABDUL RAHMAN]

    This game uses real crypto prices from the internet!
    Player has to analyze past prices and guess if price will go up or down.
    Now supports: Bitcoin, Ethereum, Solana, and Dogecoin!
    """
    global player_money, streak

    #All of the 4 cryptos
    crypto_list = [
        ["bitcoin", "Bitcoin"],
        ["ethereum", "Ethereum"],
        ["solana", "Solana"],
        ["dogecoin", "Dogecoin"]
    ]

    print("\n" + "="*70)
    print("CRYPTO TRADING GAME")
    print("="*70)
    print("This game uses REAL crypto data from the internet!")
    print("Analyze the trend and predict if price will go UP or DOWN")
    print("Cryptos: Bitcoin, Ethereum, Solana, Dogecoin")
    print("="*70)
    print(f"Your Money: ${player_money}")
    print(f"Win Streak: {streak}")
    print("="*70)

    # check internet connection
    print("\nConnecting to internet...")
    test = get_crypto_price("bitcoin")

    if test is None:
        print("ERROR: Cannot connect to internet!")
        print("Please check your connection and try again.")
        return

    print(f"Connected! Bitcoin is currently ${test:,.2f}")

    # game loop
    while True:
        # check win condition
        if streak >= 10:
            print("\n" + "="*70)
            print("YOU WIN! You reached 10 streak!")
            print(f"Final Money: ${player_money}")
            print("="*70)

            again = input("\nPlay again? (Y/N): ").upper()
            if again == 'Y':
                player_money = 1000
                streak = 0
                continue
            else:
                break

        # check lose condition
        if player_money <= 0:
            print("\n" + "="*70)
            print("GAME OVER! You ran out of money!")
            print(f"Final Streak: {streak}")
            print("="*70)

            again = input("\nPlay again? (Y/N): ").upper()
            if again == 'Y':
                player_money = 1000
                streak = 0
                continue
            else:
                break

        print("\n" + "-"*70)
        print(f"Your Money: ${player_money}")
        print(f"Win Streak: {streak}")
        print("-"*70)

        # Select random crypto for this round
        # Use streak to cycle through cryptos (simple random method)
        crypto_index = streak % len(crypto_list)
        crypto_id = crypto_list[crypto_index][0]
        crypto_name = crypto_list[crypto_index][1]

        print(f"\n*** Trading {crypto_name} this round! ***")

        # get price history from internet
        print(f"\nGetting {crypto_name} price history...")
        history = get_price_history(crypto_id)

        if history is None:
            print("ERROR: Failed to get price data!")
            retry = input("Try again? (Y/N): ").upper()
            if retry != 'Y':
                break
            continue

        print("Done!\n")

        # show past 7 days prices
        print(f"Past 7 Days {crypto_name} Prices:")
        print("-"*70)

        ups = 0
        downs = 0

        for i in range(len(history)):
            price = history[i]

            if i == 0:
                print(f"Day {i+1}: ${price:,.2f}")
            else:
                old_price = history[i-1]
                change = price - old_price
                percent = (change / old_price) * 100

                if change > 0:
                    print(f"Day {i+1}: ${price:,.2f} UP +{percent:.2f}%")
                    ups = ups + 1
                else:
                    print(f"Day {i+1}: ${price:,.2f} DOWN {percent:.2f}%")
                    downs = downs + 1

        print("-"*70)
        print(f"Summary: {ups} days went up, {downs} days went down")
        print(f"Latest price (Day 7): ${history[-1]:,.2f}")
        print("-"*70)

        # get current live price
        print(f"\nGetting current live {crypto_name} price...")
        current = get_crypto_price(crypto_id)

        if current is None:
            print("ERROR: Failed to get current price!")
            continue

        print(f"Current price now: ${current:,.2f}\n")

        # player bets with validation
        while True:
            bet = input(f"How much to bet? (max ${player_money}) or Q to quit: ").strip()

            # remove dollar sign if user typed it
            bet = bet.replace("$", "")
            bet = bet.replace(",", "")

            if bet.upper() == 'Q':
                print(f"\nThanks for playing!")
                print(f"Final Money: ${player_money}")
                print(f"Final Streak: {streak}")
                return

            # check if valid number
            try:
                bet_amount = float(bet)
            except:
                print("Please enter numbers only! (no $ or other symbols)")
                continue

            # check if positive
            if bet_amount <= 0:
                print("Bet must be greater than 0!")
                continue

            # check if enough money
            if bet_amount > player_money:
                print(f"You don't have enough money! You only have ${player_money}")
                continue

            # all checks passed!
            break

        # player predicts with validation
        while True:
            prediction = input(f"\nWill {crypto_name} price go UP or DOWN? (U/D): ").strip().upper()

            if prediction == 'U' or prediction == 'D':
                break
            else:
                print("Please enter U for UP or D for DOWN only!")

        # wait for new price
        print("\nWaiting for price to change", end="")
        for i in range(5):
            time.sleep(1)
            print(".", end="")
        print()

        print(f"\nGetting new {crypto_name} price...")
        new_price = get_crypto_price(crypto_id)

        if new_price is None:
            print("ERROR: Failed to get new price!")
            continue

        # calculate change
        change = new_price - current
        percent = (change / current) * 100

        # show result
        print("\n" + "="*70)
        print("RESULT")
        print("="*70)
        print(f"Crypto: {crypto_name}")
        print(f"Old price: ${current:,.2f}")
        print(f"New price: ${new_price:,.2f}")
        print(f"Change: ${change:+,.2f} ({percent:+.2f}%)")

        # determine if up or down
        if change > 0:
            actual = 'U'
            print("Price went UP")
        elif change < 0:
            actual = 'D'
            print("Price went DOWN")
        else:
            actual = 'S'
            print("Price STAYED THE SAME")

        print("="*70)

        # check if player won
        if actual == 'S':
            print("\nPrice didn't change - bet returned")
        elif prediction == actual:
            # player won!
            win_amount = bet_amount * 0.5
            player_money = player_money + win_amount
            streak = streak + 1

            print("\nCORRECT! YOU WIN!")
            print(f"You won ${win_amount}")
            print(f"New money: ${player_money}")
            print(f"Win streak: {streak}")
        else:
            # player lost
            player_money = player_money - bet_amount
            streak = 0

            print("\nWRONG! YOU LOSE!")
            print(f"You lost ${bet_amount}")
            print(f"New money: ${player_money}")
            print(f"Streak reset to 0")

        print("="*70)

        # continue?
        if player_money > 0 and streak < 10:
            cont = input("\nKeep playing? (Y/N): ").upper()
            if cont != 'Y':
                print(f"\nThanks for playing!")
                print(f"Final Money: ${player_money}")
                print(f"Final Streak: {streak}")
                break


def launch_application():
    os.system('cls')

    while True:
        selected_main_menu_option = main_menu()

        if selected_main_menu_option == "1":
            os.system('cls')
            display_crypto()
            os.system('cls')

        elif selected_main_menu_option == "2":
            os.system('cls')
            add_crypto()
            os.system('cls')

        elif selected_main_menu_option == "3":
            os.system('cls')
            amend_crypto()
            os.system('cls')

        elif selected_main_menu_option == "4":
            os.system('cls')
            remove_crypto()
            os.system('cls')

        elif selected_main_menu_option == "5":
            os.system('cls')
            crypto_portfolio_statement()
            os.system('cls')

        elif selected_main_menu_option == "6":
            os.system('cls')

            while True:
                selected_business_analysis_menu_option = portfolio_business_analysis_menu()

                if selected_business_analysis_menu_option == "1":
                    os.system('cls')
                    fetch_live_prices()
                    live_price_comparison()
                    os.system('cls')

                elif selected_business_analysis_menu_option == "2":
                    os.system('cls')
                    fetch_live_prices()
                    real_time_portfolio_report()
                    os.system('cls')

                elif selected_business_analysis_menu_option == "3":
                    os.system('cls')
                    fetch_live_prices()
                    market_volatility_risk_analysis()
                    os.system('cls')

                elif selected_business_analysis_menu_option == "4":
                    os.system('cls')
                    fetch_live_prices()
                    live_market_scenario_simulation_menu()
                    os.system('cls')

                elif selected_business_analysis_menu_option == "5":
                    os.system('cls')
                    fetch_live_prices()
                    investment_recommendation()
                    os.system('cls')

                elif selected_business_analysis_menu_option.upper() == "E":
                    os.system('cls')
                    break

                else:
                    os.system('cls')

        elif selected_main_menu_option == "7":
            os.system('cls')
            crypto_trading_game()
            os.system('cls')

        elif selected_main_menu_option.upper() == "E":
            os.system('cls')
            print("You have successfully exited the application. Thank you!.")
            break

        else:
            os.system('cls')


launch_application()