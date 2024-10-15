import requests

# Google Sheets API URL 및 API 키
url = "https://sheets.googleapis.com/v4/spreadsheets/1Sru_57UKdy8QfjD8brkR3rs8CCPC64SIwr2_g61CWCw/values/sns%EC%A0%95%EB%B3%B4/"
params = {
    'key': 'AIzaSyCh7rOV5pXSosUvdwENtockIf0H9XAGCyY'
}

# 헤더 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.1 Safari/605.1.15",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Origin": "http://43.200.44.34",
    "Referer": "http://43.200.44.34/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site"
}

# 데이터 요청
response = requests.get(url, headers=headers, params=params)

# 응답 데이터 확인
if response.status_code == 200:
    data = response.json()
    print(data)  # 데이터를 JSON 형식으로 출력
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
