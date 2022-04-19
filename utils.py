def align_times(structure, voices):
    result = []
    for n_voices, _ in structure:
        print("Start beat")
        voice_index = 0
        beat_voices = []
        for _ in voices:
            print("Start voice")
            print("beat_voices", beat_voices)
            print("n_voices", n_voices)
            print("voice_index", voice_index)
            if len(beat_voices) <= n_voices:
                cell_length = voices[voice_index][0][1]
                while cell_length > 0:
                    print("Start cell", cell_length)
                    beat_voices.append(voice_index + 1)
                    cell_length -= 1
                del voices[voice_index][0]
                n_voices -= 1
            else:
                beat_voices.append(0)
            voice_index += 1
            print("End voice", beat_voices)
        result.append(beat_voices)
        print("End beat", result)
    return result

