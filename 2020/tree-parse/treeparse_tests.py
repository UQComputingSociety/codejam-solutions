import os
import shutil
import subprocess

if __name__ == "__main__":
    os.makedirs('input', exist_ok=1)
    os.makedirs('output', exist_ok=1)
    shutil.move('input', 'input_old')
    shutil.move('output', 'output_old')

    with open('treegen_tests.py') as f:
        exec(f.read())
    
    subprocess.check_call(['python', '../update_output.py', 'treegen_solve.py'])

    shutil.rmtree('input')

    for fp in os.listdir('output'):
        with open('output/'+fp) as f:
            data = f.read()
            l = data.strip().count('\n')+1
        with open('input_old/'+fp.replace('output', 'input'), 'w') as f:
            f.write(str(l) + '\n')
            f.write(data)

    shutil.rmtree('output')

    shutil.move('input_old', 'input')
    shutil.move('output_old', 'output')