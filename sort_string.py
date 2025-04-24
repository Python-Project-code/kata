def sort_string(s, ordering):
    
    # Remove duplicates from the second string
    list_ordering =  list(ordering)   
    ordering_no_duplicate = []

  
    [ordering_no_duplicate.append(l) for l in list_ordering if l not in ordering_no_duplicate]

    # Sort the first string using the second string as a guide
    count_letter = {}
    for letter in s:
       count_letter[letter] = count_letter.get(letter, 0) + 1
     

    print("count",count_letter.items())
    
    sorted_s = []
    for letter in ordering_no_duplicate:
        if letter in count_letter:
            sorted_s.extend([letter] * count_letter[letter])
            count_letter.pop(letter)  # remove it from the dict to handle the rest

    # Add the remaining letters in original order
    for l in s:
        if l in count_letter:
            sorted_s.append(l)
            count_letter[l] -= 1
            if count_letter[l] == 0:
                count_letter.pop(l)


    return "".join(sorted_s)



print(sort_string("banana", "xyz"))

#print(sort_string("foos", "of"))
#sort_string("string", "gnirts") 
#sort_string("banana", "abn") 