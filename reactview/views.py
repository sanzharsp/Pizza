
from django.http import JsonResponse
from django.shortcuts import render
from .models import Pizza
from .serializers import *
from django.views import View

def index(request):
    return render(request,'index.html')


#Загрузка данных
class load(View):
    def get(self,request):
        blist = Pizza.objects.all()
        data = [{
         "id":x.id,
         "imageUrl":"{}".format(x.imageUrl.url),
          "name":x.name, 
          "types":[s.id-1 for s in x.types.all()] ,
          "sizes":[s.size for s in x.sizes.all()],
          "price":x.price,
          "category":x.category,
          "rating":x.rating} 
          for x in blist] 
        return JsonResponse(data,safe=False)

#Фильртация
class Filters(View):
    def get(self,request):
        print("Hello")
        return "Succesful GET request"
        


class Manifest(View):
    def get(self,request):
        return render(request,'manifest.json')


