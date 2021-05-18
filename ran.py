import random
import json
import prime
import math
with open('prime.json', 'r') as openfile: 
	json_object = json.load(openfile)
# print(json_object)

temp = json_object["primes"]

p=random.choice(temp)
q=random.choice(temp)
print(p,q)
n = p * q
phi = (p-1)*(q-1)
