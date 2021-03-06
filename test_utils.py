from utils import align_times, combine_voice_times, rand_with_window, seed_structure, create_densities

def check_0(cell):
    if cell[1] == 0:
        return True
    else:
        return False

def test_align_times():
    structure = [[0,1], [2,1], [2,3], [3,3], [1,3]]
    voices = [
        [["1-1",1],["1-2",2],["1-3",1]],
        [["2-1",1],["2-2",1],["2-3",1]],
        [["3-1",3],["3-2",1],["3-3",1]]
    ]
    result = align_times(structure, voices) 
    assert len(result) == len(structure)
    filtered_0_result = []
    for i in result:
        filtered_0_result.append(list(filter(check_0, i)))
        # voices = []
        # print(i)
        # for v in i:
        #     voices.append(v)
        # print(voices)
        # assert len(set(voices)) == len(voices)
    assert len(filtered_0_result[0]) == 3
    assert len(filtered_0_result[1]) == 1
    assert len(filtered_0_result[2]) == 0
    assert len(filtered_0_result[3]) == 0
    assert len(filtered_0_result[4]) == 0

def test_combine_voice_times():
    v_number = 1
    pause = "r8"
    voice = [["es''4.", 3],["b'8",1],["c''16 as''16",1]]
    times = [[3,2,1],[1,0,0],[1,3,0],[0,2,0],[1,2,0],[0,0,0],[1,0,0]]
    expected_result = "es''4. r8 b'8 r8 c''16 as''16"
    result = combine_voice_times(v_number, voice, times, pause)
    assert result == expected_result

def test_rand_with_window():
    voice = [["es''4.", 3],["b'8",1],["c''16 as''16",1]]
    window = 2
    size = 20
    expected_result = 20
    result = rand_with_window(voice, window, size)
    assert len(result) == expected_result

def test_seed_structure():
    size = 20
    n_voices = 5
    bar_size = 4
    density_range = [0,5]
    result = seed_structure(size, n_voices, bar_size, density_range)
    assert len(result) == 20
    for i in result:
        assert len(i) == 2
        assert i[0] <= n_voices
        assert i[1] <= n_voices
        assert i[0] >= 0
        assert i[1] >= 0

def test_create_densities():
    crescendo = create_densities([5,10], 0, 5)
    assert crescendo == [6,7,8,9,10]
    diminuendo = create_densities([10,5], 0, 5)
    assert diminuendo == [10,9,8,7,6]
    same = create_densities([5,5], 0, 4)
    assert same == [5,5,5,5]