from django.shortcuts import render
from django.http import HttpResponse
from .models import Listing

def index(request):
    
    
    """
    context = {
        "home_1": "16th South Ave.",
        "home_1_description": "Perched against stunning mountain vistas, \
            this meticulously designed mountainside home boasts panoramic views, \
            luxurious interiors, and seamless integration with nature. With high-end finishes,\
            multiple outdoor spaces, and easy access to outdoor activities, this residence \
            offers a unique blend of elegance and mountain living. ",
            
        "home_2": "28 Walnut Dr.",
        "home_2_description": "Discover modern urban living in this chic condo \
            featuring a compact yet stylish design. Enjoy a wealth of amenities, \
            including a fitness center, rooftop lounge, and concierge service. Ideal \
            for those seeking convenience and comfort in the heart of the city."


    }
    """


    listings = Listing.objects.all()
    context = {"listings": listings}



    return render(request, "index.html", context)
