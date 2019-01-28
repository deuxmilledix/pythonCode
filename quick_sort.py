import os
import quickSort_module	
os.system('clear')

     

# quick sort algorithm

sourceTable = [10,7,12,9,5,14,2,6,13,15,0,8,11,3,1,4]
n = len(sourceTable)				      
							
sortedTable = quickSort_module.quicksort(sourceTable, 0, n-1)   

print (sortedTable)				
