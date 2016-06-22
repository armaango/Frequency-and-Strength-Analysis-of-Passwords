# For 2.7
from __future__ import division
from collections import Counter
from math import log

#creating a single string of the passwords to compute the length
file = open('cse664spring16hw3pwds', 'r')
passwords = ""
c = 0
for line in file:
    passwords += line
passwords = passwords.strip()
file.close()

print 'pre part done'
# part1- question 2- using the entire file as base
count = 0
password_list = passwords.split('\n')
passwords = passwords.replace('\n', '')
total = len(passwords)
counter = Counter(passwords)
output = open('cse664spring16hw3Question2.txt', 'w')
password_entropy = dict()
for password in password_list:
    entropy = 0.0
    pass1 = ''.join(set(password))
    for character in pass1:
        entropy += -(counter[character]/total)*log((counter[character]/total), 2)
    password_entropy[password] = entropy
    print count
    count+=1

for password in sorted(password_entropy, key=password_entropy.get, reverse=True):
    output.write(str(password_entropy[password]) + '\t' + password + '\n')

output.close()
print('done-part 1')
#part 1 ends here, output for question 2 is generated


#2 Part 2- using the unique passwords as base for calculation
count = 0
password_list = set(password_list)
passwords = ''.join(password_list)
total = len(passwords)
counter = Counter(passwords)
output = open('cse664spring16hw3Question3.txt', 'w')
password_entropy = dict()
for password in password_list:
    entropy = 0.0
    pass1 = ''.join(set(password))
    for character in pass1:
        entropy += -(counter[character]/total)*log((counter[character]/total), 2)
    password_entropy[password] = entropy

for password in sorted(password_entropy, key=password_entropy.get, reverse=True):
    output.write(str(password_entropy[password]) + '\t' + password + '\n')
output.close()
print('done-part 2')