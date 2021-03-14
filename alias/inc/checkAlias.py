from rest_framework.response import Response
from alias.models import Alias


def check_alias(alias, target, date_from, date_to):

    # checking are there any object which has the same target and  alias as a creating obj
    try:
        alias_obj = Alias.objects.filter(target=target, alias=alias)
        return {'success': 0,
                'message': 'You already have such object'}
    except:
        pass
    
    # checking are there any object which run in the same time as a creating obj
    try:
        alias_obj = Alias.objects.filter(target=target,
                                         alias=alias,
                                         date_from__lte=date_to)
        if date_to:
            try:
                alias_obj = Alias.objects.filter(target=target,
                                                 alias=alias,
                                                 date_to__gte=date_from)
                return {'success': 0,
                        'message': 'Time was already taken, choose another time'}
            except:
                pass

        return {'success': 0,
                'message': 'Time was already taken, choose another time'}
    except:
        pass

    return True
