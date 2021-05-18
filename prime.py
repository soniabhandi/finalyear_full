import json

lower = 1000
upper = 1500

# print("Prime numbers between", lower, "and", upper, "are:")
a = []
for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
       		a.append(num)

temp = {
	"primes" : a
}
with open("prime.json", "w") as outfile: 
	json.dump(temp, outfile)