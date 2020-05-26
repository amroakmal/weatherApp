from django.shortcuts import render

# Create your views here.
def home(request):
    import json, requests
    zip_code = "20002"
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip_code + "&distance=25&API_KEY=A3ADA6EC-7329-49CF-B291-19D16733441A")
    
    try:
        api = json.loads(api_request.content)
        categoryColor = ""
        category = api[0]['Category']['Name']
        if(category == "Good"):
            categoryColor = "good"
        elif category == "Moderate":
            categoryColor = "moderate"
        elif category == "Unhealty for Sensitive Groups":
            categoryColor = "usg"
        elif category == "Unhealthy":
            categoryColor = "unhealthy"
        elif category == "Very Unhealthy":
            categoryColor = "veryUnhealthy"
        else:
            categoryColor = "hazardous"
    except Exception as e:
        api = 'Error..'
    return render(request, 'home.html', {'api': api, 'categoryColor': categoryColor})

def about(request):
    return render(request, 'about.html')