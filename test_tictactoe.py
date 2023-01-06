

import pytest

import TicTacToe_2016 as ttt

class TestZone:



    def test_create_grid(self):
        b = ttt.create_grid()
        print(b)
        assert b == [[" ", " ", " "],
                     [" ", " ", " "],
             [" ", " ", " "]]

def test_announce_win(capsys):
    symbol = "X"
    ttt.announce_win(symbol)

    captured = capsys.readouterr()

    assert captured.out ==  "Player X just nicked the game"
