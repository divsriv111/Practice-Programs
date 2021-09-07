def MaxProfit(price):
    profit = 0
    for i in range(1, len(price)):
        if price[i] > price[i - 1]:
            profit += price[i] - price[i - 1]
    return profit


arr = list(map(int, input().strip().split()))
print(MaxProfit(arr))
