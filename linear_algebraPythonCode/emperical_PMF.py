f = open('inputfile_16.txt','r')
m=f.read()
emp = []
for i in range(26):
	emp.append(0)
for x in int(m):
	z=ord(x)
	if 65<=z<=90:
		z=z+32
		
	if 97<=z<=122:
		emp[z-97]+=1/m

print(emp)

