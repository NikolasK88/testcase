from alias.models import Alias
from datetime import datetime, timedelta


def alias_replace(existing_alias, replace_at, new_alias_value):
    replace_at = datetime.strptime(replace_at, '%Y-%m-%dT%H:%M:%S')
    alias_obj = Alias.objects.get(id=int(existing_alias))
    alias_obj.end = replace_at - timedelta(microseconds=1)
    alias_obj.save()
    new_alias_obj = Alias.objects.create(alias=new_alias_value,
                                         target=alias_obj.target,
                                         start=replace_at,
                                         end=None)
    return{'success': 1,
           'message': 'New object created',
           'object alias': new_alias_obj.alias}
