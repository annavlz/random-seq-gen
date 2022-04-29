import random
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

def seed_structure(size, n_voices):
    
    structure = []
    while size > 0:
        n = random.randint(1,n_voices)
        d = random.randint(-1, 1)
        structure.append([n, d])
        size -= 1
    return structure

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


