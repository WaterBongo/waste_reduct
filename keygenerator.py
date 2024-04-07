import requests
import random
import string

cookies = {
    'csrftoken': 'r0h52UUSTuOeANEHSYrScxGeGr8uCNfq',
}

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'csrftoken=r0h52UUSTuOeANEHSYrScxGeGr8uCNfq',
    'dnt': '1',
    'origin': 'https://www.alphavantage.co',
    'referer': 'https://www.alphavantage.co/support/',
    'sec-ch-ua': '"Chromium";v="123", "Not:A-Brand";v="8"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'x-csrftoken': 'r0h52UUSTuOeANEHSYrScxGeGr8uCNfq',
    'x-requested-with': 'XMLHttpRequest',
}

data = {
    'first_text': 'deprecated',
    'last_text': 'deprecated',
    'occupation_text': 'Student',
    'organization_text': 'wqr',
    'email_text': 'wwg@gmail.com',
}
for i in range(10):
    def generate_random_email():
        email_length = 10
        email = ''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
        email += '@gmail.com'
        return email

    data['email_text'] = generate_random_email()
    response = requests.post('https://www.alphavantage.co/create_post/', cookies=cookies, headers=headers, data=data)
    print(response.json())