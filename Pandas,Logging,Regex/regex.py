import re

# Example text
text = "Hello, my email is rehan@gmail.com and my phone number is 0306-0603253."

# Regex patterns
email_pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
phone_pattern = r"\d{4}-\d{7}"

# Find email addresses in the text
emails = re.findall(email_pattern, text)
print("Emails found:")
for email in emails:
    print(email)

# Find phone numbers in the text
phones = re.findall(phone_pattern, text)
print("\nPhone numbers found:")
for phone in phones:
    print(phone)

text = "Visit our website at https://www.example.com to learn more"

url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"

urls = re.findall(url_pattern, text)
print("\n link found:")
print(urls)
