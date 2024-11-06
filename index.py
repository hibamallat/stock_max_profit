price_list = []

for i in range (8):
    num = int(input(""))
    if num > 0 :
        price_list.append(num)
    elif num == -1 :
        break
    else:
        print("The number should be positive")
print(price_list)