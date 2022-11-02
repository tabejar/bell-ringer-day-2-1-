coffee_prices =[('cappucino', 1.5,),
               ('expresso',1.2),
               ('mocha',1.9)]

#retrieve the prices and price from the above tuple

for coffee, price in coffee_prices:
  print(f"{coffee} costs ${price}")
# create a function for retrieving the highest priced coffee and name
print("Welcome Jonesy")
expensive = max(coffee_prices)
print(f"The most expensive coffee is {coffee} and it costs ${price}")

def most_expensive_coffee(coffee_prices):
  highest_prices = 0
  my_most_expensive_coffee = ''
  for coffee, price in coffee_prices:
    if price > highest_prices:
      highest_prices = price
      my_most_expensive_coffee = coffee
  else:
    pass
  return(my_most_expensive_coffee, highest_prices)
  
print(most_expensive_coffee(coffee_prices))
  