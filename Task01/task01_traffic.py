# Task 1: Traffic sizing (all rates are decimal Mbps)
robot = 40 * 200 * 8 / 0.002 / 1_000_000
sensors = 600 * 50 * 8 / 1 / 1_000_000
cctv = 24 * 4
office = 150 * 0.10 * 2
line_total = robot + sensors + cctv + office
plant_total = line_total * 8
cctv_event = cctv * 0.05
alt_line = robot + sensors + cctv_event + office
alt_plant = alt_line * 8
for name, value in [("Robots", robot), ("Sensors", sensors), ("CCTV", cctv),
                    ("Office", office), ("One line total", line_total),
                    ("Eight-line plant", plant_total),
                    ("Alternative one line", alt_line),
                    ("Alternative eight-line plant", alt_plant)]:
    print(f"{name:25s}: {value:.2f} Mbps")
print("1 Gbps uplink sufficient for original peak:", plant_total <= 1000)
print("1 Gbps uplink sufficient for local CCTV:", alt_plant <= 1000)
