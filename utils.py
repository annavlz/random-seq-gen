from operator import contains


def align_times(structure, voices):
    result = [[] for i in range(len(structure))]
    for current_beat, form in enumerate(structure):
        n_voices = form[0]
        voice_number = 0
        for i in voices:
            if len(result[current_beat]) < n_voices:
                current_voice = voice_number + 1
                if not current_voice in result[current_beat]:
                    cell_length = voices[voice_number][0][1]
                    relative_beat = current_beat
                    while cell_length > 0:
                        result[relative_beat].append(voice_number + 1)
                        cell_length -= 1
                        relative_beat += 1
                    del voices[voice_number][0]
            else:
                result[current_beat].append(0)
            n_voices -= 1
            voice_number += 1
    print(result)
    return result

