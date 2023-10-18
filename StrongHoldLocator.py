#Premier oeil d'enderman
x1, y1 = 12, -25 #Coordonnées x et y du lancé de l'oeil
x2, y2 = 25, -19 #Coordonnées x et y de l'atterissage de l'oeil

#Deuxième oeil d'enderman
x3, y3 = 92, -500 #Coordonnées x et y du lancé de l'oeil
x4, y4 = 106, -488 #Coordonnées x et y de l'atterissage de l'oeil

#Calcul des pentes
m1 = (y2 - y1) / (x2 - x1) #Premier oeil
m2 = (y4 - y3) / (x4 - x3) #Deuxième oeil

#Calcul des ordonnés à l'origine
b1 = y1 - m1 * x1 #Premier oeil
b2 = y3 - m2 * x3 #Deuxième oeil

#Calcul de l'intersection des vecteurs
x = (b2 - b1) / (m1 - m2)
y = m1 * x + b1

print(f"Le stronghold se trouve à {x}, {y}")