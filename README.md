# MIDI Swarlipi
A fork of the MIDI Util python package with an addition of the Hindustani Swarlipi

## Addition to MIDI Util
- This fork adds one method to the MIDIFile Class, the addSwarLipi method
- This works very similarly to the MIDIFile.addNote method, but you can provide an entire melody in swarlipi format

```python
from midiutil import MIDIFile, thaats

base	 = 60	# Pitch for the base sa in the sargam
track    = 0
channel  = 0
time     = 0    # Start time (in beats)
bpb 	 = 1    # Amount of beats per | (In beats)
tempo    = 60   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track
MyMIDI.addTempo(track, time, tempo)

sargam = "पप म । ग़रेग़ रे । सा - सा । .नि सा - । मम म । रेम ध़ प । ग़ - रे । म (पमग़रेसा) । , ।ग़ । - । ग़ प रे । - । ग़रेसा .नि .ध़ । रे । म ग़ रे सा । - रेसा । .नि - सा"
MyMIDI.addSwarLipi(track, channel, base, time, bpb, volume, sargam)

with open("sargam.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
```

- This works very similarly to the addNote method, but instead adds an entire long melody worth of notes
- The "base" is the pitch for the base "sa" in the melody, so for example if base is set to 60 then a re komal would be 61

### Note
If your melody belongs to a thaat of Hindustani music, you can import midiutil.thats, which is a dictionary of arrays, and pass one to the addSwarLipi method

For example:
```python
MyMIDI.addSwarLipi(track, channel, base, time, bpb, volume, sargam, thaat = thaats["asavari"])
```
This would enable you to write a melody such as "ग म प ध" and it will automatically read ga and dha as komal since they are komal in raags of the asavari thaat

## Swarlipi
The swarlipi string used in this package follows these rules:
- The ascii | or the devanagari full stop character । can be used for beat markers
- ऱे, ग़, ध़, ऩि are used for komal versions (if necessary), and मं or म़ can be used for ma teevra
- For a note of another octave, the note must be followed or preceded by ascii full stops (periods). .ऩि is ni from an octave below, while सा. is sa from an octave above
- "-" is used for continuing a note, while "," is used for pauses
- () can be used for doublets or triplets to be executed in the same time as a single note

## Installation
The installation instructions for this fork are the same as the midiutils (except this functionality is not available in the pip package)
So to install this package:
- Clone this package onto your machine
- Run the setup.py script as such `python setup.py install`
- Or, alternatively, add the src directory to your $PYTHONPATH so the package is found by python

## Documentation
For more information about the midiutils package (not related to the swarlipi functionality) please go to the base repository at https://github.com/MarkCWirt/MIDIUtil
