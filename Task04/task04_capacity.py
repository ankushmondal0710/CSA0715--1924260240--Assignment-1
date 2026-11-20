import math
def nyquist(bandwidth_hz, levels):
    return 2 * bandwidth_hz * math.log2(levels)
def shannon(bandwidth_hz, snr_db):
    snr_ratio = 10 ** (snr_db / 10)
    return bandwidth_hz * math.log2(1 + snr_ratio)
for name, bw, snr in [("Telephone line",3100,30),("Cat6 pair",250e6,40),
                      ("Wi-Fi 6 channel",160e6,25)]:
    print(f"{name:<16} Shannon limit {shannon(bw,snr)/1e6:10.2f} Mbps")
print(f"Nyquist, 3,100 Hz with 4 levels: {nyquist(3100,4)/1e3:.1f} kbps")
print("250 MHz at 40 dB:", round(shannon(250e6,40)/1e6,2), "Mbps")
print("250 MHz at 15 dB:", round(shannon(250e6,15)/1e6,2), "Mbps")
print("Wi-Fi 160 MHz at 15 dB:", round(shannon(160e6,15)/1e6,2), "Mbps")
required_snr = 10*math.log10(2**(56000/3100)-1)
print("SNR needed for 56 kbps over 3100 Hz:", round(required_snr,2), "dB")
