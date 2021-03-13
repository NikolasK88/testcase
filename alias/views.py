from django.shortcuts import render
from rest_framework import viewsets, permissions
from datetime import datetime
from rest_framework.response import Response
from alias.models import Alias
from alias.serializers import AliasSerializer
from alias.inc.replaceAlias import alias_replace
from alias.inc.checkAlias import check_alias
from alias.inc.getAlias import get_alias


class AliasView(viewsets.ModelViewSet):
    serializer_class = AliasSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Alias.objects.all()

    def list(self, request):
        return Response(get_alias(request).values())

    def create(self, request):
        alias = request.POST.get('alias', False)
        target = request.POST.get('target', False)
        date_from = request.POST.get('date_from', False)
        date_to = request.POST.get('date_to', False)

        replace = request.POST.get('replace', False)
        # if replace = 'true' we use def alias_replace()
        existing_alias_id = request.POST.get('existing_alias_id', False)
        replace_at = request.POST.get('replace_at', False)
        new_alias_value = request.POST.get('new_alias_value', False)

        check = check_alias(alias, target, date_from, date_to)
        if check is True:
            alias_obj = Alias.objects.create(alias=alias,
                                             target=target,
                                             start=date_from)
            if date_to:
                alias_obj.end = date_to
                alias_obj.save()

        else:
            return Response(check)

        if replace == 'true':
            return Response(alias_replace(existing_alias_id,
                                          replace_at,
                                          new_alias_value))

        return Response({'success': 1,
                         'object alias': alias_obj.alias})
