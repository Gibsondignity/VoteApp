from unicodedata import category
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .models import MovieTitle, Contestants, Nominations, Category
from .serializers import MovieTitleSerializer, NominationSerializer, CategorySerializer
# Create your views here.

@api_view(['GET', "POST"])
def MovieTitleApi(request):
    if request.method == "GET":
        movie_title = MovieTitle.objects.all()
        print(movie_title)
        serializer = MovieTitleSerializer(movie_title, many=True)
        return Response(serializer.data)


        
@api_view(['GET', "POST","PUT"])
def NominationApi(request):
    if request.method == "GET":
        nominations = Nominations.objects.all()
        print(nominations)
        serializer = NominationSerializer(nominations, many=True)
        return Response(serializer.data)


    elif request.method == "POST":
        serializer = NominationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

    elif request.method == "PUT":
        nomination = Nominations.objects.get(id=request.data['id'])
        serializer = NominationSerializer(nomination, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        

 
@api_view(['GET', "POST","PUT"])
def CategoryApi(request):
    if request.method == "GET":
        category = Category.objects.all()
        print(category)
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


    
        

 

        


 