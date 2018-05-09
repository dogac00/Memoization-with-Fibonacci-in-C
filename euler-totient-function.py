def gcd(n, m):
  result = 1

  for i in range(1, min(n,m)+1):    # for 1 to min of two numbers
    if(n % i == 0 and m % i == 0):  # if both are divisible by i
      result = i                    # greatest divisor is result
  
  return result
  
def euler(n):
  count = 0
  for i in range(1,n+1):    # for 1 to n
    if(gcd(n,i) == 1):      # if gcd is 1
      count += 1            # increment the count by 1
  
  return count
  
print(euler(int(input())))
