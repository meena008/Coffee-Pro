#ITERATIVE CONTROL
#FOR LOOP
for x in "meena":             #type:1(for) it's only accepted in string
    print(x)

for x in range(10):           #type:2 range set
    print(x)

for x in range(1,5):          #type:3 1->start value,5->end value
    print(x)

for x in range(1,10,2):       #type:4 2->skip value
    print(x)


#WHILE LOOP
while(0):                     #type:1(infinite loop) ctrl+c->stop loop
    print("meena")
a=1
while a<=10:                  #type:2(finite loop)
    print(a)
    a+=1


#LOOPING CONTROL
for val in "meena":          #type:1(break)
    if val=='n':
        break
    print(val)

for val in "meena":          #type:2(continue)
    if val=='n':
        continue
    print(val)

for val in "meena":          #type:3(pass)
        pass
print(val)


