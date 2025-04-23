import re

def backpak(pile,basket):    
    # Extract only the numbers (coal weights) from the 'pile' string
    coal_weight = [int(n) for n in re.findall(r'\d+', pile)]

    dp = [0] * (basket + 1)
    # Find the best combination of weights that does not exceed the basket capacity
    for weight in coal_weight:
    
        for i in range(basket, weight - 1, -1):
            dp[i] = max(dp[i], dp[i - weight] + weight)

    return f'The basket weighs {dp[basket]} kilograms'
       

    


pile = 'dust83dust 45 25 22 46'

basket = 50
print(backpak(pile,basket))