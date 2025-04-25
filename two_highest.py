def two_highest(arg1):
      
    unique_values = set(arg1) 
   
    sorted_values = sorted(unique_values, reverse=True)  
    return sorted_values[:2] 

print(two_highest([4, 10, 10, 9]))