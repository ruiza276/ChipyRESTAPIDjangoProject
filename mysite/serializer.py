from django.contrib.auth.models import User, Group
from rest_framework import serializers
from mysite.models import Bands, MetalBands


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bands
        fields = ['id','band_name','fans','formed','origin','split','style']

class MetalBandSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetalBands
        fields = ['id','band_name','fans','formed','origin','split','style']

# ##    band_name = models.CharField(max_length = 120)
#     fans = models.CharField(max_length = 10)
#     formed = models.CharField(max_length = 4)
#     origin = models.CharField(max_length = 50)
#     split = models.CharField(max_length = 4)
#     style = models.CharField(max_length = 35)