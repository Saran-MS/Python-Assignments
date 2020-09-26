import re

total = 0
confidence = 0
result = 0

file = open('mbox-short.txt')
for i in file:
    i = i.rstrip()
    conf = re.search('X-DSPAM-Confidence: ([\d.]+)', i)
    if conf:
        total += float(conf.group(1))
        confidence += 1
        
    if re.search('X-DSPAM-Result:', i):
        changed = re.sub(r'X-DSPAM-Result: (.*)', r'X-DSPAM-Outcome: \1', i)
        result += 1
        print(changed)

print()
print('X-DSPAM-Result to X-DSPAM-Outcome : {} times'.format(result))
print('Total Confidence :', total)
print('Count :',confidence)
print('Average Confidence :', total / confidence)
