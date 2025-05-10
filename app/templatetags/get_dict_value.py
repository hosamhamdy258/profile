from django import template

register = template.Library()


@register.filter("get_dict_value")
def get_dict_value(dict_data: dict, key: str = None):
    """Lookup a value in a dictionary or return the first value if no key is provided."""
    if key:
        return dict_data.get(key)
    elif dict_data:
        return list(dict_data.values())[0]
    return None
