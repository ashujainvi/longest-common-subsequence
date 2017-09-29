# def xrange(x):
# 	return iter(range(x))


def lcs(X,Y, m, n, output_filepath):
	#assign 0 to the intial values of X and Y
	lengths = [[0 for i in xrange(n+1)] for i in xrange(m+1)]

	#check for the range of X and Y 
	for i in xrange(n+1):
		for j in xrange(m+1):
			if i == 0 or j == 0 :
				lengths[i][j] = 0
			elif X[i-1] == Y[j-1]:
				lengths[i][j] = lengths[i-1][j-1] + 1
			else :
				lengths[i][j] = max(lengths[i-1][j], lengths[i][j-1])
	L = lengths[i][j]

	#for storing the value of LCS, we create a lcs array
	lcs = [""] * (L)

	while m != 0 and n != 0:
		#if both index value of X and Y are equal
		if X[m-1] == Y[n-1]:
			lcs[L-1] = X[m-1]
			m -= 1
			n -= 1
			L -= 1
		#if both vlaues are not equal then check for larger one
		#and move in that direction
		elif lengths[m-1][n] > lengths[m][n-1]:
			m -= 1
		else :
			n -= 1
	length = len(lcs)
	write_output(length, lcs, output_filepath)


def take_input(filepath):
	data = open(filepath).read().split("\n")
	for i in data:
		A = data[0]
		B = data[1]
	return A, B

def write_output(length, lcs, output_filepath):
	result = ''
	for i in lcs:
		result = result+ i
	with open(output_filepath,'w') as output:
		output.write(str(length)+"\n"+str(result))


if __name__ == '__main__':
	X, Y = take_input("input.txt")
	m = len(X)
	n = len(Y)
	lcs(X, Y, m, n, "output.txt")