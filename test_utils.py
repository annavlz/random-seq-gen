from utils import align_times

def test_align_times():
    structure = [[2,1], [1,5], [3,6], [1,3]]
    voices = [[["1-1",1],["1-2",2]],[["2-1",1],["2-2",1]],[["3-1",3],["3-2",1]]]
    expected_result = [[1,2,0],[1,0,0],[1,2,3],[3,0,0]]
    result = align_times(structure, voices) 
    assert len(result) == len(expected_result)
    for i in result:
        assert len(i) == len(voices)
    assert result == expected_result