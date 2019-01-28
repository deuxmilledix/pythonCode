import os
import zhuoSwap_module
os.system('clear')

# Bubble Sort

sortable = [14,5,1,4,2,12,8,10,3,9,0,11,7,6,13,15]

n = len(sortable)
temp = 0

for j in range(1, n):
	for i in range(0, n-j):
		#print("%s %s" % (sortable[i], sortable[i+1]))
		if(sortable[i] > sortable[i+1]):
			sortable = zhuoSwap_module.zhuoSwap(sortable, i, i+1)

print (sortable)
