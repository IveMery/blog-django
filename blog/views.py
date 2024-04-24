from django.shortcuts import render
from .models import *
from django.http import Http404
from django.shortcuts import render , get_object_or_404

#def indexView(request):
    #template_name = 'index.html'
    #return render(request, template_name)

def boardsView(request):
    boards = Board.objects.all()
    #boards_names = list()
    return render(request,'home.html', {'boards': boards})

def board_topicsView(request,pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})