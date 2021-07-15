def initialiseAllNonZeroCoords(tfidfVectors):
# This function just exists since it seems to be expensive and I'd rather not call it multiple times
# Hence it is intended to be called outside of loops in order to simplify the row specific processing
	values=[]
	nzc=zip(*tfidfVectors.nonzero())

	# In Python 3 the zip can only be iterated through one time before it is automatically released
	# So need to copy the results otherwise the main loop below will no longer work
	pointList=[]
	for i,j in nzc:
		pointList.append([i,j])

	for row in range(tfidfVectors.shape[0]):
		rowList=[]
		for i,j in pointList:
			if row==i:
				rowList.append(j)
		values.append(rowList)

	return values