import http.client
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random

# Function to fetch proxies
def fetch_proxies():
    """Fetch a list of proxies from ProxyScrape API."""
    conn = http.client.HTTPSConnection("api.proxyscrape.com")
    payload = ''
    headers = {}
    conn.request("GET", "/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8").splitlines()

# Function to choose a random proxy from the list
def get_random_proxy():
    proxies = fetch_proxies()
    if not proxies:
        raise Exception("No proxies available. Ensure the API is working and the list is populated.")
    return random.choice(proxies)

def open_chrome_with_proxy(proxy_address):
    """Open Chrome with a specified proxy."""
    print(f"Using Proxy IP: {proxy_address}")
    
    # Chrome options
    options = Options()
    options.headless = False  # Set to True if you want to run in headless mode
    
    # Manually set proxy for Chrome
    options.add_argument(f'--proxy-server={proxy_address}')

    # Open Chrome with the proxy settings
    try:
        driver = webdriver.Chrome(options=options)
        driver.get("http://checkip.amazonaws.com")  # Check your current IP address
        print("IP Address:", driver.page_source.strip())  # Print IP from the page source
        input("Press Enter to close the browser...")
    except Exception as e:
        print(f"Error opening browser: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    proxy_address = get_random_proxy()
    open_chrome_with_proxy(proxy_address)
