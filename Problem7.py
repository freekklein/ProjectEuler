prime = []
prime.append(2)

n = 101

for i in range(3,10000):
	if len([c for c in range(2,i) if i % c]) == len(range(2,i)):
		prime.append(i)
		
print(prime[n-1])