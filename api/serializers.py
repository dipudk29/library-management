from rest_framework import serializers
from app.models import Books, Members

class BookSerialzier(serializers.ModelSerializer):


    class Meta:
        model = Books
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = '__all__'