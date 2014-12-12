f=open("final1")
string=''
count=0
for line in f:
	if line!='\n':
		temp=line.split('\t')
		if temp[2][0]=='B':
			if count!=0:
				string=string+']'+' '
			string = string + '['+temp[0]
			count=count+1
		elif temp[2][0]=='I':
			string = string + ' ' + temp[0]
	elif line=='\n':
		string = string + ']'+'\n'
		count=0
	
print string

