import json
from django.http import JsonResponse

def api_home(request,*arge,**kwargs):
    body  = request.body
    data = {}
    print("Get:",request.GET)
    print("Post:",request.POST)
    try:
        data = json.loads(body)   # converting the request body [string json data] --> json type
    except:
        pass 
      
    data["params"] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    print("data:",data)

    return JsonResponse({'message': 'Welcome to the API',
                          'data': data})
  