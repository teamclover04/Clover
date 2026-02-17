def get_ticket_price(age, is_student):
    if age <0 or age >120:
        return "Invalid Entry"
    elif age < 12 :
        cost= 8
    elif  age >=65:
        cost = 10
    else :
        if  is_student== True:
            cost = 12
        else:
            cost= 15
    return  cost        
        

age= int(input("Enter your AGE :"))
Is=0
if age >= 12 and age <=64:
        stu= input("Are you a Student (Y/N):")
        if stu in 'Yy':
            Is= True
        elif stu in 'Nn':
            Is= False
print("The Ticket price to be paid: $", get_ticket_price(age, Is))        
    
