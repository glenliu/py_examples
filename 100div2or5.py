# 1到100 这些正整数中，不能被2或5整除的数的个数
result=0
for i in range (1,101):
	print(i)
	if i%2 != 0 and i % 5 != 0:
		print("caught one!")
		result+=1
print("Result is: "+str(result))