from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from Sentimov.sentiment import searchApi, sentimenttweets

def index(request):
    return render(request, 'index.html')

def search(request):
    try:
        movie_name = request.GET['moviename']
        if (movie_name == ""):
            return HttpResponse("<h1>ERROR</test>")
        return render(request, 'search.html')
    except:
        return HttpResponse("<h1>ERROR</test>")

def tweet(request):
    try:
        movie_name = request.GET['moviename']
        if (movie_name == ""):
            return HttpResponse("<h1>ERROR</test>")
        return render(request, 'tweet.html')
    except:
        return HttpResponse("<h1>ERROR</test>")

def result(request):
    return render(request, 'result.html')

def api_tweet(request):
    movie_name = request.GET['moviename']
    max_id = int(request.GET['maxid'])
    x = searchApi.get_tweets(movie_name, max_id)
    return JsonResponse(x)

def delete_tweet(request):
    try:
        movie_name = request.GET['moviename']
        if (movie_name == ""):
            return HttpResponse("<h1>ERROR</test>")
        searchApi.delete_file(movie_name)
        return JsonResponse({'done':'done'})
    except:
        return HttpResponse("<h1>ERROR</test>")

def sentiment(request):
    try:
        movie_name = request.GET['moviename']
        if (movie_name == ""):
            return HttpResponse("<h1>ERROR</test>")
        x = sentimenttweets.sentiment(movie_name)
        return JsonResponse(x)
    except:
        return HttpResponse("<h1>ERROR</test>")

def download(request):
    try:
        movie_name = request.GET['moviename']
        if (movie_name == ""):
            return HttpResponse("<h1>ERROR</test>")
        movie_name = movie_name.replace(" ", "").replace(":", "").replace("'","").replace("-","")
        file_full_path = "./Sentimov/sentiment/" + movie_name + '.tsv'
        with open(file_full_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + movie_name + '.tsv'
            return response
    except:
        return HttpResponse("<h1>ERROR</test>")