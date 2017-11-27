import subprocess
import re
import nest
import sys
import config

access_token_cache_file = 'nest.json'

result = subprocess.check_output(['sensors', '-u'])
p = re.compile('.*temp._input: ..')
temps = p.findall(result.decode("utf-8"))

tempNum = []
for i in temps:
    tempNum.append(int(i[-2:]))

averageTemp = sum(tempNum) / len(tempNum)

if averageTemp > comparison_temp:
    print("Temperature is high!")
else:
    print("Temperature is averageTemp")

napi = nest.Nest(client_id=client_id, client_secret=client_secret, access_token_cache_file=access_token_cache_file)

if napi.authorization_required:
    print('Go to ' + napi.authorize_url + ' to authorize, then enter PIN below')
    if sys.version_info[0] < 3:
        pin = raw_input("PIN: ")
    else:
        pin = input("PIN: ")
    napi.request_token(pin)