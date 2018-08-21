a = [[1, 2], [3, 4, 5]]
b = [[5, 6], [7, 8, 9]]

result = [[0, 0, 0], [0, 0, 0]]


def matmul(a, b):
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]


matmul(a, b)
print(result)