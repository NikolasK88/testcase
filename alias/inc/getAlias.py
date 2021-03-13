from alias.models import Alias
from datetime import datetime


def get_alias(request):
    target = request.GET.get('target', False)
    date_from = request.GET.get('date_from', False)
    date_to = request.GET.get('date_to', False)

    alias_obj = Alias.objects.all()

    if target:
        alias_obj = alias_obj.filter(target=target)
    if date_from:
        date_from = datetime.strptime(date_from, '%Y-%m-%d %H:%M:%S.%f')
        alias_obj = alias_obj.filter(start__gte=date_from)
    if date_to:
        date_to = datetime.strptime(date_to, '%Y-%m-%d %H:%M:%S.%f')
        alias_obj = alias_obj.filter(end__lt=date_to)

    return alias_obj
