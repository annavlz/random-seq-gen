from utils import align_times, randomize_voices, seed_structure, process_voices
from copy import deepcopy

# voices_raw = [
#     [["es''4.", 3],["b'8",1],["c''16 as''16",1],["r8",1],["bes''8",1],["d''2",4],["des''4",2],["f'4",2],["\tuplet 3/8 {g'16 g' g'} r8",2],["bes'32 bes' bes' bes'",1],["a'4",2],["cis''16 d''8.",2]],
#     [["g'16 as'16 g'16 as'16", 2],["\appoggiatura b8 cis'4",2],["\appoggiatura bes'8 d'4",2],["\tuplet 3/4 {es'8 es' es'}",2],["\tuplet 3/4 {r8 es' es'}",2],["{e''2.-+}",6],["fis''4\glissando b''4\staccato",4],["r16 d'''16\staccato",1],["gis1",8]],
#     [["r16 b16 c' b",2],["c'8\staccato", 1],["c'4--",1],["as4",2],["ges'4.",3],["f'8",1],["\tuplet 3/4 {e'8 es' d'}",2],["des'4\staccato",2],["a'2",4],["ais'8\staccato",1],["cis'8\staccato",1],["gis8\staccato",1],["a4\glissando c'8\staccato",3],["\tuplet 3/16 {g32 g g} r16",1]],
#     [["\tuplet 3/4 { e8 e e}",2],["gis,4\glissando {b,4-+}",4],["bes8 (f8\staccato) r8",3],["e2\glissando fis2",8],["gis8\staccato",1],["d'8\staccato",1],["\tuplet 3/4 {a8 d f}",2],["r8",1],["dis,4",2],["d,4",2],["as32 as as g32",1]]
# ]
voices_raw = [
    [["e'16 e' e' e'",2],["c'2",4],["d'8 d'8",2],["e'8",1],["r8",1],["a'8 a'",2],[ "c''4.",3],["a'8",1]],
    [["c'4",1], ["d'8 d'8",2],["e'8",1],["r8",1],["a'8 a'",2],["e'8",1],["c'4",2],["d'8 d'8",2]]
]

# Input
tempo = 20 # beats per minute
minutes = 1
unit = 2 # notes per beat
number_of_voices = len(voices_raw)
window = 3
pause = "r8"
bar_size = 4

# Transformations
size = tempo * minutes * unit
structure = seed_structure(size,number_of_voices)
voices = randomize_voices(voices_raw, window, size)
# print(len(voices[0]), len(voices[1]))
times = align_times(structure, deepcopy(voices))
processed_voices = process_voices(voices, times, pause)
print(processed_voices[0])
print(processed_voices[1])


