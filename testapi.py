import requests

url = " http://192.168.21.189:5000/colorize"
files = {"file": open("test_images/image.png", "rb")}
response = requests.post(url, files=files)

print(response.json())