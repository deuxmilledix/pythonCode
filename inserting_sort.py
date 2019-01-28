import os
import zhuoSwap_module
os.system('clear')

sortable = [10,7,12,9,5,14,2,6,13,15,0,8,11,3,1,4]
n = len(sortable)

for i in range(0, n):
	for j in range(i, 0, -1):
		if (sortable[j-1]>sortable[j]):
			sortable = zhuoSwap_module.zhuoSwap(sortable, j-1, j) #swap

print (sortable)
