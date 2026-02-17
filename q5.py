def caluculate (expression):
    expression = expression.replace(" ", "")
    tk = []
    num = ""
    
    for k in expression:
        if k in '()':
            return "Paranthesis is not allowed"
        elif  k.isdigit() or k == '.':
            num += k
        else:
            if num:
                tk.append(float(num))
                num = ""
            tk.append(k)
    
    if num:
        tk.append(float(num))

    stk = []
    i = 0
    while i < len(tk):
        if tk[i] == '*':
            stk[-1] *= tk[i+1]
            i += 2
        elif tk[i] == '/':
            if tk[i+1] !=0:
                stk[-1] /= tk[i+1]
                i += 2
            else:
                print ("Division by zero is not allowed")
                return
        else:
            stk.append(tk[i])
            i += 1
    result = stk[0]
    i = 1
    while i < len(stk):
        if stk[i] == '+':
            result += stk[i+1]
        elif stk[i] == '-':
            result -= stk[i+1]
        i += 2

    return round(result, 2)
exp= input("Enter the Required Expression:")
if not exp.replace(" ", "").replace(".", "").replace("+","").replace("-","").replace("*","").replace("/","").isdigit():
    print("Invalid Expression")
else:
    print("Result:", caluculate(exp))
