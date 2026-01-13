from collections import Counter

def get_shoe_money(x: int,
                   sizes: list[int],
                   n: int,
                   prices: list[tuple[int, int]]) -> int:
    
    stock = Counter(sizes)
    total_money = 0

    for shoe_size, price in prices:
        if stock.get(shoe_size, 0) > 0:
            total_money += price
            stock[shoe_size] -= 1
    
    return total_money


num_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
num_customers = int(input())

customers = []
for _ in range(num_customers):
    size, price = map(int, input().split())
    customers.append((size, price))

result = get_shoe_money(num_shoes, shoe_sizes, num_customers, customers)
print(result)