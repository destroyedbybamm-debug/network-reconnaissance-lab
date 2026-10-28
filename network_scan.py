import socket
from datetime import datetime

report_lines = []


def log(message):
    print(message)
    report_lines.append(message)


log("=== Network Reconnaissance Lab ===")
log(f"Scan started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

target = input(
    "Enter a hostname or IP address you own or have permission to test: "
)

try:
    ip_address = socket.gethostbyname(target)
    log(f"\nTarget: {target}")
    log(f"Resolved IP address: {ip_address}")
    log(f"Hostname: {socket.getfqdn(target)}")

    log("\n=== Local Port Check ===")

    if ip_address == "127.0.0.1":
        ports_to_check = [22, 80, 443, 3000, 5000, 8000]

        for port in ports_to_check:
            try:
                with socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM
                ) as sock:
                    sock.settimeout(0.5)
                    result = sock.connect_ex(("127.0.0.1", port))

                if result == 0:
                    log(f"[OPEN] Port {port} accepts connections.")
                else:
                    log(f"[CLOSED] Port {port} did not accept a connection.")

            except OSError as error:
                log(f"[ERROR] Port {port}: {error}")
    else:
        log("Port checks are limited to localhost in this version.")

except socket.gaierror:
    log("Error: Could not resolve that hostname or IP address.")

log("\nReconnaissance complete.")

with open("scan_report.txt", "w", encoding="utf-8") as report_file:
    report_file.write("\n".join(report_lines) + "\n")

print("Report saved to scan_report.txt")
