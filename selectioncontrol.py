#CONTROL STATEMENTS
#SELECTOIN CONTROL
a=eval(input("Enter A"))                         #type:1(if)
b=eval(input("Enter B"))
if(a<b):
    print("greater than value")


a=eval(input("Enter A"))                    
b=eval(input("Enter B"))                          #type:2(ifelse)
if(a<b):
    print(" B Less than value")
else:
    print("A Greater than value")



a=eval(input("Enter A"))                        #type:3(elseif(0r)elif)     
b=eval(input("Enter B"))
if(a<b):
    print("B greater than")
elif(a>b):
    print("A greater than")
elif(a==b):
    print("A and B equal")
else:
    print("nothing")


num=int(input("Enter number"))                  #type:4(Nested ifelse)
if(num>=0):
    if(num==0):
        print("Neutral Number")
    else:
        print("positive Number")
else:
    print("Negative Number")

