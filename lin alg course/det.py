# put your python code here
#f = open('input.txt', 'r')
#n = int(f.readline())
n = int(input())
matrix = []
for i in range(n):
    #matrix.append(list(map(float, f.readline().split())))
    matrix.append(list(map(float, input().split())))
#print(matrix)

def get_det(i):
    sign=1
    if i == n-1:
        return matrix[i][i]

    tmp_id = i
    while tmp_id<n:
        if matrix[tmp_id][i] != 0:
            break
        tmp_id+=1
    if tmp_id==n:
        return 0
    if tmp_id != i:
        tmp_str = matrix[tmp_id]
        matrix[tmp_id] = matrix[i]
        matrix[i] = tmp_str
        sign = -1
    #print('matrix', matrix)
    for tmp_id in range(i+1,n):
        #print('tmp_id', tmp_id, matrix[i][i], matrix[tmp_id][i])
        mul = matrix[tmp_id][i] / matrix[i][i]
        #print(tmp_id, 'mul', mul)
        for j in range(i,n):
            matrix[tmp_id][j] -= mul*matrix[i][j]

    #print(matrix)
    return sign*matrix[i][i]*get_det(i+1)

res = get_det(0)
print(round(res))
