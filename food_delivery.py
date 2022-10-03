chiken_menu_count = int(input())
fish_menu_count = int(input())
vegan_menu_count = int(input())

price_chicken  = chiken_menu_count * 10.35
price_fish = fish_menu_count * 12.4
price_vegan = vegan_menu_count * 8.15

all_price_menu = price_chicken + price_fish + price_vegan
desert_price = all_price_menu * 0.20

total_summ = all_price_menu + desert_price + 2.5
print(total_summ)