from rest_framework.response import Response
from alias.models import Alias


def check_alias(alias, target, date_from, date_to):
    print('ok')
    try:
        print('ok1')
        alias_obj = Alias.objects.filter(target=target, alias=alias)
        print('ok2')
        return {'success': 0,
                'message': 'You already have such object'}
    except:
        pass

    try:
        alias_obj = Alias.objects.filter(target=target, alias=alias, date_from__lte=date_to)
        if date_to:
            try:
                if Alias.objects.filter(target=target, alias=alias, date_to__gte=date_from):
                    return {'success': 0,
                            'message': 'Time was already taken, choose another time'}
            except:
                pass

        return {'success': 0,
                'message': 'Time was already taken, choose another time'}
    except:
        pass

    return True
