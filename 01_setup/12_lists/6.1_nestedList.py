matrix = [
    [1, 3, 6],
    [2, 4, 5],
    [7, 8, 9]
]

# Transpose the matrix
transposeMatrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print("Original Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transposeMatrix:
    print(row)

#the method below is not working because the matrix is not initialized and cannot be initialized in much easier way
# transpose = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         transpose[j][i]=matrix[i][j]