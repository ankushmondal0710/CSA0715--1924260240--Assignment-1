# Task 5: Mobility calculations; assume first coverage area is the starting cell.
route_m = 1200
wifi_spacing_m = 30
fiveg_cell_m = 300
wifi_handover_ms = 150
fiveg_handover_ms = 20
wifi_cells = route_m / wifi_spacing_m
fiveg_cells = route_m / fiveg_cell_m
wifi_handover_count = int(wifi_cells) - 1
fiveg_handover_count = int(fiveg_cells) - 1
print("Wi-Fi handovers:", wifi_handover_count)
print("Wi-Fi unreachable time:", wifi_handover_count*wifi_handover_ms, "ms")
print("5G handovers:", fiveg_handover_count)
print("5G unreachable time:", fiveg_handover_count*fiveg_handover_ms, "ms")
sensor_mbps = 600*50*8/1e6
print("All 600 sensors:", sensor_mbps, "Mbps =", sensor_mbps*1000, "kbps")
print("LoRa gateway capacity:", 5, "kbps; overload factor:", sensor_mbps*1000/5)
