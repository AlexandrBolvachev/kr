import argparse
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument('host', type=str)
parser.add_argument('port', type=str)
parser.add_argument('fname', type=str)
parser.add_argument('--word', default='', type=str)
parser.add_argument('--n', default=0, type=int)
args = parser.parse_args()

with open(args.fname) as f:
    customers = [json.loads(line) for line in f]
data = requests.get(f"http://{args.host}:{args.port}").json()
if args.word:
    for i in range(len(data)):
        data[i][1] += ' ' + args.word

for num, cust in enumerate(customers, 1):
    mas = []
    for i, elem in enumerate(data, args.n + 1):
        if any(word in elem[1] for word in cust['happened'].split()) and i % cust['urgency'] == 0:
            mas.append(elem[0])
    if mas:
        print(f'{num}: {", ".join(mas)}')
