#renvoie le nombre de diviseurs d'un nombre

#n est un entier que l'on définit.
def nb_div( n : int) -> int:
    r = 0
#itère tous les nombres de 1 a n
    for i in range(1, n+1):
        #si n est divisible par i ( i est un diviseur de n)
        if n % i == 0:
            #si i est un diviseur de n, on ajoute 1 a r
            r = r + 1
#r est un entier qui est le nombre de diviseurs de n.
    print(r)
#définir qu'elle entier on souhaite mettre
nb_div(49)

def nb_div_tous_entiers(n : int) -> int:
    r = []
    for i in range(1, n+1):
        if n % i == 0:
            r.append(i)

    print(r)


nb_div_tous_entiers(49)