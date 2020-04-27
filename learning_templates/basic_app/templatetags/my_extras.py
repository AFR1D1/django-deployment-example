from django import template
register = template.Library()

@register.filter #@register.filter(name= 'cut')   #same...
def cutout(value, arg):

    #this cuts out the arg from the string

    return value.replace(arg, '')
