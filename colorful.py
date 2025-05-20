def colorful(number):

    

    dig_int = [int(digito) for digito in str(number)]
    print(dig_int)
    products = []
    for i in range(len(dig_int)):
        products.append(dig_int[i])

    for i in range(len(dig_int)-1):
        product = dig_int[i] * dig_int[i + 1]
        products.append(product)

    for i in range(len(dig_int)-2):
        product = dig_int[i] * dig_int[i + 1] * dig_int[i + 2]
        products.append(product)

    print(products)
   
    dig_uniques = set(products)
  

    if len(products) == len(dig_uniques):
        return True
    else:
        return False

  



print(colorful(236))


# 263  -->  true
# 236  -->  false