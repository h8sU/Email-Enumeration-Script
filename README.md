# Email Enumeration Script

This repository contains a Python script for email enumeration by interacting with a login endpoint. It attempts to identify valid email addresses from a provided list using server responses.

## Features
- Sends login requests with a given email and a random password.
- Parses server responses to determine if the email is valid.
- Outputs the valid and invalid emails to the console.

## Requirements
- Python 3.x
- `requests` library

Install the required library using pip:
```bash
pip install requests
```

## Usage
1. Clone the repository or download the script.
2. Create a text file containing a list of emails (one email per line).
3. Run the script with the following command:
   ```bash
   python3 script.py <email_list_file>
   ```
   Replace `<email_list_file>` with the path to your email list file.

Example:
```bash
python3 script.py emails.txt
```

## Script Explanation
The script works by sending HTTP POST requests to a specified URL with the email address and a placeholder password. It parses the server's JSON response to identify valid and invalid emails based on predefined error messages.

### Code Overview
Below is the Python code with added comments to explain its functionality and indicate areas for customization.
