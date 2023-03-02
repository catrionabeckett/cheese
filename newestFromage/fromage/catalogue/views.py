from django.shortcuts import render, get_object_or_404, redirect
from .models import Cheese, Review, Customer

# Create your views here.
def home(request):

    # if "query" in query_params:
    #     cheese_name_query = query_params["query"]
    #     cheese_strength_query = query_params["strength"]
    #     cheese_query = Cheese.objects.filter(name__icontains=cheese_name_query, strength=int(cheese_strength_query))
    # else:
    #     cheese_query = Cheese.objects.all()


    # query_params -> {"query": "Brie", "strength": "4"}
    # items -> [("query", "Brie"), ("strength", "4")]
    # filters -> {"name__icontains": "Brie", "strength": "4"}

    query_params = request.GET

    filter_map = {
        "query": "name__icontains",
        "strength": "strength",
        "country": "country__iexact"
    }

    filters = {}
    for key, value in query_params.items():
        filter_key = filter_map[key]
        if value:
            filters[filter_key] = value

    cheeses = Cheese.objects.filter(**filters)

    countries = Cheese.objects.values_list("country", flat=True).distinct()
        
    context = {
        "cheeses": cheeses,
        "countries": countries
    }

    return render(request, "catalogue/home.html", context)










def cheese_details(request, id):
    context = {
        "cheese": get_object_or_404(Cheese, id=id)
    }
    return render(request, "catalogue/cheese_details.html", context)

def review(request, id):
    context = {
        "review": get_object_or_404(Review, id=id)
    }
    return render(request, "catalogue/review.html", context)

def customer(request, id):
    context = {
        "customer": get_object_or_404(Customer, id=id),
    }

    return render(request, "catalogue/customer.html", context)

def add_review(request, id):
    if request.method == "POST":
        customer = get_object_or_404(Customer, id=id)
        cheese = request.POST.get("cheese")
        cheese_obj = get_object_or_404(Cheese, id=int(cheese))
        rating = request.POST.get("rating")
        recommend = True

        review = Review(reviewer=customer, cheese=cheese_obj, rating=int(rating), recommend=recommend)
        review.save()
        return redirect(request.POST.get("redirect_url"))

def add_cheese(request):
    if request.method =="POST":
        name = request.POST.get("name")
        strength = request.POST.get("strength")
        colour = request.POST.get("colour")
        country = request.POST.get("country")
        age = request.POST.get("age")

        cheese = Cheese(name=name, strength=int(strength), colour=colour, age=int(age), country=country)
        cheese.save()
        return redirect(request.POST.get("redirect_url"))


