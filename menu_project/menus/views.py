from django.shortcuts import get_object_or_404, render

from .models import Node


def menu(request, node_id):
    '''View rendering menu with chosen node'''
    current_node = get_object_or_404(Node, id=node_id)
    root = current_node.get_root(current_node)
    return render(request, 'menus/menus.html', {
        'current_node_id': node_id,
        'menu_name': root,
    })


def index(request):
    '''View rendering main page with all available menus'''
    return render(request, 'menus/index.html', {
        'roots': Node.objects.filter(parent=None),
    })
