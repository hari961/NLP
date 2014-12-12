f=open("rule")
out=f.readlines()

k=open("gold")
inp=k.readlines()

l=len(inp)

count=0
count1=0

for i in range(0,l):
	t1=inp[i]
	t1=t1.split('[')
	t2=out[i]
	t2=t2.split('[')

	k1=len(t1)
	k2=len(t2)
	
	count1+=k2


	for j in range(0,k1):
		for l in range(0,k2):
			if t1[j]==t2[l]:
				count+=1

print count , count1
