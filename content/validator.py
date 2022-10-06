from logging.config import valid_ident
from xmlrpc.client import boolean


class ContentValidator:
    valid_keys = [
        "title",
        "module",
        "description",
        "students",
        "is_active",
    ]
    valid_inputs = {
        "title": str,
        "module": str,
        "description": str,
        "students": int,
        "is_active": bool,

    }

    def __init__(self, *args: tuple, **kwargs: dict):
        self.data = kwargs
        self.errors = {}

    def is_valid(self) -> bool:
        self.clean_data()
        try:
            self.validated_required_keys()
            self.validated_data_types()
            return True

        except KeyError:
            return False

    def clean_data(self):
        data_keys = list(self.data.keys())
        for key in data_keys:
            if key not in self.valid_keys:
                self.data.pop(key)

    def validated_required_keys(self):
        for valid_key in self.valid_keys:
            if valid_key not in self.data.keys():
                self.errors.update({valid_key: "missing key"})
        if self.errors:
            raise KeyError

    def validated_data_types(self):
        for valid_key, expected_type in self.valid_inputs.items():
            if type(self.data[valid_key]) is not expected_type:
                err_msg = f"expected '{valid_key}' to be an '{expected_type.__name__}'"
                self.errors.update({valid_key: err_msg})
        if self.errors:
            raise KeyError
