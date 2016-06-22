import hashlib

fh = open("cse664spring16hw3pwds")
count = 0
#creating a set of the hash values to be checked
hashesset=["ba931c15ec0163c4bb339f41571694ce","c9cd905fc459e5550b8c3b01d4346c25","e9269d9e52a692f52caece9d0e7cdae1","660719b4a7591769583a7c8d20c6dfa4"]
for line in fh:
    line = line.rstrip()
    pwd = line.encode('utf-8')
    if hashlib.md5(pwd).hexdigest() in hashesset:
        out = str(hashlib.md5(pwd).hexdigest() + '\t') + str((pwd) + '\n')
        count = count + 1
        target = open('cse664spring16hw3Question4.txt', 'a')
        target.write(str(out))
        hashesset.remove(str(hashlib.md5(pwd).hexdigest()))
    if count == 4:
        break

print('done')