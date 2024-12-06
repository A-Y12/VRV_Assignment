import re
import csv
from collections import Counter

# Configurable Threshold
FAILED_LOGIN_THRESHOLD = 3

# File Paths
LOG_FILE = r'C:\Users\kumar\Downloads\sample.log'
OUTPUT_FILE = 'log_analysis_results.csv'


def parse_log_file(file_path):
    """
    Parses the log file and extracts data for IP requests, endpoints, and failed login attempts.

    Args:
        file_path (str): Path to the log file.

    Returns:
        tuple: Three Counters for IP requests, endpoint access counts, and failed login attempts.
    """
    ip_requests = Counter()
    endpoint_requests = Counter()
    failed_logins = Counter()

    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        for line in file:
            # Extract IP Address
            ip_match = re.match(r"^(\S+)", line)
            ip = ip_match.group(1) if ip_match else None
            if ip:
                ip_requests[ip] += 1

            # Extract Endpoint
            endpoint_match = re.search(r'"\S+ (\S+) HTTP', line)
            endpoint = endpoint_match.group(1) if endpoint_match else None
            if endpoint:
                endpoint_requests[endpoint] += 1

            # Detect Failed Login Attempts
            if '401' in line or 'Invalid credentials' in line and ip:
                failed_logins[ip] += 1

    return ip_requests, endpoint_requests, failed_logins


def save_results_to_csv(ip_requests, most_accessed, failed_logins):
    """
    Saves the analysis results to a CSV file.

    Args:
        ip_requests (Counter): Counts of requests per IP.
        most_accessed (tuple): The most accessed endpoint and its count.
        failed_logins (Counter): Counts of failed login attempts per IP.
    """
    with open(OUTPUT_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write IP Request Count
        writer.writerow(['IP Address', 'Request Count'])
        writer.writerows(ip_requests.most_common())

        writer.writerow([])  # Blank line

        # Write Most Accessed Endpoint
        writer.writerow(['Most Accessed Endpoint', 'Access Count'])
        writer.writerow(most_accessed)

        writer.writerow([])  # Blank line

        # Write Suspicious Activity
        writer.writerow(['IP Address', 'Failed Login Count'])
        writer.writerows([(ip, count) for ip, count in failed_logins.items() if count > FAILED_LOGIN_THRESHOLD])


def display_results(ip_requests, most_accessed, failed_logins):
    """
    Displays the analysis results in the terminal.

    Args:
        ip_requests (Counter): Counts of requests per IP.
        most_accessed (tuple): The most accessed endpoint and its count.
        failed_logins (Counter): Counts of failed login attempts per IP.
    """
    print("\nIP Address Request Count:")
    print(f"{'IP Address':<20}{'Request Count':>15}")
    for ip, count in ip_requests.most_common():
        print(f"{ip:<20}{count:>15}")

    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed[0]} (Accessed {most_accessed[1]} times)")

    print("\nSuspicious Activity Detected:")
    print(f"{'IP Address':<20}{'Failed Login Attempts':>20}")
    for ip, count in failed_logins.items():
        if count > FAILED_LOGIN_THRESHOLD:
            print(f"{ip:<20}{count:>20}")


def main():
    """
    Main function to run the log analysis.
    """
    # Parse the log file
    ip_requests, endpoint_requests, failed_logins = parse_log_file(LOG_FILE)

    # Identify the most accessed endpoint
    most_accessed = endpoint_requests.most_common(1)[0] if endpoint_requests else ('None', 0)

    # Display results
    display_results(ip_requests, most_accessed, failed_logins)

    # Save results to CSV
    save_results_to_csv(ip_requests, most_accessed, failed_logins)


if __name__ == "__main__":
    main()
