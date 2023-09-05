
from rest_framework import serializers 


#CustomUser Serializer 
class StudentSerializers(serializers.Serializer): 
    id = serializers.IntegerField() 
    email = serializers.EmailField()
    username = serializers.CharField()
    skills = serializers.CharField()
    github_url = serializers.URLField()
    linkedin_url = serializers.URLField()
    submissions = serializers.IntegerField()
    is_active = serializers.BooleanField()
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField() 

#CodingProblemSerializer
class CodingProblemSerializers(serializers.Serializer):
    pass 


#InputParamterSerializsers
class InputParameterSerializer(serializers.Serializer):
    pass 


#OutputParameterSerializsers
class OutputParameterSerializers(serializers.Serializer):
    pass 