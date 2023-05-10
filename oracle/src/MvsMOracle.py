from Predictor import Predictor
import numpy as np


class MvsMOracle(Predictor):
    def __init__(self):
        super().__init__("MvsM", "tab")

    def predictNextNumber(self):
        sequence = self.getNumberSequence()
        for i in range(len(sequence)):
            move(int(sequence[i]))

        self.setNextNumberPredicted(gameboard[2](len(gameboard[2])-1))

        gameboard = np.empty((3, 15), dtype=str)
        board_idx = 0
        a = np.zeros((2, 3, 2, 3, 2))

        p1 = c1 = p2 = c2 = 0
        man_score = mach_score = moves = 0

        def zero_matrix():
            global a
            a = np.zeros((2, 3, 2, 3, 2))

        def zero_board():
            global gameboard
            gameboard = np.empty((3, 15), dtype=str)
            gameboard.fill('')

        # def reset():
        #     global p1, c1, p2, c2, man_score, mach_score, moves, board_idx
        #     zero_matrix()
        #     p1 = c1 = p2 = c2 = 0
        #     man_score = mach_score = moves = 0
        #     display_scores()
        #     zero_board()
        #     board_idx = 0
        #     # display_board()

        def display_board():
            for i in range(gameboard.shape[0]):
                for j in range(gameboard.shape[1]):
                    print(gameboard[i][j], end=' ')
                print()

        def display_scores():
            global man_score, mach_score
            print('Man Score:', man_score)
            print('Machine Score:', mach_score)

            man_per, mach_per = 0, 0
            total = man_score + mach_score
            man_win = '-'
            mach_win = '-'

            if total > 0:
                man_per = (man_score / total) * 100
                mach_per = (mach_score / total) * 100
                if man_score > mach_score:
                    man_win = '*'
                elif mach_score > man_score:
                    mach_win = '*'

            print('Man Win:', man_win)
            print('Machine Win:', mach_win)
            print('Man Percentage:', '{:.2f}'.format(man_per))
            print('Machine Percentage:', '{:.2f}'.format(mach_per))

        def judge(man_ans, mach_ans):
            global man_score, mach_score
            if mach_ans != 2:
                if man_ans == mach_ans:
                    mach_score += 1
                else:
                    man_score += 1
                # display_scores()

        def move(man):
            global p1, c1, p2, c2, moves, board_idx
            global a, gameboard

            if moves < 3:
                mach = 2
            else:
                if abs(a[p1, c1, p2, c2, 0] - a[p1, c1, p2, c2, 1]) <= 1.8 * pow(1.01, moves):
                    mach = 2
                elif a[p1, c1, p2, c2, 0] < a[p1, c1, p2, c2, 1]:
                    mach = 1
                else:
                    mach = 0

                a[p1, c1, p2, c2, man] += pow(1.1, moves)
                judge(man, mach)

            board_idx = moves % 15
            if board_idx == 0:
                zero_board()

            gameboard[0][board_idx] = '#' + str(moves)
            gameboard[1][board_idx] = str(man)
            gameboard[2][board_idx] = 'pass' if mach == 2 else str(mach)
            # print(" MACHINE : ", mach, "MAN", man)
            # display_board()

            c1, c2 = c2, mach
            p1, p2 = p2, man
            moves += 1
