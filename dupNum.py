num=0
for i in range(100,1000,1): 
	g=str(i)[2] 
	s=str(i)[1] 
	b=str(i)[0]
	print("i="+str(i)+"\tb="+b+"\ts="+s+"\tg="+g)
	if (b==s or b==g or s==g):
		print(str(i))
		num=num+1
		print("num="+str(num))


	

