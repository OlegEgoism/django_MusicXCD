from django import template
from xcd.models import *

register = template.Library()

@register.simple_tag()
def get_styles():
    return Style.objects.all()

