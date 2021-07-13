from django import template
import json

register = template.Library()


@register.simple_tag
def entry_saved_data(value):
    return json.loads(value)
