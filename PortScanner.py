import socket
from datetime import datetime

def scan_ports(target, start_port, end_port):
    print(f"\nScanning target: {target}")
    print(f"Scanning ports from {start_port} to {end_port}")
    print(f"Start Time: {datetime.now()}")
    print("-" * 50)

    for port in range(start_port, end_port + 1):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            s.close()
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
            break
        except socket.gaierror:
            print("Hostname could not be resolved.")
            break
        except socket.error:
            print("Could not connect to server.")
            break

    print("-" * 50)
    print(f"Scan completed at: {datetime.now()}")

if __name__ == "__main__":
    target = input("Enter the target IP address or domain: ").strip()
    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))

        if start_port < 0 or end_port > 65535 or start_port > end_port:
            print("❌ Invalid port range.")
        else:
            scan_ports(target, start_port, end_port)

    except ValueError:
        print("❌ Please enter valid integers for ports.")
