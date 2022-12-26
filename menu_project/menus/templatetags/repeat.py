from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def repeat(value: str, arg: any) -> str:
    '''Repeats string "arg" times'''
    return value * int(arg)
