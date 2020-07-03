def max():
	 a=int(input("enter num1:"))
	 b=int(input("enter num2:")) 
	 c=int(input("enter num3:")) 
	 if a==b==c:
	 	 print("all are equal..no maximum number")
	 elif (a>b and a>c):
	 	print("max no is :",a)
	 elif (b>c and b>a):
	 	print("max no is :",b)
	 else:
	 	print("max no is:",c)
max()