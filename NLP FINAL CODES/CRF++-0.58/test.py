f=open("final")

count1=0
count2=0

for line in f:
	if line!='\n':
		temp=line.split('\t')
		print temp
		if temp[3][0]=='B':
			count1=count1+1
		if temp[2][0]=='B':
			count2=count2+1

print count1,count2
