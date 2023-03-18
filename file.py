import os, platform
os.system('git pull')
try:
    import requests
except:
    os.system('pip install requests')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    import file64
elif bit == '32bit':
    import file
