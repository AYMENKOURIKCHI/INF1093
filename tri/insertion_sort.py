# Trie d'une sequence en ordre croissant a base du trie isertion
def insertionSort(tab):
    n = len(tab)
    # Debutons le tri en considerant le premier item seul comme etant trie
    for i in range(1,n):
        # Memoriser la valeur a inserer
        value = tab[i]
        # Rechercher a quelle position inserer l'item dans la partie ordonnee
        pos = i
       
        while pos > 0 and value < tab[pos-1]:
            # Decaler les items vers la droite durant la recherche
            tab[pos] = tab[pos-1]
            pos -= 1

            # Inserer la valeur memorisee dans le slot ouvert
            tab[pos] = value
        print("value=" ,value, tab)

tab = [8, 4, 5, 3, 25, 0 , 14, -1]
insertionSort(tab)
        
    
