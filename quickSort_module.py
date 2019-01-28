import quickSortPartition_module
# define the module function quicksort 
def quicksort(Table, lo, hi):
	if(lo < hi):
		p = quickSortPartition_module.partition(Table, lo, hi) 
		quicksort(Table, lo, p)      
		quicksort(Table, p+1, hi)    
	return Table
