from django.shortcuts import render

# Create your views here.
def home(request):
    import json
    import requests
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=F6F49C45-2671-4B1B-B479-6A2F06741B25")
    #https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=F6F49C45-2671-4B1B-B479-6A2F06741B25
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error ..."

    return render( request, 'home.html' , {'api':api} )

def about(request):
    return render(request,'about.html',{})
