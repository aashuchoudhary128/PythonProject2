prices= input("Enter prices of sold items separated by spaces: ")
prices = tuple(map(float, prices.split()))
print("Total number of items sold:", len(prices))
if len(prices) > 0:
    cheapest = min(prices)
    print("Cheapest item price:", cheapest)
    costliest = max(prices)
    print("Costliest item price:", costliest)
    print("Prices in ascending order:", tuple(sorted(prices)))
    count_costliest = prices.count(costliest)
    print("Number of costliest items sold:", count_costliest)
else:
    print("No items sold.")