def generate_three(start,end):
    l=[]
    for k in range (start,end,3):
        l.append(k)
    return l    
s= int(input("Enter the starting no :"))
e= int(input("Enter the ending no:"))
if -1000<= s and e <= 1000:
    print("skip by 3:", generate_three(s,e))
else:
    print("Limit Exceeded!!")
