#!/usr/bin/env python3
from q_model import Policy

def _get_reward(game):
    ''' Score for the current game state '''
    if game.won():
        return 1
    if game.lost():
        return -1

    # Negative reward values incentivizes finding the fastest solution
    return -0.2


def solve(game: Game, attempts: int = 0):
    '''
    Try to solve the game in a predefined number of steps

    If attempts is 0, game.attempts is used instead
    '''
    actions = game.get_actions()
    policy = Policy(len(actions))

    attempts = attempts or game.attempts

    for _ in range(attempts):
        game.reset()

        steps = 0
        while not (game.won() or game.lost()):
            steps += 1

            # Take the index of the state with highest reward
            state = game.get_state()
            idx = policy.get_action_id(state)

            # Execute the highest rewarding action
            game.do_action(actions[idx])
            reward = _get_reward(game)

            # Update the policy of the last action performed
            new_state = game.get_state()
            policy.update(state, new_state, idx, reward)

            # game.draw()


        if game.won():
            print('Won in ', steps)
        else:
            print('Lost in ', steps)


if __name__ == '__main__':
    from problems.labirinth import Game

    solve(Game())
