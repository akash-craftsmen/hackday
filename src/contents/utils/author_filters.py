from ..models import Author

import django_filters


class AuthorFilter(django_filters.FilterSet):

    class Meta:
        model = Author
        fields = {
            'name': ["exact"],
            'author_id':['exact'],
            'timeframe':['exact']
        }
