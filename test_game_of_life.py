import game_of_life as game

test_list1 = [game.Cell((1,2), 'alive')]
test_list2 = [game.Cell((1,2), 'alive'), game.Cell((1,2), 'dead'), game.Cell((6,2), 'alive')]


def test_alive_in():
    assert game.alive_in(test_list1) == 1#this test is passed
    assert game.alive_in(test_list2) == 3#this test is failed
    
    