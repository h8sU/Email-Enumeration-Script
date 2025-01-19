# Email Enumeration Script

This Python script is designed to enumerate email addresses by sending POST requests to a specified target URL. The script identifies valid and invalid email addresses based on server responses.

## Features
- Customizable headers via command-line arguments.
- Simple to use with clear output.
- Supports bulk email enumeration from a file.

## Requirements
- Python 3.x
- `requests` library

Install the required library using:
```bash
pip install requests
```

## Usage

### Command Syntax
```bash
python3 script.py <email_list_file> --url <target_url> --host <host_header> --referer <referer_header> --origin <origin_header>
```

### Command-Line Arguments
- `<email_list_file>`: Path to the file containing email addresses (one email per line).
- `--url`: The target URL for the POST request.
- `--host`: Value for the `Host` header.
- `--referer`: Value for the `Referer` header.
- `--origin`: Value for the `Origin` header.

### Example
1. Create a file named `emails.txt` with the following content:
   ```
   test@example.com
   invalid@example.com
   valid@example.com
   ```

2. Run the script:
   ```bash
   python3 script.py emails.txt \
       --url http://enum.thm/labs/verbose_login/functions.php \
       --host web.com \
       --referer http://web.com/loginpage \
       --origin http://web.com
   ```

3. Example Output:
   ```
   [INVALID] test@example.com
   [VALID] valid@example.com
   [INVALID] invalid@example.com

   Valid emails found:
   valid@example.com
   ```

## How It Works
1. The script reads emails from the specified file.
2. Sends a POST request for each email to the target URL using the provided headers.
3. Parses the server's JSON response to determine the validity of the email.
4. Outputs valid and invalid emails in the console.

## Customization
You can adjust the script to match your specific use case by modifying the following:
- `invalid_error`: Customize the error message string to identify invalid emails.
- `data` dictionary: Adjust the POST request payload as needed.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
