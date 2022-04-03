import random
import string

if __name__ == "__main__":
    for n in range(50):
        with open(f'input/input{n}.txt', 'w') as f:
            N = random.randint(0, 26)
            letters = random.sample(string.ascii_uppercase, N)
            random.shuffle(letters)
            print(N, file=f)
            print('\n'.join(letters), file=f)