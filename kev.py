import requests

kev_url = 'https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json'
output_file = 'known_exploited_vulnerabilities.json'

response = requests.get(kev_url)

if response.status_code == 200:
    with open(output_file, 'wb') as f:
        f.write(response.content)
    print(f"File downloaded successfully and saved as {output_file}")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
