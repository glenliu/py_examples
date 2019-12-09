# encoding=utf-8

result=0

for i in range(1,2019):
	result += 1/(i*(i+1))
	print("+ 1/"+str(i)+"*"+str(i+1))
	
print(result)

print(result*2019)

