# Chrome Proxy Browser

This Python script fetches proxies from the ProxyScrape API and uses a randomly selected proxy to open Google Chrome for anonymous browsing. The current IP address is displayed to verify the proxy is active.

## Features

- Fetches proxies using the ProxyScrape API.
- Uses a randomly selected proxy for Chrome browsing.
- Displays the current IP address to verify the proxy is working.

## Getting Started

### Prerequisites

- Python 3.x
- Selenium WebDriver
- ProxyScrape API key (if required by API)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Sheekovic/chrome-new-ip.git
   cd chrome-new-ip

2. Install the required Python libraries:
   ```bash
   pip install selenium

3. Add your ProxyScrape API key or ensure the API is accessible.

### Usage

1. Run the script:
   ```bash
   python proxy.py
   ```

2. The script will fetch proxies, select a random one, and open Chrome with the selected proxy.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- ProxyScrape API
- Selenium WebDriver
