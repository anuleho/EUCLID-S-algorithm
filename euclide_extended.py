a1= input ( "first integer: ")
b1 = input ("sercond integer: ")
a = int(a1)
b = int(b1)
def gcde( a, b):
 if a == 0 :
   return b,0,1
 gcd , x , y = gcde(b%a , a)
 X = y - (b//a)*x
 Y = x
 return gcd,X,Y
g , X , Y = gcde(a,b)
print (g)

