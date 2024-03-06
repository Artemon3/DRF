import re

from rest_framework.serializers import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        # reg = re.compile('https://www.youtube.com')
        tmp_val = value.get(self.field)
        if tmp_val and not tmp_val.startswith('https://www.youtube.com'):
            raise ValidationError('Url is not ok')
