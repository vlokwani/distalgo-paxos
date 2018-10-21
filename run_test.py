import subprocess
import json

cmd = ['python', '-m', 'da', 'main.da']

proc = subprocess.run(cmd, stdout=subprocess.PIPE)
output = str(proc.stdout).strip()[13:-3]
print("Print output returned by main.da: ")
# print(output)
print(json.loads(output))