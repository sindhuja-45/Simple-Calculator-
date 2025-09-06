# calculator.py
def add(x,y): return x+y
def sub(x,y): return x-y
def mul(x,y): return x*y
def div(x,y): return "Error: / by zero" if y==0 else x/y

if __name__=="__main__":
    op=input("Enter + - * /: ")
    a=float(input("num1: ")); b=float(input("num2: "))
    func = {"+":add, "-":sub, "*":mul, "/":div}.get(op)
    if func is None:
        print("Invalid operator")
    else:
        print("Result:", func(a,b))
