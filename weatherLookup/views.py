from django.shortcuts import render

# Create your views here.
def home(request):
    import json, requests
    zip_code = "20002"
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip_code + "&distance=25&API_KEY=A3ADA6EC-7329-49CF-B291-19D16733441A")
    
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = 'Error..'
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html')