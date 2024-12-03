from rest_framework import serializers

from . models import *

class SBIcustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=customer_register_table
        fields=['full_name','email_id'] #database table columns only
        
        
class SBI_admin_Serializer(serializers.ModelSerializer):
    class Meta:
        model=admin_table
        fields='__all__' 
        


        