product = int(input('Please enter the price of the product: '))

if product >= 100:
    discount = product*0.10
    final_price = product - discount
else:
    discount = product*0.02
    final_price = product - discount

print(f'The final price of your product with the discount is {final_price}')