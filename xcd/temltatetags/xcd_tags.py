# from django import template
# from xcd.models import *
# from django.db.models import Count, F
#
# register = template.Library()
#
#
# @register.simple_tag()
# def get_styles():
#     return Style.objects.all()
#
#
# @register.inclusion_tag('home.html')
# def show_style(arg1='Helo', arg2='OLeg'):
#     # style = Style.objects.annotate(cnt=Count('style')).filter(cnt__gt=0)
#     style = Style.objects.annotate(cnt=Count('style', filter=F('published'))).filter(cnt__gt=0)
#     return ('style':style, 'arg1':arg1, 'arg2':arg2)
