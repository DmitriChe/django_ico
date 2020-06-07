from django import template
register = template.Library()


def alfajumper(text):
    return ''.join([text[i].upper() if i % 2 == 0 else text[i] for i in range(len(text))])


def capitalize(text):
    return text.capitalize()


# регистрация фильтра
register.filter('alfajumper', alfajumper)
register.filter('capitalize', capitalize)