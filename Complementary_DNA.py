
def ComplementaryDNA(string):
	"""
	with open(file_path, 'r') as file:
		string = file.read()
	"""

	compl = ''
	nuc_dict = {
		'A' : 'T',
		'C' : 'G',
		'G' : 'C',
		'T' : 'A'
		}
	for nuc in reversed(string):
		if nuc == '\n':
			pass
		else:
			compl += nuc_dict[nuc]

	return compl

if __name__ == '__main__':
	file_path = "rosalind_revc.txt"
	print(ComplementaryDNA(file_path))