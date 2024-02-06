def determinant(matrix):
	if len(matrix)!=2 or len(matrix[1])!=2:
		raise ValueError("Input matrix must be a 2*2 matrix")
	return matrix[0][0]*matrix[1][1]-matrix[0][1]
matrix_2=[[3,4],[3,4]]
result=determinant(matrix_2)
print("Determinant od 2*2 matrix",result)
