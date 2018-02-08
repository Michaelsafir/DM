chislo = str(input())
result = 0
count = len(chislo)
chislo = int(chislo)

for x in range(count):
	result += chislo%10
	chislo = chislo / 10 

print(result)
