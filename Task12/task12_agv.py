# Explicit assumption for illustration: each AGV uses the same 200-byte/2-ms
# command pattern as a robot controller. The assignment does not specify AGV rate.
agvs=50
per_agv_mbps=200*8/0.002/1e6
agv_total=agvs*per_agv_mbps
original_line=158.24
print("Assumed traffic per AGV:",per_agv_mbps,"Mbps")
print("50 AGVs added:",agv_total,"Mbps")
print("One-line traffic if added to one line:",original_line+agv_total,"Mbps")
print("Eight-line traffic if 50 AGVs are plant-wide:",158.24*8+agv_total,"Mbps")
print("Eight-line traffic if 50 AGVs are added per line:",(158.24+agv_total)*8,"Mbps")
print("Task 5 5G handover interruption for 1.2 km route:",3*20,"ms")
print("Decision: use private 5G URLLC for AGV mobility, wired industrial Ethernet/fibre for fixed critical control.")
