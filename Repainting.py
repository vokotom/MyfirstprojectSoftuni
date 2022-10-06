nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

price_nylon = 1.50
price_paint = 14.50
price_thinner = 5
price_bags = 0.40

extra_nylon = nylon + 2
extra_paint = paint + (paint * 10 / 100)

final_price_nylon = extra_nylon * 1.50
final_price_paint = extra_paint * 14.50
final_price_thinner = thinner * 5

mat_price = final_price_paint + final_price_thinner + final_price_nylon + price_bags
work_price = hours * (mat_price * 30 / 100)

total_price = mat_price + work_price

print(total_price)
