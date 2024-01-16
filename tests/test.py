
#from Needleman_Wunsch import main
import src
import pytest



def test_needleman():
    
    assert src.Needleman_Wunsch('GCATGCG', 'GATTACA') == 0



