import pytest
from . import triple_num

def test_triple_num():
    """A few unittests for the triple_num function
    """
    assert triple_num(0) == 0
    
    assert triple_num(0.5) == 1.5
    
    assert triple_num (-2) == -6
    
def test_triple_num_errors():
    """
    check we fail when supplying non num. 
    """
    with pytest.raises(TypeError):
        triple_num("a") == "aaa"
    
    with pytest.raises(TypeError):
        triple_num([1,2,1,2])
