def remove_dups(L1, L2):
    to_remove = []
    for e in L1:
        if e in L2:
            to_remove.append(e)
    for i in to_remove:
        L1.remove(i)


L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
remove_dups(L1, L2)
