'''
1
12
123
1234
12345
'''
'''for row in range(1, 5 + 1):
    for col in range(1, row + 1):
        print(col, end='')
    print()
'''
'''
1               1 
  2           2   
    3       3     
      4   4       
        5         
      6   6       
    7       7     
  8           8   
9               9 
'''
'''n=9
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+ col==n+1 or row == col:
            print(row,end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''
1               1 
  2           2   
    3       3     
      4   4       
        5         
      4   4       
    3       3     
  2           2   
1               1 
'''
'''n=9
m=1
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+ col==n+1 or row == col:
            print(m,end=' ')

        else:
            print(' ',end=' ')
    if row < (n+1)//2:
        m += 1
    else:
        m-=1
    print()'''
'''
                * 
              * * 
            * * * 
          * * * * 
        * * * * * 
      * * * * * * 
    * * * * * * * 
  * * * * * * * * 
* * * * * * * * * 
'''
'''n = 9
for row in range(1, n + 1):
    for col in range(1, n + 1):
        if row + col >= n + 1:
            print('*', end=' ')

        else:
            print(' ', end=' ')
    print()'''
'''
    A 
   B B 
  C C C 
 D D D D 
E E E E E
'''

'''n=5
char=ord('A')
space=n-1
for row in range(1,n+1):
    for col in range(1,space+1):
        print(end=' ')
    space-=1
    for col in range(1,row+1):
        print(chr(char),end=' ')
    char+=1
    print()'''

'''

'''
'''n = 5
char = ord('A')
low = ord('a')
space = 1
for row in range(n, 0, -1):
    for col in range(1, space + 1):
        print(end=' ')
    space += 1
    for col in range(1, row + 1):
        print(chr(char) + chr(low), end=' ')
        char += 1
        low += 1
    print()'''

'''
*  *  *  *  *
   *  *  *
      *
   *  *  *
*  *  *  *  *
'''
