import sys
from typing import List


class Ocean:
    state: List[List[int]]

    def __init__(self, init_state: List[List[int]]):
        self.state = init_state

    def __str__(self) -> str:
        return "\n".join(["".join(str(el) for el in row) for row in self.state])

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.state!r})"

    def gen_next_quantum(self) -> "Ocean":
        fish = 2
        shrimp = 3
        new_state = []
        for i in range(len(self.state)):
            new_r = []
            for k in range(len(self.state[i])):
                if self.state[i][k] == 1:
                    new_r.append(1)
                else:
                    k_fish = 0
                    k_shrimp = 0
                    sosed = [
                    (i - 1, k - 1),
                    (i - 1, k),
                    (i - 1, k + 1),
                    (i, k - 1),
                    (i, k + 1),
                    (i + 1, k - 1),
                    (i + 1, k),
                    (i + 1, k + 1),
                ]
                for n_i, n_k in sosed:
                    if n_i < 0 or n_k < 0 or n_i >= len(self.state) or n_k >= len(self.state[i]):
                        continue
                    if self.state[n_i][n_k] == fish:
                        k_fish += 1
                    elif self.state[n_i][n_k] == shrimp:
                        k_shrimp += 1
                if k_fish == fish and k_shrimp == shrimp:
                    new_r.append(2)
                elif k_fish == 3:
                    new_r.append(2)
                else:
                    new_r.append(0)
                if self.state[i][k] == fish:
                    if k_fish < 2 or k_fish > 3:
                        new_r.append(0)
                    else:
                        new_r.append(2)
                elif self.state[i][k] == shrimp:
                    if k_shrimp < 2 or k_shrimp > 3:
                        new_r.append(0)
                    else:
                        new_r.append(3)

            new_state.append(new_r)

        return Ocean(init_state=new_state)



if __name__ == "__main__":
    n_quantums = int(sys.stdin.readline())
    n_rows, n_clms = (int(i) for i in sys.stdin.readline().split())
    init_state = []
    for i in range(n_rows):
        line = [int(i) for i in sys.stdin.readline().split()]
        init_state.append(line)

    ocean = Ocean(init_state=init_state)
    for _ in range(n_quantums):
        ocean = ocean.gen_next_quantum()
    print(ocean)
