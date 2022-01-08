from midi2audio import FluidSynth
import os

fs = FluidSynth()

path = "midi/"
#Getting midi files
midi_list = []
for i in os.listdir(path):
  if i.endswith(".mid"):
    fs.midi_to_audio(path+i, 'converted/'+i)