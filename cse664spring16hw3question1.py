fileName = ("cse664spring16hw3pwds")
fh = open(fileName)
#creating a dictionary of passwords
pwdCount = dict()
abc = list()
for line in fh:
    line = line.rstrip()
    pwdCount[line] = pwdCount.get(line,0) + 1
for pwd, count in pwdCount.items():
    abc.append((count,pwd))
#sorting the list in reverse order of frequencies
abc.sort(reverse=True)
#writing the output to file
for ans in abc:
    out = str(ans[0]) + " " + str(ans[1] + '\n')
    target = open('cse664spring16hw3Question1.txt', 'a')
    target.write(str(out))
print ('done')

