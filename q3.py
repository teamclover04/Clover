def average_passing_grades(grades):
    c=0
    s=0
    for k in grades:
        if k>=0 and k<=100:
            if  k >=50:
                c= c+1
                s=s+k
            
    if  (c==0):
                return 0.0     
    avg= s/c         
    return  float(avg)
grades= list(map(int,input("Enter the list of grades :").split()))
if  len(grades) <=1000:
    print("The Average of grades above 50:",average_passing_grades(grades))

else:
    print("List EXCEEDING...")
             
