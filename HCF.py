while True:
	num1 = int(input("Enter the First number:\n"))
	num2 = int(input("Enter the Second number:\n"))

	mn = min(num2, num1)
	for i in range(1, mn+1):
		if num1%i==0 and num2%i==0:
			hcf = i

	print(f"The HCF of these two numbers is {hcf}")