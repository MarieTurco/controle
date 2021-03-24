# position du problème    

note1 = ('eleve1', 'math', 13)
note2 = ('eleve1', 'physique', 15)
note3 = ('eleve1', 'math', 13)
note4 = ('eleve1', 'eco', 12)
note5 = ('eleve1', 'eco', 13)
note6 = ('eleve1', 'math', 12)
note7 = ('eleve2', 'math', 13)
note8 = ('eleve2', 'math', 14)

notes = [note1, note2, note3, note4, note5, note6,note7,note8]
print(f"note : {notes}")

#Question 4 
#a

moy1= (notes[0][2] + notes[1][2] + notes[2][2] + notes[3][2] + notes[4][2] + notes[5][2]) / 6
print(f"Moyenne de l'élève 1 : {moy1}")

#b 

moy2= (notes[0][2] + notes[2][2] + notes[5][2]) / 3
print(f"Moyenne de l'élève 1 en maths : {moy2}")

#c 

def moyenne_tuples (notes,eleve = None,matiere = None):
  notes = [ note for note in notes if note[0] == eleve ] if eleve is not None else notes
  notes  = [ note for note in notes if note[1] == matiere] if matiere is not  None else notes
  print(notes)
  return sum(notes[2] for notes in notes)/len(notes)


  
#test
print("le résultat de la fonction : " , moyenne_tuples(notes,"eleve2",None))


# test faute matière 
#moyenne_tuples(notes,"eleve2","maths") : ne fonctionne pas
class Note:
  instances = []  
  def __init__(self, eleve, matiere, valeur): #La méthode pour créer un objet
    self.eleve = eleve
    self.matiere = matiere
    self.valeur = valeur

    Note.instances.append(self)


  
  def afficher(self):
    print('eleve', self.eleve, 'matiere', self.matiere, 'note', self.valeur)



  def __str__(self):
    return f"{self.__class__.__name__}('{self.eleve}','{self.matiere}','{self.valeur}')"


  @classmethod #attention !
  def vider(cls):
    cls.instances = []

  @classmethod #attention !
  def moyenne(cls):
    return(sum(n.valeur for n in cls.instances)/len(cls.instances))


#Question 5

onotes = [Note(eleve, matiere, valeur) for eleve, matiere, valeur in notes]
print(f"longueur de la liste : {len(onotes)}")


#Question 6 

for onote in onotes:
  onote.afficher()
  print(onote.valeur)


#Question 8 

def moyenne_Notes(liste, eleve = None ,matiere = None):
  notes = [ note for note in liste if note.eleve == eleve ] if eleve is not None else liste
  notes  = [ note for note in liste if note.matiere == matiere] if matiere is not  None else liste
  print(notes)
  return sum(notes.valeur for notes in notes)/len(notes)


print(f"Test : {moyenne_Notes([onote])}")




if __name__ == '__main__':
  note1 = ('eleve1', 'math', 13)
  note2 = ('eleve1', 'physique', 15)
  note3 = ('eleve1', 'math', 13)
  note4 = ('eleve1', 'eco', 12)
  note5 = ('eleve1', 'eco', 13)
  note6 = ('eleve1', 'math', 12)
  note7 = ('eleve2', 'math', 13)
  note8 = ('eleve2', 'math', 14)


  notes = [note1, note2, note3, note4, note5, note6, note7, note8]

  notes_e2 = [note for note in notes if note[0] == 'eleve2']

  print(notes_e2)

  print(sum(note[2] for note in notes_e2)/len(notes_e2))

  notes_e2_math = [note for note in notes_e2 if note[1] == 'math']

  print(sum(note[2] for note in notes_e2_math)/len(notes_e2_math))


  print(moyenne_tuples(notes, 'eleve2', 'math'))


  onote = Note('eleve2', 'maths', 13)





  onotes = [Note(eleve, matiere,  valeur) for eleve, matiere, valeur in notes]




  onotes = [Note(*note) for note in notes]


#on vide la liste
  Note.vider()

  print(Note)

  onotes = [Note(*note) for note in notes]

  print(Note.moyenne())
