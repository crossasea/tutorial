from rest_framework import serializers
from snippets.models import Snippet

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['userid', 'firstname', 'lastname', 'companyname', 'age', 'city', 'state', 'zip', 'email', 'web']

"""
class SnippetSerializer(serializers.Serializer):
    userid = serializers.IntegerField(read_only=True)
    firstname = serializers.CharField(required=False, allow_blank=True, max_length=100)
    lastname = serializers.CharField(required=False, allow_blank=True, max_length=100)
    companyname = serializers.CharField(required=False, allow_blank=True, max_length=100)
    age = serializers.IntegerField(max_value=None, min_value=None)
    city = serializers.CharField(required=False, allow_blank=True, max_length=100)
    state = serializers.CharField(required=False, allow_blank=True, max_length=100)
    zip = serializers.IntegerField(max_value=None, min_value=None)
    email = serializers.CharField(required=False, allow_blank=True, max_length=100)
    web = serializers.CharField(required=False, allow_blank=True, max_length=100)

   def create(self, validated_data):
        
       # Create and return a new `Snippet` instance, given the validated data.
        
        return Snippet.objects.create(**validated_data)

   def update(self, instance, validated_data):
        
       # Update and return an existing `Snippet` instance, given the validated data.
        
        instance.firstname = validated_data.get('first name', instance.firstname)
        instance.lastname = validated_data.get('last name', instance.lastname)
        instance.companyname = validated_data.get('company name', instance.companyname)
        instance.age = validated_data.get('age', instance.age)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.zip = validated_data.get('zip', instance.zip)
        instance.email = validated_data.get('email', instance.email)
        instance.web = validated_data.get('web', instance.web)
        instance.save()
        return instance
"""
