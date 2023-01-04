l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
out = []
for i in l:
    for j in l:
        if i + j == 10 and i != j and [i,j] not in out :
            out += [[i, j]]
print(out)