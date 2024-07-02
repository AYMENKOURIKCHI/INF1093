# Trie d'une sequence en ordre croissant a base du trie isertion
def quickSort(tab):
    if len(tab) <= 1:
        return tab

    pivot = tab.pop()

    petit = []
    grand = []

    for val in tab:
        if val < pivot:
            petit.append(val)
        else:
            grand.append(val)

    return quickSort(petit) + [pivot] + quickSort(grand)


tab = [8, 4, 5, 3, 25, 0 , 14, -1]
print(quickSort(tab))
        
    
