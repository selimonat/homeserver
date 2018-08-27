from django import template

register = template.Library()




@register.filter
def value_at_max(d):
	"""
		Returns the value of a dict at key with maximum value,
	"""	
	return d.get(max(d.keys()))
