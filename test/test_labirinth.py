import unittest

from problems import labirinth as lab


class LabirinthTest(unittest.TestCase):
    def test_lose_condition_if_in_obstacles(self):
        game = lab.Game()

        game.board = lab.Coord(3, 3)
        game._hidden_obstacles = [
            lab.Coord(x=0, y=2)
        ]
        game._position = lab.Coord(x=0, y=2)

        outcome = game.lost()

        self.assertTrue(outcome)

    def test_not_lose_if_not_in_obstacles(self):
        game = lab.Game()

        game.board = lab.Coord(3, 3)
        game._hidden_obstacles = [
            lab.Coord(x=0, y=0),
            lab.Coord(x=1, y=0),
            lab.Coord(x=2, y=0),
            lab.Coord(x=0, y=1),
            lab.Coord(x=2, y=1),
            lab.Coord(x=0, y=2),
            lab.Coord(x=1, y=2),
            lab.Coord(x=2, y=2),
        ]
        game._position = lab.Coord(x=1, y=1)

        outcome = game.lost()

        self.assertFalse(outcome)


    def test_win_condition(self):
        game = lab.Game()

        game.board = lab.Coord(4, 4)
        game._goal = lab.Coord(1, 2)
        game._position = lab.Coord(1, 2)

        outcome = game.won()

        self.assertTrue(outcome)

    def test_not_win_if_position_neq_goal(self):
        game = lab.Game()

        game.board = lab.Coord(4, 4)
        game._goal = lab.Coord(1, 2)
        game._position = lab.Coord(1, 1)

        outcome = game.won()

        self.assertFalse(outcome)

    def test_move_right(self):
        game = lab.Game()

        game.board = lab.Coord(4, 4)
        game._position = lab.Coord(1, 0)
        game.do_action(lab.Coord(x=+1, y=0))

        self.assertEqual(lab.Coord(x=2, y=0), game._position)

    def test_move_left_overshoot(self):
        game = lab.Game()

        game.board = lab.Coord(4, 4)
        game._position = lab.Coord(0, 0)
        game.do_action(lab.Coord(x=-1, y=0))

        self.assertEqual(lab.Coord(x=0, y=0), game._position)

    def test_move_left(self):
        game = lab.Game()

        game.board = lab.Coord(4, 4)
        game._position = lab.Coord(1, 0)
        game.do_action(lab.Coord(x=-1, y=0))

        self.assertEqual(lab.Coord(x=0, y=0), game._position)

    def test_move_down_overshoot(self):
        game = lab.Game()

        game.board = lab.Coord(4, 4)
        game._position = lab.Coord(1, 0)
        game.do_action(lab.Coord(x=0, y=5))

        self.assertEqual(lab.Coord(x=1, y=4), game._position)

    def test_move_up_overshoot(self):
        game = lab.Game()

        game.board = lab.Coord(4, 4)
        game._position = lab.Coord(1, 0)
        game.do_action(lab.Coord(x=0, y=-1))

        self.assertEqual(lab.Coord(x=1, y=0), game._position)

