from django.shortcuts import render
import requests
from django.http import JsonResponse

# Create your views here.

def movie_list(request):
    key = '93ca9100'
    url = f"http://www.omdbapi.com/?apikey={key}&s=lion king"
    response = requests.get(url).json()

    context ={
        'movies':response
    }
    #return JsonResponse(response)

    return render(request, 'list.html', context)

def movie_detail(request, movie_id):
    key = '93ca9100'
    url = f"http://www.omdbapi.com/?apikey={key}&i={movie_id}"
    response = requests.get(url).json()

    context ={
        'movie': response
    }

    #return JsonResponse(response)

    return render(request, 'detail.html', context)



