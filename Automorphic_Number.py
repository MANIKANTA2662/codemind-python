num=int(input())
num_of_digits=len(str(num))
sqr=num**2
last_digit=sqr%pow(10,num_of_digits)
if last_digit==num:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")