temp = []

for i in range(1,101):
	temp.append(i**2)
	
print((sum(range(1,101))**2)-sum(temp))