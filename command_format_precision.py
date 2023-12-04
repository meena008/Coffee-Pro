#COMMANDS
'''
      PROJECT:SOFTWARE
      NAME:MEENA                     #multiline command using trible quotes from starting to ending
      UPDATE:12.1.98   '''
print(__doc__)


#FORMATTING
a=0x0E       #input formating
print(a)
a="meena"
print(a)
a=0b0011  #binary value
print(a)
a=0o17     #octal value
print(a)

a=10        #output formatting
b=20
print("A value %d and b value %d "%(a,b))   #decimal
print("A value %f and b value %f "%(a,b))   #float
print("A value %X and b value %x " %(a,b))   #hex

#FORMAT OPERATOR FOR ANT DATATYpe
a="gomathi"     #int,string,float any datatype accepted
b="meenu"
print("A value{} b value{}".format(a,b))
print("A value{0} b value{1}".format(a,b))
print("A value{1} b value{0}".format(a,b))

#PRECISION SET
x=1/3
print("x=%f"%(x))
print("x=%.2f"%(x))
print("x=%.3f"%(x))
