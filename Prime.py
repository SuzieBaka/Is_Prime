Bool = 0
num = 0
div = 2
while Bool == 0:
    num = input("Gimme Number:")
    try:
        int(num)
        print("input valid")
        Bool = 1
    except:
        Bool = 0
num = int(num)
while num%div != 0 and num/div > 2:
    div+= 1
if num%div == 0:
    print("composite")
else:
    print("prime")
        
        
    
