from django import Template

register = template.library()

@register.filter(name='cut')
def cut(value, arg):
	"""
	This cuts all values of "arg" from the string!
	"""

	return value.replace(arg,'')

# register.filter('cut', cut)
