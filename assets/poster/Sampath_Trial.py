def cycle(level,n):
	while(checker(level,n)==1):
		for levels in level:
			#print(level)
			if levels < n:
				k=level.index(levels)
			#	print(maxxer(level,n),2*(k+1))
				level[level.index(levels)]=maxxer(level,n)+(2*(k+1))
		for levels in level:		
			if(levels==n):
			#	print(level)
			#	print(levels)
				return level.index(levels)
	return -1

def checker(level,n):
	for levels in level:
		if(levels<n):
			return 1
	return 0
def maxxer(level,n):
	high=level[0]
	for levels in level:
		if(levels>high and levels<=n):
			high=levels
	#print("Max is " + str(high))
	return high

if __name__=="__main__":
	n=int(input())
	while(n>0):
		
		k=int(input())
		n=int(input())
		names=input().split()
		level=[]
		i=1
		for men in names:
			level.append(i)
			i+=1
#		if(n<=i+1):
#			print(names[])
		o=cycle(level,n)
		if(o==-1):
			print("Kill Bill")
		else:
			print(names[o])
		n-=1
