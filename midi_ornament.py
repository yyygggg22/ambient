import time
import sys
import random
from more_itertools import difference
import rtmidi
import musx
from musx import keynum
from main_multi_solution import main

from harmonizer_dict import note_to_number, number_to_note
from harmonizer_dict import note_accidental_to_semitone as semitone
from harmonizer_dict import semitone_to_accidental as accidental

# MIDI port set up:
midiout = rtmidi.MidiOut()
outports = midiout.get_ports()
midiout.open_port(outports.index('IAC Driver Bus 1'))
midiout.is_port_open()

# Define the melody:
# chord_progression = main()[0]
# melody = keynum([['a2', 'd4', 'a4', 'e5'], ['d3', 'c#4', 'a4', 'f#5'], ['f3', 'c4', 'a4', 'e5'], ['e3', 'g3', 'b4', 'e5'], ['f3', 'f3', 'ab4', 'c5'], ['b2', 'f#3', 'b4', 'e5'], ['g3', 'b3', 'g4', 'd5'], ['a3', 'b3', 'e4', 'a4'], ['d3', 'c4', 'f4', 'a4'], ['c#3', 'c#4', 'g#4', 'e5'], ['a2', 'b3', 'a4', 'e5'], ['d3', 'g3', 'a4', 'd5'], ['c3', 'g3', 'c4', 'eb4'], ['g3', 'a3', 'd4', 'g4'], ['e3', 'b3', 'e4', 'g4'], ['g3', 'a3', 'd4', 'g4'], ['e3', 'b3', 'e4', 'g4'], ['g3', 'a3', 'd4', 'g4'], ['b2', 'a#3', 'd#4', 'f#4'], ['c3', 'g3', 'c4', 'e4'], ['a2', 'g3', 'c4', 'e4'], ['b2', 'e4', 'b4', 'f#5'], ['c3', 'e4', 'g4', 'c5'], ['c3', 'eb4', 'bb4', 'g5'], ['g3', 'd4', 'b4', 'f#5'], ['e3', 'e4', 'b4', 'g5'], ['g3', 'd4', 'c5', 'g5'], ['e3', 'e4', 'b4', 'a5'], ['g3', 'd4', 'b4', 'g5'], ['b2', 'd4', 'b4', 'f#5'], ['c3', 'c4', 'g4', 'e5'], ['a2', 'e4', 'g#4', 'c#5'], ['b2', 'd4', 'f#4', 'b4'], ['c3', 'eb4', 'g4', 'c5'], ['f3', 'g3', 'c4', 'f4'], ['e3', 'g3', 'e4', 'b4'], ['f3', 'f3', 'c4', 'a4'], ['b2', 'f#3', 'd4', 'b4'], ['g3', 'b3', 'd4', 'g4'], ['a3', 'a3', 'd4', 'e4'], ['d3', 'a3', 'c4', 'f4'], ['c#3', 'e3', 'c#4', 'g#4'], ['a2', 'b3', 'e4', 'a4'], ['d3', 'g3', 'd4', 'a4'], ['f3', 'a3', 'c4', 'f4'], ['e3', 'b3', 'd#4', 'g#4'], ['f3', 'c4', 'eb4', 'ab4'], ['b3', 'b3', 'e4', 'f#4'], ['g3', 'd4', 'f4', 'bb4'], ['a3', 'c4', 'e4', 'a4'], ['d3', 'd4', 'f4', 'a4'], ['c#3', 'e4', 'g#4', 'c#5'], ['a2', 'e4', 'g#4', 'c#5'], ['d3', 'd4', 'g4', 'a4'], ['f3', 'c4', 'e4', 'a4'], ['e3', 'g3', 'e4', 'b4'], ['f3', 'f3', 'c4', 'ab4'], ['b2', 'f#3', 'd4', 'a4'], ['g3', 'bb3', 'd4', 'f4'], ['a2', 'c4', 'e4', 'g4'], ['d3', 'a3', 'c#4', 'f#4'], ['c#3', 'c#4', 'g#4', 'd#5']])
melody = [
    [['c3', 'g3', 'eb4', 'bb4'], ['c3', 'c4', 'd4', 'g4'], ['g3', 'b3', 'd4', 'g4']], 
    [['c3', 'g4', 'eb5', 'bb5'], ['c3', 'c5', 'd5', 'g5'], ['g3', 'b4', 'd5', 'g5']], 
    [['c4', 'g4', 'eb5', 'bb5'], ['c4', 'c5', 'd5', 'g5'], ['g3', 'b4', 'd5', 'g5']], 
    [['c3', 'g4', 'bb4', 'eb5'], ['c3', 'd4', 'c5', 'g5'], ['g3', 'd4', 'b4', 'g5']], 
    [['c4', 'g4', 'bb4', 'eb5'], ['c3', 'd4', 'c5', 'g5'], ['g3', 'd4', 'b4', 'g5']], 
    [['c3', 'bb3', 'g4', 'eb5'], ['c3', 'd4', 'c5', 'g5'], ['g3', 'd4', 'b4', 'g5']]
]


