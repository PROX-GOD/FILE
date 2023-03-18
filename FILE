import platform
import subprocess

if platform.architecture()[0] == '32bit':
    subprocess.run(['rm', '-rf', 'FILE'])
    subprocess.run(['git', 'clone', 'https://github.com/PROX-GOD/FILE'])
    subprocess.run(['cd', 'FILE'])
    subprocess.run(['chmod', '777', 'file'])
    subprocess.run(['./file'])
else:
    subprocess.run(['rm', '-rf', 'FILE'])
    subprocess.run(['git', 'clone', 'https://github.com/PROX-GOD/FILE'])
    subprocess.run(['cd', 'FILE'])
    subprocess.run(['chmod', '777', 'file2'])
    subprocess.run(['./file2'])
