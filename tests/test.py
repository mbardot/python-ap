
from src import main

import pytest

#file = input("give a fasta file for testing")
file = "abc"


def test_needleman():
    #test if the file is correct
    # raise FileNotFoundError('')
    with pytest.raises(FileNotFoundError):
        main(file)
 



