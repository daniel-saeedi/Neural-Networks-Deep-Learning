seq_lenght = 40


#Helping function        
def extract_notes(file):
    notes = []
    pick = None
    for j in file:
        # instrument is a method from music21
        songs = instrument.partitionByInstrument(j)
        for part in songs.parts:
            pick = part.recurse()
            for element in pick:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append(".".join(str(n) for n in element.normalOrder))

    return notes

def chords_n_notes(Snippet):
    Melody = []
    offset = 0 #Incremental
    for i in Snippet:
        #If it is chord
        if ("." in i or i.isdigit()):
            chord_notes = i.split(".") #Seperating the notes in chord
            notes = [] 
            for j in chord_notes:
                inst_note=int(j)
                note_snip = note.Note(inst_note)            
                notes.append(note_snip)
                chord_snip = chord.Chord(notes)
                chord_snip.offset = offset
                Melody.append(chord_snip)
        # pattern is a note
        else: 
            note_snip = note.Note(i)
            note_snip.offset = offset
            Melody.append(note_snip)
        # increase offset each iteration so that notes do not stack
        offset += 1
    Melody_midi = stream.Stream(Melody)   
    return Melody_midi


def Malody_Generator(Note_Count):
    # Note_Count = Count of Notes want to generate
    seed = [np.random.randint(0,len(X_test)-1, seq_lenght)] #sequence_length = 40
    Music = ""
    Notes_Generated=[]
    for i in range(Note_Count):
        seed = np.array(seed).reshape(1,seq_lenght,1)
        prediction = model.predict(seed, verbose=0)[0]
        prediction = np.log(prediction) / 1.0 #diversity
        exp_preds = np.exp(prediction)
        prediction = exp_preds / np.sum(exp_preds)
        index = np.argmax(prediction)
        index_N = index/ float(L_symb)  # L_symb is length of total unique characters
        Notes_Generated.append(index)
        Music = [reverse_mapping[char] for char in Notes_Generated] # reverse_mapping is a dictionary that maps each number to its related note 
        seed = np.insert(seed[0],len(seed[0]),index_N)
        seed = seed[1:]
    #Now, we have music in form or a list of chords and notes and we want to be a midi file.
    Melody = chords_n_notes(Music)
    Melody_midi = stream.Stream(Melody)   
    return Music,Melody_midi

Music_notes, Melody = Malody_Generator(50)
#To save the generated melody
Melody.write('midi','Melody_Generated.mid')



