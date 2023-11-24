from django.shortcuts import render
from .models import Personagem, Review, List
from django.views import generic
from django.shortcuts import get_object_or_404

def index(request):
    context = {}
    return render(request, 'staticpages/index.html', context)

def about(request):
    context = {}
    return render(request, 'staticpages/about.html', context)

def list_personagem(request):
    personagem_list = Personagem.objects.all()
    context = {'personagem_list': personagem_list}
    return render(request, 'lista/list.html', context)



def list_review(request, post_id):
    personagem = get_object_or_404(Personagem, pk=post_id)
    reviews = Review.objects.filter(personagem=personagem)
    return render(request, 'lista/revi.html', {'personagem': personagem, 'reviews': reviews})


class PersonagemListView(generic.ListView):
    model = Personagem
    template_name = 'lista/list.html'

class ListListView(generic.ListView):
    model = List
    template_name = 'lista/revi.html'


