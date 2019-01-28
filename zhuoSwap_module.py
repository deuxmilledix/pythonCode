# Define my swap function in zhuoSwap_module.py
def zhuoSwap(table, i, j):
	temp = table[i]
	table[i] = table[j]
	table[j] = temp
	return table
