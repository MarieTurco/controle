#     position du problème    

note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]
print(notes)

#Question 4 
#a

moy1= (notes[0][2] + notes[1][2] + notes[2][2] + notes[3][2] + notes[4][2] + notes[5][2]) / 6
print(f"Moyenne de l'élève 1 : {moy1}")

#b 

moy2= (notes[0][2] + notes[2][2] + notes[5][2]) / 3
print(f"Moyenne de l'élève 1 en maths : {moy2}")

#c 

def moyenne_tuples (liste_note,eleve = None,matiere = None):
  if matiere != None : 
    notes = [ liste_note[i][2] for i in range(len(liste_note)) if liste_note[i][0] == eleve and liste_note[i][1] == matiere]
    moyenne = sum(notes)/len(notes)
    return moyenne
  else :
    notes = [ liste_note[i][2] for i in range(len(liste_note)) if liste_note[i][0] == eleve ]
    moyenne = sum(notes)/len(notes)
    return moyenne
  
#test
print("le résultat de la fonction : " , moyenne_tuples(notes,"eleve2","math"))


# test faute matière 
#moyenne_tuples(notes,"eleve2","maths") : ne fonctionne pas





class Note:
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur


  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)


onote = Note('eleve1', 'maths', 13)
print(onote.eleve)
print(onote.matiere)
print(onote.valeur)
Note.afficher(onote)


#Question 5

eleve = [notes[i][0] for i in range(len(notes))]
print(eleve) 

onotes = Note("eleve1", 'maths',13)
Note.afficher(onotes)

