price_list = [10 , 2 , 12 , 24]
another_list_to_test = [5 , 7 , 2 , 9 , 1 , 3]

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

#for i in range (8):
#    num = int(input(""))
#    if num > 0 :
#        price_list.append(num)
#    elif num == -1 :
#        break
#    else:
#        print("The number should be positive")
        
print("The stock pricing list:", price_list)
print("The maximum possible profit:", max_profit(price_list))
print("The stock pricing list:", another_list_to_test)
print("The maximum possible profit:", max_profit(another_list_to_test))