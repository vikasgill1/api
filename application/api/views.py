
from rest_framework.generics import ListAPIView,ListCreateAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny , IsAuthenticated
from .serializer import*
from rest_framework.decorators import api_view

from ..custom import *
from rest_framework.status import *

class RegisterViewApi(ListAPIView):
    queryset=User.objects.all()
    permission_class=(AllowAny,)
    serializer_class=RegisterSerializer

class SignUpApi(APIView):
    permission_class=(AllowAny,)
    def post(self,request):
        serializer=SignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User create succesfully','data':[]},status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)



class LoginApiView(APIView):
    permission_class = (AllowAny,)

    def post(self,request):
        serializer=LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message':'login successfully','data':serializer.data},status=HTTP_200_OK)
        return Response(get_serializer_errors(serializer),status=HTTP_400_BAD_REQUEST)

class UpdateApi(APIView):
    permission_class=(AllowAny,)
    def post(self,request,pk):
        stu=User.objects.get(id=pk)
        serializer=SignSerializer(instance=stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'User create succesfully','data':[]},status=HTTP_201_CREATED)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)

class DeleteApi(APIView):
    permission_class=(AllowAny,)
    def delete(self,request,pk):
        stu=User.objects.get(id=pk)
        stu.delete()
        return Response({'message':'User delete succesfully'})
        





@api_view(['GET'])
def product_list(request):
    tasks=Product.objects.all().order_by('-id')
    serializer=ProductSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_search(request,pk):
    tasks=Product.objects.get(id=pk)
    serializer=ProductSerializer(tasks,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def product_create(request):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def product_update(request,pk):
    tasks=Product.objects.get(id=pk)
    serializer=ProductSerializer(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def product_delete(request,pk):
    tasks=Product.objects.get(id=pk)
    tasks.delete()
    return Response('item successfully delete')