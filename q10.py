import sys
def organize_scores(scores,descending):
    n_list=[]   
    if descending == True:
        n_list= sorted(scores, reverse= True)
    else:
        n_list= sorted(scores)
    return n_list            
Slst = []
n= int(input("No of Scores:"))
if n==0:
        print("List is Empty...")
elif n> 5000:
    print("List Limit Exceeded")
    sys.exit()
else:
    for k in range (0,n):
        inp= int(input(f"Enter the score {k}:"))
        Slst.append(inp)
des = input(" Enter 'D' for Descending order & 'A' for Ascending order:")
d=None
if des in 'Dd':
         d= True
elif des in 'Aa':
         d= False
print("New sorted list of Integers:", organize_scores(Slst, d))  
    
