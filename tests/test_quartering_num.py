import pytest
from . import quartering_num

@pytest.mark.parametrize("num, expected",[
    (1,0.25),
    (0,0),
    (-4,-1),
    (24,6)
    ])
def test_quartering_num(num, expected):
    """Test appropriate input/output pairs
    """
    assert quartering_num(num) == expected
    

def test_quartering_num_errors():
    """
    check we fail when supplying non num.
    """
    with pytest.raises(TypeError):
        quartering_num("aaaa") == "a"
        
    with pytest.raises(TypeError):
        quartering_num([1,5,1,5,1,5])
        
    with pytest.raises(TypeError):
        quartering_num(True) == 0.25