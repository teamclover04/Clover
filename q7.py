def  count_inventory(fruit_list):
    dic={}
    if x==0 :
        print("Fruits are out of season...")
    else:
        for k in  fruit_list:
            if k  in dic:
                 dic[k]+=1
            else:
                   dic[k] =1
        
    return dic   
        
fl=[]
x= int(input("Enter no of Fruit varieties:"))
if x<= 1000:
    for k in range(0,x):
         l= input("Enter the fruit name :")
         fl.append(l)
else:
    print("List is Limited to 1000")
print("Fruits data :",count_inventory(fl))   
    
    
