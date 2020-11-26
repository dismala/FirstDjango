from django.shortcuts import render, HttpResponse, Http404
from .models import Item
from django.core.exceptions import ObjectDoesNotExist

user_data = {
    "surname": "Иванов",
    "name": "Алексей",
    "second_name": "Петрович",
}
items = [
   {"id": 1, "name": "Кроссовки abibas"},
   {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
   {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]

# Create your views here.
def main(request):
    user_format = f"{user_data['surname']} {user_data['name'][0]}.{user_data['second_name'][0]}."
    return render(request, 'index.html', context={"short_name": user_format})

def item(request, id):
    context = {}
    try:
        item = Item.objects.get(id=id)
    except 
        raise Http404
    context["item"] = item
        return HttpResponse(item["name"])
    raise Http404

def item_list(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items_list.html", context)