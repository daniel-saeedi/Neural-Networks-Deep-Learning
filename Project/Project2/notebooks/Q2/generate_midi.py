import os
from pyknon.genmidi import Midi
from pyknon.music import NoteSeq, Note

MIDI_DATA_DIR = "./data/midi"

index = 0
for instrument in range(128):
    for octave in range(9):
        for value in range(12):
            notes1 = NoteSeq([Note(value=value, octave=octave+1)])
            midi = Midi(1, tempo=60, instrument=instrument)
            midi.seq_notes(notes1, track=0)
            midi.write(os.path.join(MIDI_DATA_DIR, "%s_%s.mid" % (instrument, octave * 12 + value)))
