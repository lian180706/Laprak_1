def fibonachi (n):
    if n<0 :
        return print("maka tidak ada nilai fibonachi")
    elif n == (1) or n == (2):
        return (1)
    else:
        return (fibonachi (n-1))+ (fibonachi (n-2))
    
#mencari nilai fibonachi
a = int(input("masukkan nilai fibonachi: "))
cari_fibonachi=fibonachi (a)
print ("nilai dari",a,"! adalah ",cari_fibonachi)

    
    
    

