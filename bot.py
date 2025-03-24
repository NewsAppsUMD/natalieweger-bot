import requests

# List of Department of Education pages to track
urls = [
    "https://www.ed.gov/higher-education/find-college-or-educational-program",
    "https://www.ed.gov/higher-education/paying-college",
    "https://www.ed.gov/higher-education/manage-your-loans",  
]

def check_url_status(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code in [404, 403, 503]:
            print(f"⚠️ {url} is down! Status code: {response.status_code}")
        else:
            print(f"✅ {url} is up. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"❌ Error checking {url}: {e}")

# Run the check for all URLs
for url in urls:
    check_url_status(url)

