import re
 
text = "Please contact us at support@example.com or sales@example.org."
 
# Regular expression to match email addresses
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
# Find all email addresses
emails = re.findall(email_pattern, text)
print(emails)
