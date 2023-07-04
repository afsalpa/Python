class ZigZagConversion:

    def findZigZagConversion(s, rows):
        indx = 0
        step=0
        tab = [[] for r in range(rows)]
        for char in s:
            tab[indx].append(char)
            if rows == 1: # in case of only one row then you don't need to go up or down 
                step = 0            
            elif indx == 0:
                step = 1 # adding pointer to go down in the table
            elif indx == rows - 1:
                step = -1 # adding pointer to go up in the table
            indx += step

        for i in range(rows):
            tab[i] = "".join(tab[i])
        resp = "".join(tab)
        return resp
        


    #print(findZigZagConversion("PAYPALISHIRING",4))

    #print(findZigZagConversion("PAYPALISHIRING",3))

    print(findZigZagConversion("ABC",1))