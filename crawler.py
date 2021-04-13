import requests
import ssl
from bs4 import BeautifulSoup

response = requests.get(
    "https://www.ibm.com/support/pages/apar/OA59321", verify=False)
# try:

# except:
#     print(requests.exceptions)


# response = requests.get(
#     "https://www.ibm.com/support/pages/apar/OA59321", verify=False)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())  # 輸出排版後的HTML內容
