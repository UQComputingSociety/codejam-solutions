import os
import shutil

if __name__ == "__main__":
    os.makedirs('input', exist_ok=1)
    for f in os.listdir('outputx'):
        o = 'outputx/' + f
        dest = 'input/'+f.replace('output', 'input')
        shutil.copy(o, dest)
        with open(dest, 'r') as f:
            data = f.read()
            num = data.count('\n')
        with open(dest, 'w') as f:
            f.write(str(num)+'\n')
            f.write(data)
