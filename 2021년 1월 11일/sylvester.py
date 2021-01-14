#AX = XB의 형태의 Matrix 방정식을 실베스터 방정식이라고 한다. 다만, 이는 현재, 존재하는 Method가 없어, 직접 제작
import numpy as np
import math

def syl(A, B):
    D = np.zeros((12, 12))
    D[0][0] = A[0][0] - B[0][0]
    D[0][1] = -B[1][0]
    D[0][2] = -B[2][0]
    D[0][3] = -B[3][0]
    D[0][4] = A[0][1]
    D[0][8] = A[0][2]

    D[1][0] = -B[0][1]
    D[1][1] = A[0][0] - B[1][1]
    D[1][2] = -B[2][1]
    D[1][3] = -B[3][1]
    D[1][5] = A[0][1]
    D[1][9] = A[0][2]

    D[2][0] = -B[0][2]
    D[2][1] = -B[1][2]
    D[2][2] = A[0][0] - B[2][2]
    D[2][3] = A[0][0] - B[3][3]
    D[2][6] = A[0][1]
    D[2][10]= A[0][2]

    D[3][0] = -B[0][3]
    D[3][1] = -B[1][3]
    D[3][2] = -B[2][3]
    D[3][3] = A[0][0] - B[3][3]
    D[3][7] = A[0][1]
    D[3][11] = A[0][2]

    D[4][0] = A[1][0]
    D[4][4] = A[1][1] - B[0][0]
    D[4][5] = -B[1][0]
    D[4][6] = -B[2][0]
    D[4][7] = -B[3][0]
    D[4][8] = A[1][2]

    D[5][1] = A[1][0]
    D[5][4] = -B[0][1]
    D[5][5] = A[1][1] - B[1][1]
    D[5][6] = -B[2][1]
    D[5][7] = -B[3][1]
    D[5][9] = A[1][2]

    D[6][2] = A[1][0]
    D[6][4] = -B[0][2]
    D[6][5] = -B[1][2]
    D[6][6] = A[1][1] - B[2][2]
    D[6][7] = -B[3][2]
    D[6][10] = A[1][2]

    D[7][3] = A[1][0]
    D[7][4] = -B[0][3]
    D[7][5] = -B[1][3]
    D[7][6] = -B[2][3]
    D[7][7] = A[1][1] - B[3][3]
    D[7][11] = A[1][2]

    D[8][0] = A[2][0]
    D[8][4] = A[2][1]
    D[8][8] = A[2][2] - B[0][0]
    D[8][9] = -B[1][0]
    D[8][10] = -B[2][0]
    D[8][11] = -B[3][0]

    D[9][1] = A[2][0]
    D[9][5] = A[2][1]
    D[9][8] = -B[0][1]
    D[9][9] = A[2][2] - B[1][1]
    D[9][10] = -B[2][1]
    D[9][11] = -B[3][1]

    D[10][2] = A[2][0]
    D[10][6] = A[2][1]
    D[10][8] = -B[0][2]
    D[10][9] = -B[1][2]
    D[10][10] = A[0][0] - B[2][2]
    D[10][11] = -B[3][2]

    D[11][3] = A[2][0]
    D[11][7] = A[2][1]
    D[11][8] = -B[0][3]
    D[11][9] = -B[1][3]
    D[11][10] = -B[2][3]
    D[11][11] = A[0][0] - B[3][3]

    return D

if __name__ == "__main__":
    A = [[0, 1, 2, 3],
         [4, 5, 6, 7],
         [8, 9, 10, 11], 
         [12, 13, 14, 15]]
    
    print(syl(A, B))

