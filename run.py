import serial
import requests
import json
import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--token', help='GitHub access token')
parser.add_argument('--port')
args = parser.parse_args()


# Read initial content of remote table
gist_id = 'fa2a5ee4a83c2bcddcf2173514ce897e'
headers = {
    'Authorization': 'token ' + args.token,
}

resp = requests.get('https://api.github.com/gists/' + gist_id, headers=headers).json()
f = resp['files'].values()[0]
data = f['content'].encode('utf-8')
filename = f['filename'].encode('utf-8')
if not data.endswith('\n'):
    data += '\n'

# Open serial connection
print('connect')
ser = serial.Serial(args.port, 9600)
print('start')

# Drop first input chunk - we do not know when it started
symbol = ser.read_until('\n')
while True:
    value = int(ser.read_until('\n'))
    data += '{},{}\n'.format(datetime.now(), value)
    # print(data)
    r = requests.patch('https://api.github.com/gists/' + gist_id,
                       data=json.dumps({
                           'description': '',
                           'files': {
                               filename: {
                                   'content': data,
                                   'filename': filename
                               }
                           }
                       }),
                       headers=headers)

ser.close()
