f=open("final-fr","r")
array=[]
string=''
for line in f:
	flag=0
	if line != '\n':
		a=line.split("\t")
		a1=a[5].split('\n')
		string=string+a[0]+' '+a[3]+' '+a[4]+' '+a1[0]+'\n'
	else:
		string=string+'\n'
print string
