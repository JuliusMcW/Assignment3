a = float(input('Enter year  number: '))
if a%4==0:
    if a%400==0:
        print('Yes,', a,'is a leap year')
    elif a%100!=0:
        print('Yes,',  a,  'is a leap year')
    else:
        print('No,',  a,  'is not a leap year')
else:
    print('No,', a,   'is not a leap year')



#developed using an online compiler. Simple doesn't have any specifications
