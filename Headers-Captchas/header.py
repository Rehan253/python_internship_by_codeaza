import requests

url = "https://www.daraz.pk/?spm=a2a0e.searchlistcategory.header.dhome.488c449amMy0MZ"
response = requests.get(url)

# Accessing request and response headers
request_headers = response.request.headers
response_headers = response.headers

print("Request Headers:")
print(request_headers)
print("\nResponse Headers:")
print(response_headers)
