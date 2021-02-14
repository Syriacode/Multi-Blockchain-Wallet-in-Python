import subprocess

import json

command = 'hd-wallet-derive.php -g --mnemonic="cram cable breeze tomato wire garment sting apology enemy tool noble oak" --cols=path,address,privkey,pubkey --format=json'

p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
output, err = p.communicate()
p_status = p.wait()

print(output)