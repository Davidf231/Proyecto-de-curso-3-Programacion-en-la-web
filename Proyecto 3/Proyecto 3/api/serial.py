from rest_framework import serializers

from .models import Shinigami

class ShinigamiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shinigami
        fields = ['id','nombre','edad','bankai','escuadron','cargo']
