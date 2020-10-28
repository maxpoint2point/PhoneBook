from django import template
from ..forms import PhonesForm

register = template.Library()


@register.inclusion_tag("webui/tags/form.html")
def phone_form():
    return {"phone_form": PhonesForm()}
