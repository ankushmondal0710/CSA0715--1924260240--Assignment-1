def mod2_div(dividend, divisor):
    rem = list(dividend)
    for i in range(len(dividend) - len(divisor) + 1):
        if rem[i] == "1":
            for j in range(len(divisor)):
                rem[i+j] = "0" if rem[i+j] == divisor[j] else "1"
    return "".join(rem[-(len(divisor)-1):])
def encode(data, gen):
    return data + mod2_div(data + "0"*(len(gen)-1), gen)
def check(frame, gen):
    return set(mod2_div(frame, gen)) == {"0"}
GEN="1011"
data="1101011011"
frame=encode(data,GEN)
print("transmitted:",frame)
print("no error   :",check(frame,GEN))
bad=frame[:4]+("1" if frame[4]=="0" else "0")+frame[5:]
print("1-bit error:",check(bad,GEN))
burst=frame[:2]+"".join("1" if b=="0" else "0" for b in frame[2:5])+frame[5:]
print("3-bit burst:",check(burst,GEN))
undetected = "1011000000000"  # x^9 multiplied by generator polynomial 1011
print("undetected error pattern:", undetected, "remainder:", mod2_div(undetected,GEN))
print("undetected pattern accepted as zero remainder:", check(undetected,GEN))
# Internet checksum: one's-complement sum of the four supplied 16-bit words.
words=[0x4500,0x0073,0x0000,0x4000]
total=sum(words)
while total >> 16:
    total=(total & 0xffff)+(total >> 16)
print(f"Internet checksum: {((~total)&0xffff):04X}")
