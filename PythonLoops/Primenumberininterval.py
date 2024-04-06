# Python program to print all prime number in an interval
def is_prime(num):
#"""This function checks if a number is prime. Args: num: The number to check. Returns:True if the number is prime, False otherwise."""
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

print("Prime numbers between", lower, "and", upper, "are:")
# Find prime numbers in the given range
for num in range(lower, upper + 1):
  if is_prime(num):
    print(num)
        