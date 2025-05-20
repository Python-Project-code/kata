def to_bcd(n):
    
    
    negative =""
    n_str = str(n)
    dig = list(n_str)
    if n < 0:
        negative = "-"
        n_str = str(n)
        dig = list(n_str)[1:]
        
  
    bcd= []
    for d in dig:
        bcd.append(bin(int(d))[2:].zfill(4))

    return(negative + " ".join(bcd))




print(to_bcd(-10 ))