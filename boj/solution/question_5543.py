import sys
prices = []
for i in range(5):
    prices.append(int(sys.stdin.readline()))
set_menu = []
for i in range(3):
    burger = prices[i]
    for j in range(3, 5):
        beverage = prices[j]
        set_menu.append(burger+beverage-50)
print(min(set_menu))        
