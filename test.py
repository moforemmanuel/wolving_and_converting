def compound_interest(principal, rate, years):
    """Return the calculated compound interest"""

    compound_amount = principal*((1 + (rate/400))**(4*years))
    #calculate compound interest
    return compound_amount
principal = 1500
year = 1
period = 1
while(year>0):
    for i in range(1,5):
        
        target = compound_interest(principal, 4.3, 1)
       
        if(target >= 2000):
           
            break
        else:
            principal = target
            i+=1
            year+=1
    if(target >= 2000):
        break
print(year);