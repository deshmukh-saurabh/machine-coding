import abc
from services.string_filter_service import StringFilterService
from services.field_filter_service import FieldFilterService


class Filter(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def apply_filter(self, filter):
        pass


class FieldFilter(Filter):
    def __init__(self):
        self.filter_service = FieldFilterService()

    def apply_filter(self, filter):
        return self.filter_service.filter_contacts(filter)


class StringFilter(Filter):
    def __init__(self):
        self.filter_service = StringFilterService()

    def apply_filter(self, filter):
        return self.filter_service.filter_contacts(filter)


class FilterFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def get_filter(filter_type):
        if filter_type == "string_filter":
            return StringFilter()
        if filter_type == "field_filter":
            return FieldFilter()
        else:
            raise Exception("Invalid filter_type!")
