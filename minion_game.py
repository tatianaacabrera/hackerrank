string = 'BANANA'
s=len(string)
vowel = 0
consonant = 0

for i in range(s):
    if string[i] in 'AEIOU':
        subs = string[i:]
        vowel += len(subs)
    else:
        subs = string[i:]
        consonant += len(subs)
            
if vowel < consonant:
    print('Stuart ' + str(consonant))
elif vowel > consonant:
    print('Kevin ' + str(vowel))
else:
    print('Draw')