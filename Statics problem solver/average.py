num = int(input("How many numbers? : "))
total_sum = 0

for _ in range(num):
	numbers = float(input("Enter the numbers"))
	total_sum += numbers

avg = total_sum / num

print("Average is :", avg)