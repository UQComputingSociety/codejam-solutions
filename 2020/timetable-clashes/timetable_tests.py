import random 
import itertools

counter = itertools.count()

if __name__ == "__main__":
    for i in range(20):
        N = random.randint(2, 10)

        with open(f'input/input{i}.txt', 'w') as f:
            print(N, file=f)
            for j in range(N):
                randint = random.randint
                id, h, m, d = next(counter), randint(0, 23), randint(0, 59), randint(1, 240)
                print(id, h, m, d, file=f)
