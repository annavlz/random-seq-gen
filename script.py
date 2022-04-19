import random
def flatten_list(_2d_list):
    flat_list = []
    for element in _2d_list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

def create_times(voice):
    times = []
    for i, v in enumerate(voice):
        length = v[1]
        while length > 0:
            times.append(i)
            length -= 1
    return times

voice1 = [["es''4.", 3],["b'8",1],["c''16 as''16",1],["r8",1],["bes''8",1],["d''2",4],["des''4",2],["f'4",2],["\tuplet 3/8 {g'16 g' g'} r8",2],["bes'32 bes' bes' bes'",1],["a'4",2],["cis''16 d''8.",2]]
voice2 = [["g'16 as'16 g'16 as'16", 2],["\appoggiatura b8 cis'4",2],["\appoggiatura bes'8 d'4",2],["\tuplet 3/4 {es'8 es' es'}",2],["\tuplet 3/4 {r8 es' es'}",2],["{e''2.-+}",6],["fis''4\glissando b''4\staccato",4],["r16 d'''16\staccato",1],["gis1",8]]
voice3 = [["r16 b16 c' b",2],["c'8\staccato", 1],["c'4--",1],["as4",2],["ges'4.",3],["f'8",1],["\tuplet 3/4 {e'8 es' d'}",2],["des'4\staccato",2],["a'2",4],["ais'8\staccato",1],["cis'8\staccato",1],["gis8\staccato",1],["a4\glissando c'8\staccato",3],["\tuplet 3/16 {g32 g g} r16",1]]
voice4 = [["\tuplet 3/4 { e8 e e}",2],["gis,4\glissando {b,4-+}",4],["bes8 (f8\staccato) r8",3],["e2\glissando fis2",8],["gis8\staccato",1],["d'8\staccato",1],["\tuplet 3/4 {a8 d f}",2],["r8",1],["dis,4",2],["d,4",2],["as32 as as g32",1]]

tempo = 60
minutes = 1
unit = 2
number_of_voices = 4
size = tempo * minutes * unit
structure = []
while size > 0:
    n = random.randint(1,number_of_voices)
    d = random.randint(-1, 1)
    structure.append([n, d])
    size -= 1
# print(structure)

voice1base = []
voice2base = []
voice3base = []
voice4base = []
window = 3
voicebasesize = int(round(tempo * minutes * unit / window,0))
indexes = list(range(0, voicebasesize-window))
for i in indexes:
    n1 = random.randint(0,len(voice1)-1-window)
    n2 = random.randint(0,len(voice2)-1-window)
    n3 = random.randint(0,len(voice3)-1-window)
    n4 = random.randint(0,len(voice4)-1-window)
    voice1base.append(voice1[indexes[n1]:indexes[n1]+window])
    voice2base.append(voice2[indexes[n2]:indexes[n2]+window])
    voice3base.append(voice3[indexes[n1]:indexes[n3]+window])
    voice4base.append(voice4[indexes[n1]:indexes[n4]+window])

voice_times1 = create_times(flatten_list(voice1base))
voice_times2 = create_times(flatten_list(voice2base))
voice_times3 = create_times(flatten_list(voice3base))
voice_times4 = create_times(flatten_list(voice4base))

voice_bases = [flatten_list(voice1base), flatten_list(voice2base), flatten_list(voice3base), flatten_list(voice4base)]
output_raw = [[],[],[],[]]
voice_counter = [[]] * len(structure)
# for each beat with number of voices
for i, v in enumerate(structure):
    voices_count = v[1]
    # decide what voice will go first
    random_voices = list(range(0,4))
    random.shuffle(random_voices)
    counter = 0
    # create voices as many as in the number
    while voices_count > 0:
        current_beat = voice_counter[i]
        current_voice = random_voices[counter]
        if len(current_beat) < voices_count:
            cell = voice_bases[current_voice][0] #take first cell from the first voice
            cell_length = cell[1]
            current_counter = 0
            while cell_length > 0:
                voice_counter[i + current_counter].append(current_voice)
                cell_length -= 1
            del voice_bases[current_voice][0]
            counter += 1
        voices_count -= 1

print(voice_counter)
# print(output_raw)


# for i in structure:
#     voices = i[0]
#     density = i[1]
#     v1