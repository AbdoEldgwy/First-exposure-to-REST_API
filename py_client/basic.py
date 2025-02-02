import requests

endpoits = "https://httpbin.org/anything"
endpoits = "http://127.0.0.1:8000/"
  
get_response = requests.get(endpoits, json={"query":"hello world"})
print(get_response.text) 


