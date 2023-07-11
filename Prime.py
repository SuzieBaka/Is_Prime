Bool = 0
num = 0
div = 2
while Bool == 0:
    num = input("Number to be checked: ")
    try:
        int(num)
        Bool = 1
    except:
        Bool = 0
num = int(num)
while num%div != 0 and num/div > 2:
    div+= 1
if num%div == 0 and num != 2:
    print(num, "is composite")
else:
    print(num, "is prime")
        
        
    
