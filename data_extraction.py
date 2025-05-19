"""
data_extraction.py

This script demonstrates the use of regular expressions to validate and extract various types of data,
such as email addresses, URLs, phone numbers, credit card numbers, and time formats.
"""

import re

email_regex = re.compile(
    r'^[a-zA-Z0-9]+(?:[._+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+$'
)

url_regex = re.compile(
    r'^https?://(?:[\w-]+\.)+[\w-]+(?:/[\w\-./?%&=]*)?$'
)

phone_regex = re.compile(
    r'^(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$'
)

credit_card_regex = re.compile(
    r'^(?:\d{4}[- ]?){3}\d{4}$'
)

time_regex = re.compile(
    r'^((([01]\d|2[0-3]):[0-5]\d)|((0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM)))$',
    re.IGNORECASE
)

test_strings = {
    "emails": [
        "user@example.com",
        "firstname.lastname@company.co.uk",
        "invalid_email@.com"  
    ],
    "urls": [
        "https://www.example.com",
        "http://subdomain.example.org/page",
        "ftp://not-valid.com" 
    ],
    "phone_numbers": [
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "1234567890"
    ],
    "credit_cards": [
        "1234 5678 9012 3456",
        "1234-5678-9012-3456",
        "1234567890123456" 
    ],
    "times": [
        "14:30",
        "2:30 PM",
        "25:00",   
        "02:60 AM" 
    ]
}

def run_tests():
    """
    Test function to check each regex pattern against sample input strings.
    """
    patterns = {
        "emails": email_regex,
        "urls": url_regex,
        "phone_numbers": phone_regex,
        "credit_cards": credit_card_regex,
        "times": time_regex,
    }
    
    for category, regex in patterns.items():
        print(f"\nTesting {category.upper()}:")
        for sample in test_strings[category]:
            result = "MATCH" if regex.match(sample) else "NO MATCH"
            print(f"  {sample!r:30} -> {result}")

if __name__ == "__main__":
    run_tests()

