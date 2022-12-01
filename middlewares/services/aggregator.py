from django.db.models import Sum, Count, QuerySet

from middlewares.services.types import CONTEXT_DATA


def aggregator(queryset: QuerySet) -> CONTEXT_DATA:
    total_visits = queryset.aggregate(Sum('count_of_visits')).get('count_of_visits__sum')
    total_pages = queryset.aggregate(Count('path')).get('path__count')
    return {
        "total_visits": total_visits,
        "count_of_visited_pages": total_pages,
    }
