from rest_framework.pagination import LimitOffsetPagination

class DefaultPagination(LimitOffsetPagination):
    """
    Default settings for the pagination
    """
    default_limit = 10
    max_limit = 100
