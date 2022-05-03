from utils import align_times, process_strings, randomize_voices, seed_structure, process_times, process_strings
from copy import deepcopy
import json
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help="File name")
args = parser.parse_args()

# Input
file = open(f'{args.filename}.json')
data = json.load(file)
file.close()

tempo = data['tempo'] # beats per minute
seconds = data['seconds']
unit = data['unit'] # notes per beat
window = data['window']
rest = data['rest']
bar_size = data['bar_size']
density_range = data['density_range']
voices_raw = list(data['voices'].values())
number_of_voices = len(voices_raw)


# Transformations
size = int(tempo/60 * seconds * unit)
structure = seed_structure(size, number_of_voices, bar_size, density_range)
voices = randomize_voices(voices_raw, window, size)
times = align_times(structure, deepcopy(voices))
strings = process_times(times, rest)
output = process_strings(strings, bar_size * unit)

with open(f'{args.filename}.txt', 'w') as writer:
    for i, voice in enumerate(output):
        writer.write(f'Voice{i+1}   ')
        writer.write(voice)
        writer.write("\n")

# for beat in times:
#     test = []
#     for i in beat:
#         test.append(i[0])
#     print(test, len(set(test)) == len(test))


