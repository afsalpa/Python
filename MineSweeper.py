# mine_sweeper([[0, 2], [2, 0]], 3, 3) should return:
# [[0, 1, -1],
#  [1, 2, 1],
#  [-1, 1, 0]]


class MineSweeper:

    def findMineSweeper(l : list[list[int]] , r, c):
        print(l)
        print(r)
        print(c)
        
        result = [ [0 for x in range(c)] for j in range(r)]
        print(result)

        def updateResult(u):
            uR = u[0]
            uC = u[1]
            if result[uR][uC] != -1:
                result[uR][uC] +=1
    

        for x in range(len(l)):
            b = l[x]
            bRow = b[0]
            bCol = b[1]
            result[bRow][bCol] = -1
            print(bRow, bCol)

            # update same row right
            updateSameRowRight = lambda row, col : [row, col+1] if col + 1 < c else None
            uSameRowRight = updateSameRowRight(bRow, bCol)
            print("uSameRowRight",uSameRowRight)
            if (uSameRowRight):
                updateResult(uSameRowRight)

            # update same row left
            updateSameRowLeft = lambda row, col : [row, col-1] if col - 1 > -1 else None
            uSameRowLeft = updateSameRowLeft(bRow, bCol)
            print("uSameRowLeft",uSameRowLeft)
            if (uSameRowLeft):
                updateResult(uSameRowLeft)

            # update upper row same column
            updateUpperRowSameCol = lambda row, col : [row-1, col] if row - 1 > -1 else None
            uUpperRowsame = updateUpperRowSameCol(bRow, bCol)
            print("uUpperRowsame",uUpperRowsame)
            if (uUpperRowsame):
                updateResult(uUpperRowsame)
            
            #update upper row left column
            updateUpperRowLeftCol = lambda row, col : [row-1, col-1] if row - 1 > -1 and col-1 > 0 else None
            uUpperRowLeftCol = updateUpperRowLeftCol(bRow, bCol)
            print("uUpperRowLeftCol",uUpperRowLeftCol)
            if (uUpperRowLeftCol):
                updateResult(uUpperRowLeftCol)

            # update upper row right column
            updateUpperRowRightCol = lambda row, col : [row-1, col+1] if row - 1 > -1 and col+1 < c else None
            uUpperRowRightCol = updateUpperRowRightCol(bRow, bCol)
            print("uUpperRowRightCol",uUpperRowRightCol)
            if (uUpperRowRightCol):
                updateResult(uUpperRowRightCol)

            #update lower row same column
            updateLowerRowSameCol = lambda row, col : [row+1, col] if row + 1 < r and col < c else None
            uLowerRowSameCol = updateLowerRowSameCol(bRow, bCol)
            print("uLowerRowSameCol",uLowerRowSameCol)
            if (uLowerRowSameCol):
                updateResult(uLowerRowSameCol)

            #update lower row left column
            updateLowerRowLeftCol = lambda row, col : [row+1, col-1] if row + 1 < r and col-1 > -1 else None
            uLowerRowLeftCol = updateLowerRowLeftCol(bRow, bCol)
            print("uLowerRowLeftCol",uLowerRowLeftCol)
            if (uLowerRowLeftCol):
                updateResult(uLowerRowLeftCol)

            #update lower row right column
            updateLowerRowRightCol = lambda row, col : [row+1, col+1] if row + 1 < r and col+1 < c  else None
            uLowerRowRightCol = updateLowerRowRightCol(bRow, bCol)
            print("uLowerRowRightCol",uLowerRowRightCol)
            if (uLowerRowRightCol):
                updateResult(uLowerRowRightCol)
        return result

    #res = findMineSweeper([[0, 2], [2, 0]], 3, 3)
    res = findMineSweeper([[0, 0], [0, 1]], 3, 4)
    for x in res:
        print(x)
    print(res)
