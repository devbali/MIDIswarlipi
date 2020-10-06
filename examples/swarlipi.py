#!/usr/bin/env python

from midiutil import MIDIFile, thaats

base	 = 60	# Pitch for the base sa in the sargam
track    = 0
channel  = 0
time     = 0    # In beats
bpb 	 = 1    # In beats
tempo    = 120   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track
MyMIDI.addTempo(track, time, tempo)

sargam = "प म़ । ग । ग । ग ग । , (धम़) । रे । रे । ऱे रे ।, ध । .नि सा । सा । सा (साग) । प । ग सा । रे । सा .नि"
MyMIDI.addSwarLipi(track, channel, base, time, bpb, volume, sargam)

with open("sargam.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)