N = int(input())
M = int(input())

def nBonacci(N, M):
  nBonacci = []
  for i in range(N-1):
    nBonacci.append(0) # initilize with zeros

  nBonacci.append(1) # Nth element is 1

  for i in range(N,M):                    # starting from N to M
    nBonacci.append(sum(nBonacci[i-N:i])) # append the sum of subarray to nBonnaci
  
  return nBonacci
  
print(nBonacci(N,M))
