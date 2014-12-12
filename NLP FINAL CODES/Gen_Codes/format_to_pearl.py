f=open("final1","r")
array=[]
string=''
for line in f:
	flag=0
	if line != '\n':
		array=line.split("\t")
		for i in array:
			string=string+' '+i

		array=[]
print string
