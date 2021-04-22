from django import template

register = template.Library()

@register.filter
def tag(username, problem_number):
    username = f'<a href="/problems/{username}/{problem_number}/">{username}</a>'
    return username