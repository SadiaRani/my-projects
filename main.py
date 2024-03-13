import requests
url = "https://courses.wscubetech.com/s/store/courses"
r = requests.get(url)
#print(r.status_code)
print(r.text)