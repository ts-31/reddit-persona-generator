import re


def extract_username(input_str):
    input_str = input_str.strip()
    match = re.search(r"reddit\.com/user/([^/]+)/?", input_str)
    return match.group(1) if match else input_str
