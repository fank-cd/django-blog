from django import template


register = template.Library()

@register.simple_tag()
def test():
    return "this is test code"