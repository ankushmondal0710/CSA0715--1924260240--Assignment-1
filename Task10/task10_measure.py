# Run this on your own computer; outputs depend on your network and target.
# Windows: python task10_measure.py; Linux/macOS: python3 task10_measure.py
import platform, subprocess
target=input("Enter a host you are allowed to test (e.g. 1.1.1.1): ").strip()
if not target:
    raise SystemExit("No target entered.")
commands = (["ping","-n","4",target] if platform.system()=="Windows"
            else ["ping","-c","4",target])
print("\\n--- PING ---")
subprocess.run(commands)
print("\\n--- TRACEROUTE ---")
trace = (["tracert",target] if platform.system()=="Windows"
         else ["traceroute",target])
try:
    subprocess.run(trace)
except FileNotFoundError:
    print("Traceroute utility not installed. On Ubuntu/Debian: sudo apt install traceroute")
