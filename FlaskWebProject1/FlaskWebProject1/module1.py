
def Distance(word1 , word2):
    matrix = [[0 for x in range(len(word2)+1)] for x in range(len(word1)+1)]
    index =1
    for i in word2:
        matrix[0][index]=index
        index+=1
    index=1
    for i in word1:
        matrix[index][0]=index
        index+=1

    for row in range(1,len(word1)+1):
        for col in range(1,len(word2)+1):
            if(matrix[row-1][col]>matrix[row][col-1]):
                if(matrix[row-1][col-1]>matrix[row][col-1]):
                    matrix[row][col]=matrix[row][col-1]+1
                elif(word2[col-1]==word1[row-1]):
                    matrix[row][col]=matrix[row-1][col-1]
                else:
                    matrix[row][col]=matrix[row-1][col-1]+1
            else:
                if(matrix[row-1][col-1]>matrix[row-1][col]):
                    matrix[row][col]=matrix[row-1][col]+1
                elif(word2[col-1]==word1[row-1]):
                    matrix[row][col]=matrix[row-1][col-1]
                else:
                    matrix[row][col]=matrix[row-1][col-1]+1

    return matrix

def Printer(str1,str2,m):
    l = []
    numval =0
    row=0
    col=0
    answer = str1
    index =0
    str1len = len(str1)
    str2len = len(str2)
    while(row+1<=str1len or col+1<=str2len):
        
        if(row+1<=str1len and col+1<=str2len):

            if(m[row+1][col+1]<=m[row][col+1]):
                if(m[row+1][col+1]<=m[row+1][col]):
                    answer = answer[0:index]+str2[col]+answer[index+1:]

                    index+=1
                    row+=1
                    col+=1
                else:
                    answer = answer[0:index]+answer[index+1:]

                    row+=1
            elif(m[row][col+1]<=m[row+1][col]):
                answer = answer[0:index]+str2[col]+answer[index:]
                index+=1
                col+=1
            else:
                answer = answer[0:index]+answer[index+1:]

                row+=1
        elif(row+1>str1len):
            answer = answer[0:index]+str2[col]+answer[index:]
            index +=1
            col+=1
        else:
            answer = answer[0:index]+answer[index+1:]
            row+=1

        numval=m[row][col]
        if(row+1<=str1len and col+1 <=str2len):
            if(numval==m[row+1][col+1] or numval==m[row+1][col]  or numval==m[row][col+1]):
                continue
        elif(row+1>str1len and col+1<str2len):
            if(numval==m[row][col+1]):
                continue
        elif (col+1>str2len and row+1<str1len):
            if(numval==m[row+1][col]):
                continue

        l.append(answer)
    return (l)