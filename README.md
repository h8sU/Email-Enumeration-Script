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

## Customization
- **Target URL**: Update the `url` variable in the `check_email` function to match the desired endpoint.
- **Error Message**: Modify the `invalid_error` variable in the `enumerate_emails` function based on the server's response for invalid emails.
- **Headers**: Update the `headers` dictionary if the server requires specific values.

## Disclaimer
This script is intended for educational purposes only. Ensure you have proper authorization before using it against any target system. Unauthorized use may violate applicable laws and regulations.

