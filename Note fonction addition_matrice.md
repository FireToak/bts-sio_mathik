A <- []
B <- []
C <- []

ligne_a <- longueur(A)
colone_b <- longueur(A[0])

Pour tout i allant de 1 à ligne_a
	Pour tout j allant de 1 à colone_b
		C[i][j] <- A[i][j] + B[i][j]

Pour tout i allant de 1 à ligne_a
	Pour tout j allant de 1 à colone_b
		Affiche C[i][j]


---
A = [[4,5,6],[1,2,3]]
B = [[4,5,6],[1,2,3]]
C = []

ligne_a = len(A)
colone_a = len(A[0])

for i in range(ligne_a):
    C.append([])
    for j in range(colone_a):
        C[i].append(A[i][j]+B[i][j])

ligne_c = len(C)
colone_c = len(C[0])

for p in range(ligne_c):
    for k in range(colone_c):
        print(C[p][k], end=" ")
    print("")