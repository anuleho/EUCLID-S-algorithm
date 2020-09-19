nu1 = input ("First no: ")
nu2 = input ("second no: ")
nu1 = int(nu1)
nu2 = int(nu2)
def gcd( nu1 , nu2 ):
 if nu1 == 0 :
  return nu2
 return gcd(nu2%nu1 , nu1)
print (gcd(nu1 , nu2)) 

