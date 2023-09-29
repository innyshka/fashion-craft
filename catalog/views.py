from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseRedirect

from .models import Clothing, Designer, Size, Materials, ClothingType


@login_required
def index(request: HttpRequest) -> HttpResponse:
    num_clothes = Clothing.objects.all().count()
    num_designers = Designer.objects.all().count()
    num_clothing_types = ClothingType.objects.all().count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    contex = {
        "num_clothes": num_clothes,
        "num_designers": num_designers,
        "num_clothing_types": num_clothing_types,
        "num_visits": num_visits + 1,
    }
    return render(request, "catalog/index.html", context=contex)


