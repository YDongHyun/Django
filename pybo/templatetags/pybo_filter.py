from django import template

register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg    #-표현 장고에는 빼기연산이 없어서 직접 만듬