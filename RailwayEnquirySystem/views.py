from django.http import HttpResponse
from django.shortcuts import render
import requests

def homepage(request):
    data = {
        'title': 'Railway Enquiry System'
    }
    return render(request, "index.html", data)

def testpage(request):
    return HttpResponse("Test")

def contact(request):
    return HttpResponse("Contact Page")

def search(request):
    data = {
        'title': 'Search Train By Name or Number'
    }
    return render(request, "search.html", data)

def s_result(request):
    try:

        if request.method == "GET":

            train = request.GET['train']

            url = "https://trains.p.rapidapi.com/"

            payload = {"search": train}
            headers = {
                "content-type": "application/json",
                "X-RapidAPI-Key": "<Key>",
                "X-RapidAPI-Host": "trains.p.rapidapi.com"
            }

            response = requests.request("POST", url, json=payload, headers=headers)

            res = response.json()

            data = {
                'title': "Search Trains",
                'train': train,
                'response': res
            }
    except:
        pass

    return render(request, "search-result.html", data)

def pnr(request):
    data = {
        'title': 'Search Passenger Name Record'
    }
    return render(request, "pnr.html", data)

def pnr_search(request):
    try:

        if request.method=="POST":

            pnr = request.POST['pnr']

            url = f"https://pnr-status-indian-railway.p.rapidapi.com/pnr-check/{pnr}"

            headers = {
                "X-RapidAPI-Key": "<Key>",
                "X-RapidAPI-Host": "pnr-status-indian-railway.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers)

            res = response.json()

            data = {
                'title': "Search By PNR - Railway Enquiry System",
                'pnr': pnr,
                'response': res
            }
    except:
        pass

    return render(request, "pnr-result.html", data)

def station(request):
    data = {
        'title': 'Search Station'
    }
    return render(request, "station.html", data)

def station_result(request):

    try:

        url = "https://indianrailways.p.rapidapi.com/findstations.php"

        station = request.GET['station']

        querystring = {"station": station}

        headers = {
            "X-RapidAPI-Key": "<Key>",
            "X-RapidAPI-Host": "indianrailways.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        res = response.json()

        data = {
                'title': "Search Stations - Railway Enquiry System",
                'station': station,
                'response': res
        }

    except:

        pass

    return render(request, "station-results.html", data)

def about(request):
    data = {
        'title': 'About'
    }
    return render(request, "about.html", data)