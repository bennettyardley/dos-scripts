import sys
import subprocess

procs = []
for i in range(500):
    proc = subprocess.Popen([sys.executable, 'connector.py', '{}in.csv'.format(i), '{}out.csv'.format(i)])
    procs.append(proc)

for proc in procs:
    proc.wait()
