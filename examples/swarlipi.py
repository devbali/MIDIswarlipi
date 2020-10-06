#!/usr/bin/env python

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