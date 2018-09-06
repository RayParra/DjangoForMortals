from django.core.exceptions import ValidationError


def validate_content(content_value):
	content = content_value
	#c = content.split().upper()
	#for word in c:
	if "TWEET" in content.upper():
		raise ValidationError("Content Canot Publicated")
	if "XXX" in content.upper():
		raise ValidationError("Content Canot Publicated")
	return content_value