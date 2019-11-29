

prenom = "Quel est votre prenom ? :"
a="Quel est votre age ? :"
b="Quel est votre sexe ? h pour Homme et f pour femme :"
c="Quel est votre poids en Kg ? :"
d="Quel est votre sport pratique ? :"
sports_pratique ="sports de contact/combats=0 ,sports d'addresse=1,sports de fond/endurance=2 :"
t="Utilisez vous un traitement particulier ? 'oui' ou 'non' : "
quelt="Quel tratement prenez vous ? :"
allergie="Avez vous des allergies connues ? 'oui' ou 'non' : "
allergi_util="Quelles allergies ? :"
nature1 = "Douleur=0,Gonflement=1,Invalidite=2,antecedants comparable=3 :"
nature = "Pourquoi avez vous besoin de consulter ? :"
liste_nature=['0','1','2','3']
liste_sport = ['0','1','2']
douleur="Ou avez vous mal ? :"
liste_endroit_douleur= ['cheville','genoux','hanche','bassin','coude','poignet','epaule','cou']
liste_douleur =['tendon','Tendon','TENDON','articulation','Articulation','ARTICULATION','articulaire','Articulaire','ARTICULAIRE','muscle','Muscle','MUSCLE','muscles','Muscles','MUSCLES']
liste_date_douleur=['quelques semaines','quelques jours','plusieurs mois']



name = raw_input(prenom)
print "Bonjour",name

age = int(input(a))
while (age<0 or age>100):
	age = int(input(a))


sexe = raw_input(b)
while (sexe!="h" and sexe!="f"):
	sexe = raw_input(b) 


poids = int(input(c))
while (poids<0):
	poids = int(input(c))


print (sports_pratique)
sport= raw_input(d)
while (sport not in liste_sport):
	sport= raw_input(d)


traitement=raw_input(t)
while (traitement!="oui" and traitement!="non"):
	traitement=raw_input(t)
	
if (traitement=="oui"):
	 quel_traitement= raw_input(quelt)
else:
	print ("Parfait !")


allergiesconnues= raw_input(allergie)	
while (allergiesconnues != "oui" and allergiesconnues!="non"):
	allergiesconnues=raw_input(allergie)

if (allergiesconnues=="oui"):
	allergieclient= raw_input(allergi_util)

else:
	print("Ok")

print (nature1)
natureconsul= raw_input(nature)
while (natureconsul not in liste_nature):
	natureconsul= raw_input(nature)

	
oudouleur=raw_input(douleur)
while (oudouleur not in liste_endroit_douleur):
	oudouleur=raw_input(douleur)


endroitdouleur=raw_input("Pensez vous que la douleur provient du : Tendon, Articulation, Muscle :")
while (endroitdouleur not in liste_douleur):
	endroitdouleur=raw_input("Pensez vous que la douleur provient du : Tendon, Articulation, Muscle :")

print(liste_date_douleur)
datedouleur=raw_input("Depuis combien de temps avez vous mal ? :") 
while (datedouleur not in liste_date_douleur):
	datedouleur=raw_input("Depuis combien de temps avez vous mal ? :") 
