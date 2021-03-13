from rest_framework import serializers
from alias.models import Alias


class AliasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alias
        fields = "__all__"
