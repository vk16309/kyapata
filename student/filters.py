import django_filters
from teacher.models import Teacher,Create


class ProductFilter(django_filters.FilterSet):

    name = django_filters.CharFilter(label="Name of Teacher",lookup_expr='icontains')

    class Meta:
        model = Teacher
        fields = ['city','class_type']
