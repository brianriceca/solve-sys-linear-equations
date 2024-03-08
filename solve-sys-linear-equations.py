#!/usr/bin/env python3

import sys
import copy

def determinant(A):
  det = 1
  for i in range(len(A)):
    det *= A[i][i]
  return det

matrix = [ [ 2, 1, -1, 5],
           [ 1, -3, 2, -1],
           [ -1, 2, 1, 4] ]

#matrix = [ [ 1, 2, 6],
#           [ -1, 4, -4 ] ]

if (determinant(matrix) == 0):
  print("I don't know how to reshuffle rows yet")
  sys.exit(1)

nrows = len(matrix)
ncols = len(matrix) + 1

for i in range(nrows):
  if (len(matrix[i]) != ncols):
    print("This doesn't look like a system of N eqs in N unknowns")
    sys.exit(2)

print(matrix)

try:
  import numpy as np
except Exception:
  pass
else:
  print("------first the easy way-------")
  A = copy.deepcopy(matrix)
  b = []
  for row in range(len(A)):
    b.append(A[row][ncols-1])
    del A[row][ncols-1]
  
  print(f"A is {A}")
  print(f"b is {b}")
     
  A = np.array(A)
  b = np.array(b)
  print(np.linalg.solve(A,b))

print("------now for the hard way-------")

print(f"matrix is {matrix}")
newmatrix = copy.deepcopy(matrix)
for pivot in range(len(matrix)-1):
  print(f"I have to pivot on matrix[{pivot}][{pivot}] = {matrix[pivot][pivot]}")
  for row in range(pivot+1,len(matrix)):
    print(f"Let's mess with row {row}")
    print(f"...I hate this {matrix[row][pivot]} in matrix[{row}][{pivot}]")
    gottamultiplyby = matrix[row][pivot] / matrix[pivot][pivot]
    print(f"...To get rid of it I have to subtract {gottamultiplyby} copies of {matrix[pivot]}")
    for col in range(pivot,ncols):
      newmatrix[row][col] = ( matrix[row][col] 
                              - 
                              gottamultiplyby * matrix[pivot][col] )
  print(f"resulting matrix is {newmatrix}")
  matrix = copy.deepcopy(newmatrix)

print("---now to do the backsubstitution---")

answervec = [0] * nrows

for row in range(nrows-1,-1,-1):

  pivotcol = row # just to be super clear

  # first thing to do is to accumulate the one row from b we need 

  partialsum = matrix[row][ncols-1]

  # ...and all the -1*weighted columns to the right of us (if any)

  for col in range(pivotcol+1,ncols-1):
    partialsum -= matrix[row][col] * answervec[col]

  # then we divide by the weight on this column
  answervec[row] = partialsum / matrix[pivotcol][row]

print(f'answervec is {answervec}')
