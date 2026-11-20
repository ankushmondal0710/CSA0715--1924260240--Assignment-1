from itertools import combinations
def encode(d):
    p1=d[0]^d[1]^d[3]
    p2=d[0]^d[2]^d[3]
    p3=d[1]^d[2]^d[3]
    return [p1,p2,d[0],p3,d[1],d[2],d[3]]
def decode(c):
    s1=c[0]^c[2]^c[4]^c[6]
    s2=c[1]^c[2]^c[5]^c[6]
    s3=c[3]^c[4]^c[5]^c[6]
    pos=s1+2*s2+4*s3
    if pos:
        c[pos-1]^=1
    return pos,[c[2],c[4],c[5],c[6]]
word=encode([1,0,1,1])
print("codeword        :","".join(map(str,word)))
for flip in (None,5):
    rx=word[:]
    if flip: rx[flip-1]^=1
    pos,data=decode(rx)
    print(f"error at {str(flip):<4}: syndrome {pos}, data {''.join(map(str,data))}")
# Two-bit error demonstration: decoder may miscorrect a double-bit error.
rx=word[:]
rx[0]^=1; rx[1]^=1
pos,data=decode(rx)
print("two-bit corruption, decoder syndrome:",pos,"decoded data:",''.join(map(str,data)))
# Minimum distance of supplied code
codes=["00000","01011","10101","11110"]
distances=[sum(x!=y for x,y in zip(a,b)) for a,b in combinations(codes,2)]
dmin=min(distances)
print("minimum distance:",dmin,"detect:",dmin-1,"correct:",(dmin-1)//2)
# For 16 data bits, smallest r satisfying 2^r >= 16+r+1
r=0
while 2**r < 16+r+1: r+=1
print("check bits for 16 data bits:",r,"overhead of 21-bit codeword:",f"{r/(16+r)*100:.2f}%")
