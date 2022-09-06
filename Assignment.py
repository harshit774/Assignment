#creating a dictionary to mapping opposite character
h={'A':'Z','B':'Y','C':'X','D':'W','E':'V','F':'U','G':'T','H':'S','I':'R','J':'Q','K':'P','L':'O','M':'N'}
h1={'Z': 'A', 'Y': 'B', 'X': 'C', 'W': 'D', 'V': 'E', 'U': 'F', 'T': 'G', 'S': 'H', 'R': 'I', 'Q': 'J', 'P': 'K', 'O': 'L', 'N': 'M'}

# for encoding
def encoding(s):
    res = '' # to store the answer
    for i in s: 
        if ord(i) % 2 == 1: # ASCII value if odd
            if i in h.keys(): # 
                res += h[i]
            else:
                res += h1[i]
        else:
            res += i
            if i in h.keys():
                res += h[i]
            else:
                res += h1[i]
    print(res)
    
# for decoding    
def decoding(s):
    for i in range(len(s) - 1):
        if (ord(s[i]) % 2) == 1:
            s = s.replace(s[i - 1], '')
    res = ''
    for i in range(len(s)):
        if ord(s[i]) % 2 == 0:
            if s[i] in h.keys():
                res += h[s[i]]
            else:
                res += h1[s[i]]
        else:
            if s[i] in h.keys():
                res += h[s[i]]
            else:
                res += h1[s[i]]
    print(res)
    
# main function    
print("Enter String:")
s=input()
print("choose \n 1.encode 2.decode")
t=int(input())
if t==1:
    encoding(s)
elif t==2:
    decoding(s)
else:
    print('wrong choice')