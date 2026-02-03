import time
import requests

# Crypto data - stored as 2D list (requirement from assignment)
crypto_data = [
    ["Bitcoin", "High", 15, 38000, 62000],
    ["Ethereum", "High", 90, 4200, 3500],
    ["Solana", "Mid", 60, 260, 110],
    ["Decentraland", "Mid", 30000, 1.5, 5],
    ["The Sandbox", "Mid", 25000, 2, 4],
    ["Dogecoin", "Low", 55000, 0.4, 0.15]
]

# Game variables
player_money = 1000
streak = 0

def display_menu():
    print("\n" + "="*60)
    print("CRYPTOCURRENCY PORTFOLIO APPLICATION".center(60))
    print("="*60)
    print("1. Display All Cryptocurrency")
    print("2. Add Cryptocurrency")
    print("3. Amend Cryptocurrency")
    print("4. Remove Cryptocurrency")
    print("5. Crypto Portfolio Statement")
    print("6. Crypto Trading Game")
    print("7. [Student 2 Function]")
    print("0. Exit")
    print("="*60)

def display_all_crypto():
    print("\n" + "="*100)
    print("ALL CRYPTOCURRENCY".center(100))
    print("="*100)
    print(f"{'No':<5}{'Name':<15}{'Capitalization':<15}{'Qty Bought':<15}{'Bought Price':<15}{'Current Price':<15}")
    print("-"*100)
    
    for i in range(len(crypto_data)):
        name = crypto_data[i][0]
        cap = crypto_data[i][1]
        qty = crypto_data[i][2]
        buy_price = crypto_data[i][3]
        current_price = crypto_data[i][4]
        print(f"{i+1:<5}{name:<15}{cap:<15}{qty:<15}{buy_price:<15.2f}{current_price:<15.2f}")
    
    print("="*100)

def add_cryptocurrency():
    print("\n" + "="*60)
    print("ADD CRYPTOCURRENCY".center(60))
    print("="*60)
    
    name = input("Enter Cryptocurrency Name: ").strip()
    
    # check if exists
    exists = False
    for i in range(len(crypto_data)):
        if crypto_data[i][0].lower() == name.lower():
            exists = True
            break
    
    if exists:
        print("This cryptocurrency already exists!")
        return
    
    cap = input("Enter Market Cap (High/Mid/Low): ").strip().capitalize()
    
    qty = float(input("Enter Quantity of Crypto Bought: "))
    buy_price = float(input("Enter Buy In Price of Crypto: $"))
    current_price = float(input("Enter Current Market Price of Crypto: $"))
    
    crypto_data.append([name, cap, qty, buy_price, current_price])
    print(f"\n{name} has been added!")

def amend_cryptocurrency():
    while True:
        print("\n" + "="*60)
        print("AMEND CRYPTOCURRENCY".center(60))
        print("="*60)
        
        for i in range(len(crypto_data)):
            print(f"{i+1}. {crypto_data[i][0]}")
        
        print("\nE. Exit to Main Menu")
        
        choice = input("\nSelect cryptocurrency index: ").strip().upper()
        
        if choice == 'E':
            break
        
        try:
            index = int(choice) - 1
            if index < 0 or index >= len(crypto_data):
                print("Invalid index!")
                continue
        except:
            print("Invalid input!")
            continue
        
        print("\n" + "-"*60)
        print(f"Name: {crypto_data[index][0]}")
        print(f"1. Market Cap: {crypto_data[index][1]}")
        print(f"2. Quantity Bought: {crypto_data[index][2]}")
        print(f"3. Buy In Price: ${crypto_data[index][3]}")
        print(f"4. Current Market Price: ${crypto_data[index][4]}")
        print("-"*60)
        
        field = input("\nSelect field to update (1-4) or C to cancel: ").strip().upper()
        
        if field == 'C':
            break
        
        field_num = int(field)
        
        if field_num == 1:
            new_cap = input("Enter new Market Cap (High/Mid/Low): ").strip().capitalize()
            crypto_data[index][1] = new_cap
            print("Market Cap updated!")
        elif field_num == 2:
            new_qty = float(input("Enter new Quantity: "))
            crypto_data[index][2] = new_qty
            print("Quantity updated!")
        elif field_num == 3:
            new_price = float(input("Enter new Buy In Price: $"))
            crypto_data[index][3] = new_price
            print("Buy In Price updated!")
        elif field_num == 4:
            new_price = float(input("Enter new Current Market Price: $"))
            crypto_data[index][4] = new_price
            print("Current Market Price updated!")

