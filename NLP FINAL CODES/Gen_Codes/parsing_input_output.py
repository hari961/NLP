f=open("example")

string=''
count=0
for line in f:
	if '((' in line:
		temp=line.split('\t')
		temp=temp[2]
		temp=temp.split('\n')
		temp=temp[0]
		phrase=temp
		count=0
	elif '))' in line:
		count=0
	else:
		if '/Sentence' in line:
		        string=string+'\n'
		elif 'id' in line:
			count=0
		else:
			if line != '\n':
				temp=line.split('\t')
				t1=temp[2].split('\n')
				if count==0:
					k='B-'
				else:
					k='I-'
				string = string + temp[1] + ' ' + t1[0] + ' ' + k + phrase + '\n'
			        count=count+1
	
print string

		

