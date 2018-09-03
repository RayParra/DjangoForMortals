from django.core.exceptions import ValidationError


def validate_content(value):
	content = value
	if content == "porno":
		raise ValidationError("Content Canot Publicated")
	return value