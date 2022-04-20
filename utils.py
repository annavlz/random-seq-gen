def align_times(structure, voices):
    result = [[] for _ in range(len(structure))]
    for current_beat, form in enumerate(structure):
        print("start beat")
        n_voices = form[0]
        voice_number = 0
        for _ in voices:
            print("start voice", len(result[current_beat]), n_voices, len(voices))
            if len(result[current_beat]) < len(voices):
                if len(result[current_beat]) < n_voices:
                    current_voice = voice_number + 1
                    if not current_voice in result[current_beat]:
                        print("New voice")
                        cell_length = voices[voice_number][0][1]
                        relative_beat = current_beat
                        while cell_length > 0:
                            print("REL BEAT", relative_beat, len(structure))
                            if relative_beat < len(structure):
                                result[relative_beat].append(voice_number + 1)
                            cell_length -= 1
                            relative_beat += 1
                        del voices[voice_number][0]
                else:
                    result[current_beat].append(0)
                voice_number += 1
            print("end voice", result)
        print("end beat",result)
    print(result)
    return result

