def square_color(file, rank):

    column_number = ord(file) - ord('a') + 1
    print((rank + column_number) % 2 )

    return "black" if (rank + column_number) % 2 == 0 else "white" 



print(square_color("b", 2))