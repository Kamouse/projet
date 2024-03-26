L_coef=[2,6,4,8,16,12,7]
L_notes=[12,7,8,9,5,11,18]

def calculer_moyennes_triées(coefs, notes):
    if not coefs:
        return [0]
    moyennes = [c * n for c, n in zip(coefs, notes)]
    moyennes_triées = sorted(moyennes)
    return moyennes_triées

moyennes_triées = calculer_moyennes_triées(L_coef, L_notes)
min_moyenne = moyennes_triées[0]
max_moyenne = moyennes_triées[-1]
print("La plus petite moyenne est:", min_moyenne)
print("La plus grande moyenne est:", max_moyenne)
print("Toutes les moyennes triées du plus petit au plus grand sont:", moyennes_triées)


