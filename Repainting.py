nylon_count = float(input())
paint_count = float(input())
paint_thinner = float(input())
hours = float(input())

nylon_price = (nylon_count+2) * 1.50
paint_price = paint_count * 15.95
paint_thinner_price = paint_thinner * 5.00
bags_price = 0.40


all_price = nylon_price + paint_price + paint_thinner_price + bags_price
total_summ = (all_price * 0.30)  * hours

print(total_summ)