a= (input('Enter year number:'))

def number(a):
    str(a)
    y=0
    z=0
    while(y<len(a) and z==0):
        if((a[y])>="0" and (a[y])<="9"):
            y+=1
        else:
            z=1
    if(z==1):
        return False
    else:
        return True
        
while(number(a)==False):
    a=(input('Enter year number:'))


a=float(a)
if a%4==0:
        if a%400==0:
                print('Yes,', a,'is a leap year')
        elif a%100!=0:
                print('Yes,', a,'is a leap year')
        else:
                print('No,', a, 'is a leap year')
else:
    print('No,', a, 'is not a leap year')
