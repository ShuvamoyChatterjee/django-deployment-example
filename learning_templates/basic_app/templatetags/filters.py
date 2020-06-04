from django import template

register = template.Library()

@register.filter(name='func')
def func(value,s):
    return value+s