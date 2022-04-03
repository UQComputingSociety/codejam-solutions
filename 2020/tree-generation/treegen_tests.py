import os
import random
import string

FOLDER_PARTS = [
    'System32', 'Windows', 'Microsoft', 'Drivers', 'SYSWOW64', 'Program Files', 'Program Files (x86)', 'Users', 'Riot Games',
    #'ProgramData', 'AppData', 'Games', '.minecraft', 'SteamLibrary', 'Documents', 'Desktop', 'Python38', 'jdk1.8.0_181',
]

FILE_NAMES = [
    'minecraft', 'explorer', 'cmd', 'chrome', 'firefox', 'spotify', 'data', 'codes', 'java', 'javaw', 'javac',
    'python', 'ghci', 'excel', 'winword'
]

FILE_EXTENSIONS = [
    '', '.exe', '.jar', '.bat', '.cmd', '.docx', '.doc'
]

def random_folder():
    p = 0.3
    s = []
    while not s or random.random() < p:
        s.append(random.choice(FOLDER_PARTS))
    return '/'.join(s)

def random_file():
    return random.choice(FILE_NAMES) + random.choice(FILE_EXTENSIONS)

def make_file_list():
    root = random.choice(FOLDER_PARTS)
    N_folders = random.randint(1, 100)
    folders = list(set(root + '/' + random_folder() for _ in range(N_folders)))
    N_files = random.randint(10, 1000)
    files = set(random.choice(folders) + '/' + random_file() for _ in range(N_files))
    
    return [str(len(files))] + list(files)
    

if __name__ == "__main__":
    os.makedirs('input', exist_ok=1)
    for n in range(10, 30):
        with open(f'input/input{n}.txt', 'w') as f:
            f.write('\n'.join(make_file_list()))