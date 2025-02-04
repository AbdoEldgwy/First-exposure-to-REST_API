import json
from django.http import JsonResponse

from products.models import Product

# def api_home(request,*arge,**kwargs):
#     body  = request.body
#     data = {}
#     print("Get:",request.GET)
#     print("Post:",request.POST)
#     try:
#         data = json.loads(body)   # converting the request body [string json data] --> json type
#     except:
#         pass 

#     data["params"] = dict(request.GET)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     print("data:",data)

#     return JsonResponse({'message': 'Welcome to the API',
#                           'data': data})

def api_home(request,*arge,**kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data["id"] = model_data.id
        data["title"] = model_data.title
        data["content"] = model_data.content
        data["price"] = model_data.price
    return JsonResponse({'message': data})