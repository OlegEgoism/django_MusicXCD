from django import template
from xcd.models import Samples

register = template.Library()

@register.simple_tag()
def get_samples():
    return Samples.objects.all()

