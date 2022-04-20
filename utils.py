import random

def align_times(structure, voices):
    result = [[] for _ in range(len(structure))]
    for current_beat, form in enumerate(structure):
        n_voices = form[0]
        voices_order = random.sample(range(3), 3)
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

