# Log Analysis Script
## Overview:
The Log Analysis Script is a Python tool designed to parse web server logs, analyze the data, and provide insights such as the number of requests per IP address, the most accessed endpoint, and potential suspicious activity based on failed login attempts. Results are displayed in the terminal and saved to a CSV file for further analysis.

## Features:
- **IP Address Request Count**: Counts the number of requests made by each IP address.
- **Most Accessed Endpoint**: Identifies the endpoint that was accessed most frequently.
- **Failed Login Attempts**: Detects IP addresses with failed login attempts exceeding a configurable threshold.
- **CSV Report Generation**: Saves the analyzed data into a structured CSV file.

## Requirements:
- Python 3.6 or higher
- Required Python modules:
  - re
  - csv
  - collections

## Installation: 
- Clone or download this repository to your local machine (git@github.com:A-Y12/VRV_Assignment.git)
- Ensure Python 3.6 or higher is installed.
- Install any required modules using the following command:
  - pip install -r requirements.txt
(No additional libraries are required for this script, as it uses Python's standard library.)

## Usage
### configuring the Script
#### Log File Path:
- Update the LOG_FILE variable in the script to point to the web server log file you wish to analyze. 
- Example:LOG_FILE = 'path/to/your/logfile.log'
#### Output File Path:
- Set the OUTPUT_FILE variable to specify the desired name and location of the output CSV file. 
- Example:OUTPUT_FILE = 'path/to/output/log_analysis_results.csv'
#### Failed Login Threshold:
- Modify the FAILED_LOGIN_THRESHOLD to adjust the number of failed login attempts considered suspicious. ---- 
- Example:FAILED_LOGIN_THRESHOLD = 3(here) or 10.

### Running the Script
- Run the script using the following command:
  - python log_analysis_script.py

### Output
- **Terminal Output**:
  - Displays:
    - Request counts for each IP address.
    - The most accessed endpoint and its count.
    - Suspicious activity with failed login attempts exceeding the threshold.

- **CSV File**:
  - Contains:
    - IP Address and request counts.
    - Most accessed endpoint and access count.
    - Suspicious activity details.

## Example
### Input Log File (sample.log):
- 192.168.1.1 - - [03/Dec/2024:10:12:34 +0000] "GET /home HTTP/1.1" 200 512
- 203.0.113.5 - - [03/Dec/2024:10:12:35 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 10.0.0.2 - - [03/Dec/2024:10:12:36 +0000] "GET /about HTTP/1.1" 200 256
- 192.168.1.1 - - [03/Dec/2024:10:12:37 +0000] "GET /contact HTTP/1.1" 200 312
- 198.51.100.23 - - [03/Dec/2024:10:12:38 +0000] "POST /register HTTP/1.1" 200 128
- 203.0.113.5 - - [03/Dec/2024:10:12:39 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 192.168.1.100 - - [03/Dec/2024:10:12:40 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 10.0.0.2 - - [03/Dec/2024:10:12:41 +0000] "GET /dashboard HTTP/1.1" 200 1024
- 198.51.100.23 - - [03/Dec/2024:10:12:42 +0000] "GET /about HTTP/1.1" 200 256
- 192.168.1.1 - - [03/Dec/2024:10:12:43 +0000] "GET /dashboard HTTP/1.1" 200 1024
- 203.0.113.5 - - [03/Dec/2024:10:12:44 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 203.0.113.5 - - [03/Dec/2024:10:12:45 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 192.168.1.100 - - [03/Dec/2024:10:12:46 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 10.0.0.2 - - [03/Dec/2024:10:12:47 +0000] "GET /profile HTTP/1.1" 200 768
- 192.168.1.1 - - [03/Dec/2024:10:12:48 +0000] "GET /home HTTP/1.1" 200 512
- 198.51.100.23 - - [03/Dec/2024:10:12:49 +0000] "POST /feedback HTTP/1.1" 200 128
- 203.0.113.5 - - [03/Dec/2024:10:12:50 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 192.168.1.1 - - [03/Dec/2024:10:12:51 +0000] "GET /home HTTP/1.1" 200 512
- 198.51.100.23 - - [03/Dec/2024:10:12:52 +0000] "GET /about HTTP/1.1" 200 256
- 203.0.113.5 - - [03/Dec/2024:10:12:53 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 192.168.1.100 - - [03/Dec/2024:10:12:54 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 10.0.0.2 - - [03/Dec/2024:10:12:55 +0000] "GET /contact HTTP/1.1" 200 512
- 198.51.100.23 - - [03/Dec/2024:10:12:56 +0000] "GET /home HTTP/1.1" 200 512
- 192.168.1.100 - - [03/Dec/2024:10:12:57 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 203.0.113.5 - - [03/Dec/2024:10:12:58 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 10.0.0.2 - - [03/Dec/2024:10:12:59 +0000] "GET /dashboard HTTP/1.1" 200 1024
- 192.168.1.1 - - [03/Dec/2024:10:13:00 +0000] "GET /about HTTP/1.1" 200 256
- 198.51.100.23 - - [03/Dec/2024:10:13:01 +0000] "POST /register HTTP/1.1" 200 128
- 203.0.113.5 - - [03/Dec/2024:10:13:02 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 192.168.1.100 - - [03/Dec/2024:10:13:03 +0000] "POST /login HTTP/1.1" 401 128 "Invalid credentials"
- 10.0.0.2 - - [03/Dec/2024:10:13:04 +0000] "GET /profile HTTP/1.1" 200 768
- 198.51.100.23 - - [03/Dec/2024:10:13:05 +0000] "GET /about HTTP/1.1" 200 256
- 192.168.1.1 - - [03/Dec/2024:10:13:06 +0000] "GET /home HTTP/1.1" 200 512
- 198.51.100.23 - - [03/Dec/2024:10:13:07 +0000] "POST /feedback HTTP/1.1" 200 128

### Terminal Output:
- IP Address Request Count:
IP Address            Request Count
203.0.113.5                       8
198.51.100.23                     8
192.168.1.1                       7
10.0.0.2                          6
192.168.1.100                     5

Most Frequently Accessed Endpoint:
/login (Accessed 13 times)

Suspicious Activity Detected:
IP Address          Failed Login Attempts
203.0.113.5                            8
192.168.1.100                          5

Process finished with exit code 0

### CSV Output (log_analysis_results.csv):
IP Address	Request Count
203.0.113.5	      8
198.51.100.23	      8
192.168.1.1	      7
10.0.0.2	      6
192.168.1.100	      5
	
Most Accessed Endpoint	Access Count
/login	 13
	
IP Address	Failed Login Count
203.0.113.5	            8
192.168.1.100	            5


## Customization
Additional Parsing Rules:
Extend the parse_log_file function to handle other log patterns.
CSV Output:
Modify the save_results_to_csv function to include additional data as needed.

## Limitations
Assumes a specific log format. For non-standard log files, the regex patterns may need adjustments.
Processes logs line by line and may require optimization for extremely large files.

## Troubleshooting
File Not Found Error:
Ensure the LOG_FILE path is correct and the file exists.
Incorrect Results:
Verify that the log file matches the expected format (IP address, HTTP method, status code, etc.).
Encoding Issues:
Use UTF-8 encoding or adjust the open function to handle other encodings with errors='replace'.

## Contribution
Feel free to fork this repository and submit pull requests for enhancements or bug fixes.
