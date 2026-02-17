def  caluculate_total_bill(amount,tip_percentage):
   
    total= amount + (amount* (tip_percentage/100)) 
    print(total)
    rd= round(total,2)
    return rd

amt= float(input ("Enter the Amount :"))
tp= int(input("Enter tip percentage :"))
if (amt>=0 and amt<=10,000) and (tp>=0 and tp<=100):
    disp= caluculate_total_bill(amt,tp)
    print("The Total bill caluculated :",disp)
else:
    print("Limit Exceeded")
