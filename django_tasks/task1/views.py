from django.shortcuts import render
from .models import Card

# Create your views here.
def view_card(request):
    cards = Card.objects.all()
    return render(request, 'task1/view_card.html', {'cards': cards})