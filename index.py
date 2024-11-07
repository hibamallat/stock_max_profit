daily_prices = []

def max_profit(prices):
    max_profit = 0
    min_price = prices[0]

    for i in range(len(prices)):

        if min_price > prices[i]:

            min_price = prices[i]
        
        profit = prices[i] - min_price

        if profit > max_profit:
        
            max_profit = profit

    return max_profit

print("(Enter -1 to stop)")

try:
    for i in range (1 , 10):
        num = int(input(f"Enter a price for Day {i}: "))
        if num > 0 :
            daily_prices.append(num)
        elif num == -1 :
            break
        else:
            print("The number should be positive")
            
    print("The daily prices list:", daily_prices)
    print("The maximum possible profit:", max_profit(daily_prices))

except ValueError:
    print("You should enter a number")

