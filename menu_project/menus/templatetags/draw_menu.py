from django import template
from django.shortcuts import get_object_or_404

from ..models import Node

register = template.Library()


@register.inclusion_tag("menu.html", takes_context=True)
def draw_menu(context, name: str) -> dict:
    '''Draws menu by its name.'''
    # чтобы понять отображать меню с активным пунктом или без проверяем
    # наличие id активного пункта в запросе
    if 'current_node_id' in context:
        current_node_id = context['current_node_id']
        current_node = get_object_or_404(Node, id=current_node_id)
        # собираем список всех пунктов меню, начиная со всех пунктов над 
        # активным
        nodes = current_node.get_ancestors(current_node)
        # добавляем активный пункт
        nodes.append(current_node)
        # наконец добавляем первый уровень вложенности
        nodes.extend(current_node.children.all())
        return {'nodes': nodes, 'current_node_id': current_node_id}
    # если id в запросе не было, отображаем первый (корневой) пункт меню
    root = [get_object_or_404(Node, text=name)]
    return {'nodes': root}
