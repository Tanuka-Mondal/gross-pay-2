#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.

hrs = input("Enter Hours:")
h = float(hrs)
xx = input("Enter the Rate:")
x = float(xx)
if h <= 40:
 	print( h  * x)
elif h > 40:
	print(40* x + (h-40)*1.5*x)