def remove_cryptocurrency():
    while True:
        print("\n" + "="*60)
        print("REMOVE CRYPTOCURRENCY".center(60))
        print("="*60)
        
        for i in range(len(crypto_data)):
            print(f"{i+1}. {crypto_data[i][0]}")
        
        print("\nE. Exit to Main Menu")
        
        choice = input("\nSelect cryptocurrency index: ").strip().upper()
        
        if choice == 'E':
            break
        
        try:
            index = int(choice) - 1
        except:
            print("Invalid input!")
            continue
        
        crypto_name = crypto_data[index][0]
        confirm = input(f"\nAre you sure you want to remove {crypto_name}? (Y/N): ").strip().upper()
        
        if confirm == 'Y':
            crypto_data.pop(index)
            print(f"{crypto_name} has been removed!")

def portfolio_statement():
    print("\n" + "="*150)
    print("CRYPTO PORTFOLIO STATEMENT".center(150))
    print("="*150)
    
    headers = ["No", "Name", "Qty Bought", "Bought Price", "Current Price", 
               "Total Invested", "Invested Portfolio %", "Total Current Value", 
               "Profit/Loss", "Current Portfolio %"]
    
    print(f"{headers[0]:<5}{headers[1]:<15}{headers[2]:<12}{headers[3]:<15}{headers[4]:<15}"
          f"{headers[5]:<18}{headers[6]:<20}{headers[7]:<20}{headers[8]:<15}{headers[9]:<20}")
    print("-"*150)
    
    # calculate totals
    total_invested_sum = 0
    for i in range(len(crypto_data)):
        qty = crypto_data[i][2]
        buy_price = crypto_data[i][3]
        total_invested_sum = total_invested_sum + (qty * buy_price)
    
    total_current_sum = 0
    for i in range(len(crypto_data)):
        qty = crypto_data[i][2]
        current_price = crypto_data[i][4]
        total_current_sum = total_current_sum + (qty * current_price)
    
    # display each crypto
    for i in range(len(crypto_data)):
        name = crypto_data[i][0]
        qty = crypto_data[i][2]
        buy_price = crypto_data[i][3]
        current_price = crypto_data[i][4]
        
        total_invested = qty * buy_price
        invested_portfolio = (total_invested / total_invested_sum) * 100
        total_current = qty * current_price
        profit_loss = total_current - total_invested
        current_portfolio = (total_current / total_current_sum) * 100
        
        print(f"{i+1:<5}{name:<15}{qty:<12.2f}${buy_price:<14.2f}${current_price:<14.2f}"
              f"${total_invested:<17.2f}{invested_portfolio:<19.2f}%${total_current:<19.2f}"
              f"${profit_loss:<14.2f}{current_portfolio:<19.2f}%")
    
    print("-"*150)
    total_profit_loss = total_current_sum - total_invested_sum
    print(f"{'SUM':<5}{'':<15}{'':<12}{'':<15}{'':<15}"
          f"${total_invested_sum:<17.2f}{'':<20}${total_current_sum:<19.2f}"
          f"${total_profit_loss:<14.2f}")
    print("="*150)

# API function to get crypto price
def get_crypto_price(crypto_id):
    # this url gives us crypto price in USD
    # crypto_id can be: bitcoin, ethereum, solana, dogecoin
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies=usd"
    
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
    # this url gives us past 7 days of crypto prices
    # crypto_id can be: bitcoin, ethereum, solana, dogecoin
    url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart?vs_currency=usd&days=7"
    
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
    By: [YOUR NAME HERE]
    
    This game uses real crypto prices from the internet!
    Player has to analyze past prices and guess if price will go up or down.
    Now supports: Bitcoin, Ethereum, Solana, and Dogecoin!
    """
    global player_money, streak
    
    # List of available cryptos
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

def main():
    print("\nWelcome to Cryptocurrency Portfolio Manager!")
    
    while True:
        display_menu()
        choice = input("\nEnter choice: ").strip()
        
        if choice == '1':
            display_all_crypto()
        elif choice == '2':
            add_cryptocurrency()
        elif choice == '3':
            amend_cryptocurrency()
        elif choice == '4':
            remove_cryptocurrency()
        elif choice == '5':
            portfolio_statement()
        elif choice == '6':
            crypto_trading_game()
        elif choice == '7':
            print("\nStudent 2's function not implemented yet!")
        elif choice == '0':
            print("\nThank you! Goodbye!")
            break
        else:
            print("\nInvalid choice!")

if __name__ == "__main__":
    main()