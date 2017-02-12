def diaginal_reverse(matrix):

   print("Normal",(matrix))

   matrix = zip(*matrix)

   print("Reversed", *matrix)

diaginal_reverse (matrix =[[1, 2, 3],[4, 5, 6], [7, 8, 9]])