def spell_pool(melody):
    # Grab the bass note (without register):
    bass_note_list = []
    for i in range(len(melody)):
        progression = melody[i]
        for j in range(len(progression)):
            chord = progression[j]
            bass_note = chord[0][:-1]
            bass_note_list.append(bass_note)
    # Test:
    print('\nbass_note_list: ' + str(bass_note_list) + '\n' + str(len(bass_note_list)))
    # Get the diatonic spelling:
    diatonic_pool = []
    diatonic_sublist = []
    for i in range(len(bass_note_list)):
        start_note = bass_note_list[i][0]
        start_note_num = note_to_number[start_note]
        diatonic_sublist.append(start_note)
        for number in [1, 2, 4, 5, 6]:
            if start_note_num + number > 7:
                next_note = number_to_note[start_note_num + number - 7]
            else:
                next_note = number_to_note[start_note_num + number]
            diatonic_sublist.append(next_note)
        # print('\ndiatonic_sublist: ' + str(diatonic_sublist) + '\n' + str(len(diatonic_sublist)))
        diatonic_pool.append(diatonic_sublist)
        diatonic_sublist = []
    # Test:
    print('\ndiatonic_pool: ' + str(diatonic_pool) + '\n' + str(len(diatonic_pool)))
    # Get the chromatic spelling:
    chromatic_pool = []
    chromatic_sublist = []
    benchmark = (2, 2, 3, 2, 2)
    for i in range(len(diatonic_pool)):
        progression = diatonic_pool[i]
        chromatic_sublist.append(progression[0])
        for j in range(1, len(progression)):
            former, latter = progression[j-1], progression[j]
            if semitone[latter] < semitone[former]:
                difference = benchmark[j-1] - (semitone[latter] + 12 - semitone[former]) 
            else:
                difference = benchmark[j-1] - (semitone[latter] - semitone[former])
            offset = accidental[difference]
            latter = latter + offset
            chromatic_sublist.append(latter)
        # print('\nchromatic_sublist: ' + str(chromatic_sublist) + '\n' + str(len(chromatic_sublist)))
        chromatic_pool.append(chromatic_sublist)
        chromatic_sublist = []
    # Test:
    print('\nchromatic_pool: ' + str(chromatic_pool) + '\n' + str(len(chromatic_pool)))
    return chromatic_pool

if __name__ == '__main__':
    chromatic_pool = spell_pool(melody)

# Assign the pool with register:
def add_register(chromatic_pool):
    pool_register = []
    pool_register_sublist = []
    for i in range(len(chromatic_pool)):
        progression = chromatic_pool[i] * 2
        for j in range(int(len(progression) * 0.5)):
            note = progression[j]
            pool_register_sublist.append(note + '6')
        for k in range(int(len(progression) * 0.5), len(progression)):
            note = progression[k]
            pool_register_sublist.append(note + '7')
        # print('\npool_register_sublist: ' + str(pool_register_sublist) + '\n' + str(len(pool_register_sublist)))
        pool_register.append(pool_register_sublist)
        pool_register_sublist = []
    # Test:
    print('\npool_register: ' + str(pool_register) + '\n' + str(len(pool_register)))
    return pool_register

if __name__ == '__main__':
    pool_register = add_register(chromatic_pool) * 100

# Flatten the chord_progression:
# melody = keynum([item for sublist in chord_progression for item in sublist])
# melody = keynum([item for sublist in melody for item in sublist])

# Test:
# print('\nflatten_chord_progression: ' + str(melody))
# print(len(melody))

# Control the player:
# command = input('\nContinue? (y/n) ')
# if command == 'y':
#     control = True
# else:
#     sys.exit()

# Real time MIDI output:
# if control == True:
    for i in range(len(pool_register)):
        # Assign the note pool:
        note_pool = pool_register[i]
        # Assign the possibility:
        possibility = (1, 1, 1, 1, 1, 1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
        # Select the notes:
        note_selected = random.choices(note_pool, weights=(possibility), k = 4)
        # pick a random midi key number
        key_1 = keynum(note_selected[0])
        key_2 = keynum(note_selected[1])
        key_3 = keynum(note_selected[2])
        key_4 = keynum(note_selected[3])
        # pick a random duration
        # dur = musx.pick(3, 3.5, 4)
        # dur = musx.pick(0.8, 1.3, 1.6)
        dur = musx.pick(0.09, 0.1, 0.12)
        vel = musx.pick(50, 70, 80)
        # send it out
        print(f"group {i+1}, key: {key_1}, {key_2}, {key_3}, {key_4}, dur: {dur}")
        midiout.send_message(musx.note_on(0, key_1, vel))
        # wait for duration
        time.sleep(dur)
        midiout.send_message(musx.note_off(0, key_1, vel))
        midiout.send_message(musx.note_on(0, key_2, vel))
        # wait for duration
        time.sleep(dur)
        midiout.send_message(musx.note_off(0, key_2, vel))
        midiout.send_message(musx.note_on(0, key_3, vel))
        # wait for duration
        time.sleep(dur)
        midiout.send_message(musx.note_off(0, key_3, vel))
        midiout.send_message(musx.note_on(0, key_4, vel))
        # wait for duration
        time.sleep(dur)
        # stop the note
        midiout.send_message(musx.note_off(0, key_4, vel))
        if i == int(len(pool_register) - 1):
            i = 0

print("\nAll done!\n")

# set midi synth back to piano
midiout.send_message(musx.program_change(0, 0))