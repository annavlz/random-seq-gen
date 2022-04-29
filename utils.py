from pickletools import read_uint1
import random
import numpy
from signal import pause

def align_times(structure, voices):
    result = [[] for _ in range(len(structure))]
    for current_beat, form in enumerate(structure):
        n_voices = form[0]
        voices_order = random.sample(range(len(voices)), len(voices))
        voice_index = 0
        for _ in voices:
            if len(result[current_beat]) < len(voices):
                if len(result[current_beat]) < n_voices and len(voices[voices_order[voice_index]]) > 0:
                    current_voice = voices_order[voice_index] + 1
                    if not current_voice in result[current_beat]:
                        cell_length = voices[voices_order[voice_index]][0][1]
                        relative_beat = current_beat
                        while cell_length > 0:
                            if relative_beat < len(structure):
                                result[relative_beat].append(voices_order[voice_index] + 1)
                            cell_length -= 1
                            relative_beat += 1
                        del voices[voices_order[voice_index]][0]
                else:
                    result[current_beat].append(0)
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
    print(flat_list)
    return flat_list[0:size]

def rand_with_window(voice, window, size):
    voicebasesize = int(round(size / window,0))
    indexes = list(range(0, voicebasesize + 1))
    voicebase = []
    for i in indexes:
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


