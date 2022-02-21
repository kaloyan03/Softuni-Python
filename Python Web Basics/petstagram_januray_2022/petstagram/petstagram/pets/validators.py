from django.core.exceptions import ValidationError


class MaxSizeFileInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        if value.file.size > self.convert_mb_to_bytes(self.max_size):
            raise ValidationError(f'Max size should be no more than {self.max_size} MB.')

    def convert_mb_to_bytes(self, value):
        return value * 1024 * 1024

