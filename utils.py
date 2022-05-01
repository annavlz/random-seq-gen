import random
import numpy

def in_beat(current_voice, current_beat_content):
    for i in current_beat_content:
        if i != 0 and current_voice in i:
            return True

def align_times(structure, voices):
    result = [[] for _ in range(len(structure))]
    memory_cell = []
    for current_beat, form in enumerate(structure):
        n_voices = form[0]
        density = form[1]
        voices_limit = n_voices
        voices_order = random.sample(range(len(voices)), len(voices))
        voice_index = 0
        for _ in voices:
            if len(result[current_beat]) < len(voices):
                enough_cells = len(voices[voices_order[voice_index]]) > 0 # safety net in case there is not enough cells
                under_voice_limit = len(result[current_beat]) < n_voices
                under_density_limit = density > voices_limit or density > 0
                current_voice = voices_order[voice_index] + 1
                if under_voice_limit and enough_cells:
                    if not in_beat(current_voice, result[current_beat]):
                        cell_length = voices[voices_order[voice_index]][0][1]
                        part = 1
                        memory_cell = [current_voice, cell_length, voices[voices_order[voice_index]][0][0]]
                        relative_beat = current_beat
                        while cell_length > 0:
                            if relative_beat < len(structure):
                                result[relative_beat].append([current_voice, [memory_cell[2],part, memory_cell[1]]])
                            cell_length -= 1
                            relative_beat += 1
                            part += 1
                        del voices[voices_order[voice_index]][0]
                    density -= 1
                elif under_density_limit and len(memory_cell) > 0:
                    part = 1
                    cell_length = memory_cell[1]
                    if not in_beat(current_voice, result[current_beat]):
                        relative_beat = current_beat
                        while cell_length > 0:
                            if relative_beat < len(structure):
                                result[relative_beat].append([current_voice, [memory_cell[2],part, memory_cell[1]]])
                            cell_length -= 1
                            relative_beat += 1
                            part += 1
                    density -= 1
                else:
                    result[current_beat].append([current_voice, 0])
                voice_index += 1
    return result

def flatten_list(_2d_list):
    flat_list = []
    for element in _2d_list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list

def create_densities(bars_density, bars_density_length, bar_size):
    current_bar_density = bars_density[bars_density_length]
    next_bar_density = bars_density[bars_density_length+1]
    result = []
    if next_bar_density == current_bar_density:
        result = [current_bar_density for _ in range(bar_size)]
    elif next_bar_density > current_bar_density:
        dim_density_step_size = (current_bar_density - next_bar_density) / bar_size
        result = numpy.arange(next_bar_density, current_bar_density, dim_density_step_size).tolist()
        result.reverse()
    else:
        cres_density_step_size = (next_bar_density - current_bar_density) / bar_size
        result = numpy.arange(current_bar_density, next_bar_density, cres_density_step_size).tolist()
    return result

def seed_structure(size, n_voices, bar_size):
    structure_size = int(round(size / bar_size,0))
    bar_indexes = list(range(0, structure_size + 1))
    bars_density = []
    structure = []
    for i in bar_indexes:
        d = random.randint(0, n_voices)
        bars_density.append(d)
    bars_density_length = 0
    while bars_density_length < len(bars_density) - 1:
        beats = []
        densities = create_densities(bars_density, bars_density_length, bar_size)
        for d in densities:
            n = random.randint(0,n_voices)
            beats.append([n, d])
        structure.append(beats)
        bars_density_length += 1
    flat_list = flatten_list(structure)
    return flat_list[0:size]

def rand_with_window(voice, window, size):
    voicebasesize = int(round(size / window,0))
    indexes = list(range(0, voicebasesize + 1))
    voicebase = []
    for _ in indexes:
        n = random.randint(0,len(voice)-1-window)
        voicebase.append(voice[indexes[n]:indexes[n]+window])
    flat_list = flatten_list(voicebase)
    return flat_list[0:size]

def randomize_voices(voices_raw, window, size):
    voices = []
    for voice in voices_raw: 
        rand_with_window_voices = rand_with_window(voice, window, size)
        voices.append(rand_with_window_voices)
    return voices

def combine_voice_times(voice_n, voice, times, pause):
    beat_n = 0
    result = []
    while beat_n < len(times):
        time = times[beat_n]
        if voice_n in time:
            result.append(voice[0][0])
            beat_n += voice[0][1]
            del voice[0]
        else:
            result.append(pause)
            beat_n += 1
    return ' '.join(result)
        
def process_voices(voices, times, pause):
    result = []
    for i, voice in enumerate(voices):
        result.append(combine_voice_times(i, voice, times, pause))
    return result

def get_voice(beat):
    return beat[0]
    
def process_times(times, rest):
    strings = [[] for _ in times[0]]
    for beat in times:
        for cell in beat:
            voice_index = cell[0] - 1
            el = cell[1]
            if el == 0:
                strings[voice_index].append([rest,1])
            else: 
                note = el[0]
                note_part = el[1]
                note_length = el[2]
                if note_part == 1:
                    strings[voice_index].append([note, note_length])
    return strings

def calc_bars(string):
    result = ""
    for cell in string:
        note = cell[0]
        result += note
        result += " "
    return result

def process_strings(strings, bar_size):
    result = []
    for string in strings:
        ready_string = calc_bars(string)
        result.append(ready_string)
    return result