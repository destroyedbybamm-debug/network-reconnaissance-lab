Network Reconnaissance Lab

Overview

A beginner-friendly Python cybersecurity project that demonstrates basic hostname resolution, local port checking, and scan report generation.

Features

Resolves a hostname to an IP address.

Retrieves basic hostname information.

Checks selected TCP ports on localhost.

Identifies ports that accept connections and ports that do not.

Saves scan output to a text report named scan_report.txt.

Handles hostname resolution errors.

Technologies

Python 3

Python socket library

Python datetime module

Linux / Ubuntu WSL

How to Run

Open a terminal in the project directory.

Run:

python3 network_scan.py

Enter localhost when prompted.

View the saved report:

cat scan_report.txt

Understanding the Results

OPEN: A service accepted a TCP connection on the tested port.

CLOSED: No service accepted the connection during the test.

ERROR: The check encountered an operating-system error.

A closed port is not necessarily a security issue, and an open port is not automatically a vulnerability.

Scope and Safety

This starter version is intended for learning and testing against the local computer only. It checks a limited set of TCP ports and is not a comprehensive vulnerability scanner.

Future Improvements

Add structured scan summaries.

Include scan duration and clearer error handling.

Add automated tests.

Improve report formatting and documentation.

Author

Cybersecurity student building practical Python and Linux security skills.
