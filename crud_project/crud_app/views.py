from ast import Delete
from .models import *     #improrting all tables from models.py to use in view.py
from rest_framework import status #to show the status in response
from rest_framework.views import APIView  #type of  function argument predefined
from rest_framework.response import Response #to get response
from datetime import date
import datetime as dt
# Create your views here.
#here we are going to use class based function


class AddProductView(APIView):
    def post(self,request):
        try:
            product=request.data.get('product_name')
            price=request.data.get('product_price')
            now = dt.datetime.now().strftime("%Y-%m-%d")

            productInfo=crud_models(product_name=product,product_price=price,product_created_date=now)
            productInfo.save()

            return Response({'status':'ok','message':'product created Succesfully'})
        except Exception as e:
            print(e)
            return Response({'status':'not ok','message':'product could not created '})

class GetAllProductView(APIView):
    def get(self,request):
        try:
            products=crud_models.objects.all()
            productsDict={}
            productList=[]
            for fruit in products:
                productsDict['id']=fruit.id
                productsDict['name']=fruit.product_name
                productsDict['price']=fruit.product_price
                productsDict['date']=fruit.product_created_date

                productList.append(productsDict.copy())

            return Response({'status':'ok','message':'product fetched succesfully','data':productList})

        except Exception as e:
            return Response({'status':'not ok','message':'product could not fetched '})

class GetProductByIdView(APIView):
    def post(self,request):
        try:
            id=request.data.get('id')
            productInfo=crud_models.objects.get(id=id)
            productDict={}
            productDict['id']=productInfo.id
            productDict['product_name']=productInfo.product_name
            productDict['product_price']=productInfo.product_price
            productDict['date']=productInfo.product_created_date

            return Response({'ststus':'ok','message':'success','data':productDict})

        except Exception as e:
            print(e)
            return Response({'ststus':'not ok','message':'unsuccess'})

class UpdateproductView(APIView):
    def put(self,request):
        try:
            id=request.data.get('id')
            product=request.data.get('product_name')
            price=request.data.get('product_price')

            productInfo=crud_models.objects.get(id=id)
            productInfo.product_name=product
            productInfo.product_price=price

            productInfo.save()
            return Response({'status':'ok','message':'product updated Succesfully'})
        except:
            return Response({'status':'not ok','message':' unSucces'})

class DeleteProductView(APIView):
    def delete(self,request):
        try:
            id = request.data.get('id')
            productInfo=crud_models.objects.get(id=id)
            productInfo.delete()

            return Response({'status':'ok','message':'product deleted Succesfully'})
        except:
            return Response({'status':'not ok','message':'unSuccess'})
