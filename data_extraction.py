#!/usr/bin/env python3
"""
data_extraction.py

This script demonstrates the use of regular expressions to validate and extract various types of data,
such as email addresses, URLs, phone numbers, credit card numbers, and time formats.
"""

import re

# -------------------------------
# REGEX PATTERNS FOR DATA EXTRACTION
# -------------------------------

# 1. Email Addresses
# Matches emails like "user@example.com" or "firstname.lastname@company.co.uk".
# Explanation:
# - The local part starts with one or more alphanumeric characters.
# - It may contain a period, underscore, plus, or dash as long as they are followed by more alphanumerics.
# - The domain contains alphanumerics and hyphens with at least one period followed by a valid TLD.
email_regex = re.compile(
    r'^[a-zA-Z0-9]+(?:[._+-][a-zA-Z0-9]+)*@[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+$'
)

# 2. URLs
# Matches URLs such as "https://www.example.com" or "http://subdomain.example.org/page".
# Explanation:
# - The URL starts with "http://" or "https://".
# - It allows one or more domain parts separated by dots.
# - Optionally, it can include a path with valid URL characters.
url_regex = re.compile(
    r'^https?://(?:[\w-]+\.)+[\w-]+(?:/[\w\-./?%&=]*)?$'
)

# 3. Phone Numbers (various formats)
# Matches:
#   - (123) 456-7890
#   - 123-456-7890
#   - 123.456.7890
# Explanation:
# - The area code can be enclosed in parentheses or not.
# - Separators between number groups can be a dash, dot, or space.
phone_regex = re.compile(
    r'^(?:\(\d{3}\)|\d{3})[-.\s]?\d{3}[-.\s]?\d{4}$'
)

# 4. Credit Card Numbers
# Matches:
#   - "1234 5678 9012 3456"
#   - "1234-5678-9012-3456"
# Explanation:
# - The pattern expects four groups of four digits.
# - Groups are separated by either a space or a dash. 
# - If you want to support numbers without delimiters, you could modify this pattern.
credit_card_regex = re.compile(
    r'^(?:\d{4}[- ]?){3}\d{4}$'
)

# 5. Time (24-hour and 12-hour formats)
# Matches:
#   - "14:30" (24-hour format)
#   - "2:30 PM" (12-hour format)
# Explanation:
# - Uses alternation to match either a 24-hour time (00:00 to 23:59)
#   or a 12-hour time with an AM/PM specifier.
# - The pattern is case-insensitive, so both "AM" and "am" are accepted.
time_regex = re.compile(
    r'^((([01]\d|2[0-3]):[0-5]\d)|((0?[1-9]|1[0-2]):[0-5]\d\s?(?:AM|PM)))$',
    re.IGNORECASE
)

# -------------------------------
# EDGE CASES & MALFORMED INPUT HANDLING
# -------------------------------
# For each regex, be aware of possible edge cases:
# - Email: Ensure that multiple consecutive dots or invalid characters do not pass.
# - URL: May not cover query parameters with special characters; consider enhancements if needed.
# - Phone: Input without any separators (like "1234567890") might be valid in some contexts.
# - Credit Card: Strictly checks for group delimiters; numbers without delimiters might be desired.
# - Time: Checks for valid hours and minutes but could be extended to check for a leading zero
#   in 12-hour format if desired.

# -------------------------------
# SAMPLE TEST CASES
# -------------------------------
test_strings = {
    "emails": [
        "user@example.com",
        "firstname.lastname@company.co.uk",
        "invalid_email@.com"  # Expected: NO MATCH
    ],
    "urls": [
        "https://www.example.com",
        "http://subdomain.example.org/page",
        "ftp://not-valid.com"  # Expected: NO MATCH
    ],
    "phone_numbers": [
        "(123) 456-7890",
        "123-456-7890",
        "123.456.7890",
        "1234567890"  # Depending on your criteria, this might need to be accepted.
    ],
    "credit_cards": [
        "1234 5678 9012 3456",
        "1234-5678-9012-3456",
        "1234567890123456"  # Without delimiters; modify pattern if needed.
    ],
    "times": [
        "14:30",
        "2:30 PM",
        "25:00",      # Expected: NO MATCH (Invalid hour)
        "02:60 AM"    # Expected: NO MATCH (Invalid minute)
    ]
}

def run_tests():
    """
    Test function to check each regex pattern against sample input strings.
    """
    # Mapping of test categories to corresponding regex patterns.
    patterns = {
        "emails": email_regex,
        "urls": url_regex,
        "phone_numbers": phone_regex,
        "credit_cards": credit_card_regex,
        "times": time_regex,
    }
    
    # Iterate over each category and sample string
    for category, regex in patterns.items():
        print(f"\nTesting {category.upper()}:")
        for sample in test_strings[category]:
            # regex.match() returns a match object if the sample fits the pattern.
            result = "MATCH" if regex.match(sample) else "NO MATCH"
            print(f"  {sample!r:30} -> {result}")

if __name__ == "__main__":
    run_tests()

