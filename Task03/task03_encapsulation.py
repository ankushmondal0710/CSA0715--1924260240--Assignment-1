# Task 3: Simplified encapsulation model from assignment
LAYERS = [("Application", "HTTP"), ("Transport", "TCP"),
          ("Network", "IP"), ("Data link", "ETH")]
def send(message):
    pdu = message
    for layer, tag in LAYERS:
        if tag == "ETH":
            pdu = f"[{tag}|{pdu}|FCS]"
        else:
            pdu = f"[{tag}|{pdu}]"
        print(f"{layer:14s} adds {tag:<4s} -> {len(pdu)} bytes")
    return pdu
def receive(frame):
    pdu = frame
    for layer, tag in reversed(LAYERS):
        head, tail = "[" + tag + "|", ("|FCS]" if tag == "ETH" else "]")
        assert pdu.startswith(head) and pdu.endswith(tail), f"{layer}: bad header"
        pdu = pdu[len(head):-len(tail)]
    return pdu
message = "GET /results"
frame = send(message)
print("on the wire:", frame)
print("delivered :", receive(frame))
print("overhead   :", len(frame) - len(message), "bytes for", len(message), "bytes of data")
# Compare a 1,400-byte payload; this is a simplified string-length model.
large = "X" * 1400
large_frame = send(large)
large_overhead = len(large_frame) - len(large)
print(f"1400-byte payload overhead: {large_overhead} bytes ({large_overhead/len(large_frame)*100:.2f}% of frame)")
# Standard header accounting requested by the task (Ethernet 14 + FCS 4, IPv4 20, TCP 20)
for payload in (12, 1400):
    total = payload + 14 + 4 + 20 + 20
    overhead = total - payload
    print(f"Standard frame: payload={payload}, wire bytes={total}, overhead={overhead/total*100:.2f}%")
