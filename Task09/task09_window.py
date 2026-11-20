import math
def utilisation(frame_bits, rate_bps, distance_m, window, speed=2e8):
    tx=frame_bits/rate_bps
    prop=distance_m/speed
    a=prop/tx
    u=min(1.0,window/(1+2*a))
    return u,a
for name,rate,dist in [("Campus LAN, 200 m, 1 Gbps",1e9,200),
                       ("City fibre, 50 km, 1 Gbps",1e9,50000),
                       ("Satellite, 36,000 km, 10 Mbps",10e6,36000000)]:
    u1,a=utilisation(12000,rate,dist,1)
    u7,_=utilisation(12000,rate,dist,7)
    u127,_=utilisation(12000,rate,dist,127)
    print(f"{name:<31} a = {a:7.2f} stop-and-wait {u1:6.1%} W=7 {u7:6.1%} W=127 {u127:6.1%}")
# Head-office link
u,a=utilisation(12000,1e9,400000,1)
window=math.ceil(1+2*a)
print("Head-office tx time:",12000/1e9*1e6,"us")
print("Head-office propagation:",400000/2e8*1000,"ms one-way")
print("Head-office a:",a,"stop-and-wait utilisation:",f"{u*100:.3f}%")
print("Minimum full-utilisation window:",window)
print("Go-Back-N sequence bits:",math.ceil(math.log2(window+1)))
print("Selective Repeat sequence bits:",math.ceil(math.log2(2*window)))
u64,_=utilisation(12000,1e9,400000,64)
print("SR W=64 utilisation:",f"{u64*100:.2f}%","throughput:",f"{u64*1000:.2f} Mbps")
print("SR W=64 receiver buffer:",64*1500,"bytes")
# Satellite full window
sat_u,sat_a=utilisation(12000,10e6,36000000,1)
print("Satellite minimum window:",math.ceil(1+2*sat_a))
