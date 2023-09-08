import random

class HeaderGenerator:
    def __init__(self):
        self.headers = {
            "User-Agent": [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
                "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36",
            ],
            'Authority': ["www.walmart.ca"],
            "Accept": ["*/*"],
            "Accept-Encoding": ["gzip, deflate"],
            "Connection": ["keep-alive"],
            "Cache-Control": ["max-age=0"],
            "DNT": ["1"],
            "Upgrade-Insecure-Requests": ["1"],
        }

    def generate_headers(self):
        headers = {}
        for key, values in self.headers.items():
            headers[key] = random.choice(values)
        return headers


class PostHeadersGenerator:
    def __init__(self):
        self.headers = {
            "User-Agent": [
                "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36",
                "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36",
            ],
            'authority': ["www.walmart.ca"],
            "accept": ["application/json"],
            "Accept-Encoding": ["gzip, deflate"],
            "Connection": ["keep-alive"],
            "Cache-Control": ["max-age=0"],
            "DNT": ["1"],
            "Upgrade-Insecure-Requests": ["1"],
        }

    def generate_headers(self):
        headers = {}
        for key, values in self.headers.items():
            headers[key] = random.choice(values)
        return headers