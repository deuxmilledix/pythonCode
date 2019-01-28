import zhuoSwap_module
# define the function module partition
def partition(Table, lo, hi):
	p = int((lo+hi)/2)
	pivot = Table[p]        
	i = lo - 1
	j = hi + 1

	while (i < hi and j > 0):
		while(True):
			i += 1
			if(Table[i] >= pivot):
				break
		while(True):
			j -= 1
			if(Table[j] <= pivot):
				break
		if(i >= j):
			return j
		Table = zhuoSwap_module.zhuoSwap(Table, i, j) #swap 
