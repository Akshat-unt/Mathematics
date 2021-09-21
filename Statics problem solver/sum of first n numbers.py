a = int(input("First term : "))
n = int(input("Upto which term : "))
d = int(input("Common Difference : "))

sn = n/2*[2*a + (n-1)*d]
print(f"Sum of first n numbers is: {sn}")