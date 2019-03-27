import numpy as np

def extractfloor(mat, floor, max_floor):
	'''This function will extract one floor from the given structure
		and return a matrix in form of 1 and i '''

	row, col = mat.shape
	y = np.zeros(mat.shape)
	for r in range(row):
		for c in range(col):
			if mat[r][c] >= floor:
				y[r][c] = 1					# 1 denotes that a block is present at this position in the given floor
			else:
				y[r][c] = max_floor + 10	# (max_floor+10) is a value quite big which denotes the empty space to check
	return y

def count_i(mat, max_floor):
	#This function counts the total no. of empty location in the given floor
	row, col = mat.shape
	count = 0
	for r in range(row):
		for c in range(col):
			if mat[r][c] == (max_floor + 10):
				count += 1
	return count

def fall(mat, org, max_floor):
	'''The function checks if water can stay in the empty location or not
		and return the matrix where 0 denotes the position where water can't stay'''
	row, col = mat.shape
	for r in range(row):
		for c in range(col):
			#look for empty location
			if mat[r][c] == (max_floor + 10):
				#check boundary condition, water can't stay at this position
				if r == 0 or r == row-1 or c == 0 or c == col-1:
					mat[r][c] = 0
				elif mat[r-1][c] == 0 or mat[r+1][c] == 0 or mat[r][c-1] == 0 or mat[r][c+1] == 0 or org[r][c] == 0:
					#check west, east, south, north and bottom position, if any of these is empty, water can't stay
					mat[r][c] = 0
	return mat

def modify(mat, org, floorno, max_floor):
	'''this function modifies the original (denoted as 'org') matrix for checking of next floor
	'''
	row, col = mat.shape
	for r in range(row):
		for c in range(col):
			#check boundary condition
			if mat[r][c] == (max_floor + 10):
				org[r][c] = floorno
			if mat[r][c] == 0:
				org[r][c] = 0
	return org