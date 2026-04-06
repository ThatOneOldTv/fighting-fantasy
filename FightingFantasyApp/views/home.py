from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse

# Create your views here.
def main_menu(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')

#---------- NEW ADVENTURE ----------
def new_adventure(request: HttpRequest) -> HttpRequest:
    """Render the new adventure page"""
    return render(request, 'new_adventure.html')

def get_adventures(request: HttpRequest) -> JsonResponse:
    """Grab all adventures in the adventure section
    
    Returns:
        JsonResponse: Contains the name and description of each adventure in the adventures folder"""
    return JsonResponse({'status': 'success'})
