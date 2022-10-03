# Author: Xiaoxuan
# Date: 9/23/2022
# Purpose: a description of the search problem.
# Chickens and foxes need to cross a river.
# There is one boat with capacity 2.
# If there are fewer chickens than foxes on either side of the river, those chickens are eaten.
class FoxProblem:
    # state: the number of chickens, foxes, and boat on the starting side
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        self.total_chicken = start_state[0]
        self.total_fox = start_state[1]

    def get_successors(self, state):
        # generate, test, add
        successors = []
        chicken, fox, boat = state[0], state[1], state[2]
        if boat == 1:
            children = [(chicken - 1, fox, 0), (chicken, fox - 1, 0), (chicken - 2, fox, 0),
                        (chicken, fox - 2, 0), (chicken - 1, fox - 1, 0)]
            for child in children:
                if self.legality_test(child):
                    successors.append(child)
        if boat == 0:
            children = [(chicken + 1, fox, 1), (chicken, fox + 1, 1), (chicken + 2, fox, 1),
                        (chicken, fox + 2, 1), (chicken + 1, fox + 1, 1)]
            for child in children:
                if self.legality_test(child):
                    successors.append(child)
        return successors

    # make sure a state is safe
    def legality_test(self, state):
        chicken, fox = state[0], state[1]
        if chicken < 0 or fox < 0:
            return False
        if chicken > self.total_chicken or fox > self.total_fox:
            return False
        if chicken != 0 and chicken < fox:
            return False
        if self.total_chicken - chicken != 0 and self.total_chicken - chicken < self.total_fox - fox:
            return False
        return True

    # test whether we have reached the goal
    def goal_test(self, state):
        return state == self.goal_state

    def __str__(self):
        string = "Chickens and foxes problem: " + str(self.start_state)
        return string


if __name__ == "__main__":
    test_cf = FoxProblem((5, 5, 1))
    print(test_cf.get_successors((5, 5, 1)))
    print(test_cf)
