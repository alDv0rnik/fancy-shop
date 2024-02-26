from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

cats = {
    "food": "food",
    "animal-goods": "animal goods"
}


def index(request):
    # breakpoint()
    # print(request)
    return HttpResponse("<h2>Main page</h3>")


def categories(request):
    return HttpResponse("<h3>Catalog</h3>")


def category(request, cat):
    if int(cat) > 2:
        return redirect('categories', permanent=True)
    # if request.GET:
    #     print(request.GET.get("type"))
    return HttpResponse(f"<h3>Items from category {cat}</h3>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h3>Page not found</h3>")
