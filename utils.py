import re

def validate_reddit_url(url: str) -> str:
    pattern = r"https?://(www\.)?reddit\.com/user/(?P<username>[\w-]+)/comments/?$"
    match = re.match(pattern, url.strip())
    if not match:
        raise ValueError("Invalid Reddit URL. Only comment URLs are supported.")
    return match.group("username")