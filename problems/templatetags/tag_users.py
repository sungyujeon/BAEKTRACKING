from django import template

register = template.Library()

@register.filter
def tag(username):
    username = f'<a href="">{username}</a>'
    
    return username