price = float(input('enter price: '))
discount = float(input('enter discount %: '))

reduction = round((price * (discount)/100), 2)
price_with_discount = round((price - reduction), 2)

print(f'price is {price}, the discount is {discount}. price with discount is {price_with_discount}, and the reduction is {reduction}')