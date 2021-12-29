from django import template
from xcd.models import *

register = template.Library()

@register.simple_tag()
def get_style():
    return Style.objects.all()

    # style = Style.objects.all()
    # author = Author.objects.all()