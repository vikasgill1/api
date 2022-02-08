
from ..models import *
from rest_framework.serializers import *
from rest_framework_jwt.settings import api_settings
jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler  = api_settings.JWT_ENCODE_HANDLER



class RegisterSerializer(ModelSerializer):
    email=EmailField(error_messages={'required':'email key is required','blank':'email is required'})
    password=CharField(write_only=True,error_messages={'required':'password key is required','blank':'password is required'})
    username=CharField(write_only=True,error_messages={'required':'username key is required','blank':'username is required'})
    mobile_number=CharField(error_messages={'required':'mobile_number key is required','blank':'mobile_number is required'})
    gender=CharField(error_messages={'required':'gender key is required','blank':'gender is required'})
    profile_image=ImageField(error_messages={'required':'profile_image key is required','blank':'profile_image is required'})
    id_proof=FileField(error_messages={'required':'id_proof key is required','blank':'id_proof is required'})
    


    class Meta:
        model=User
        fields=('email','username','gender','first_name','profile_image','id_proof','mobile_number','password')


class SignSerializer(Serializer):
    email=CharField(error_messages={'required':'email key is required','blank':'email is required'})
    password=CharField(error_messages={'required':'password key is required','blank':'password is required'})
    username=CharField(error_messages={'required':'username key is required','blank':'username is required'})
    mobile_number=CharField(error_messages={'required':'mobile_number key is required','blank':'mobile_number is required'})
    gender=CharField(error_messages={'required':'gender key is required ','blank':'gender is required'})
    profile_image=ImageField(error_messages={'required':'profile_image is required','blank':'profile_image field is required'})
    Id_proof=FileField(error_messages={'required':'id_proof key is required','blank':'id_proof field is required'})
    
    def validate(self,data):
        username=data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError("Username already exists")
        return data

    def create(self, validated_data):
        obj=User.objects.create(email=validated_data.get('email'),username=validated_data.get('username'),
                                mobile_number=validated_data.get('mobile_number'),
                                profile_image=validated_data.get('profile_image'),
                                id_proof=validated_data.get('id_proof'))
        
        obj.save()
        return validated_data
class SignSerializer(Serializer):
    email=CharField(error_messages={'required':'email key is required','blank':'email is required'})
    password=CharField(error_messages={'required':'password key is required','blank':'password is required'})
    username=CharField(error_messages={'required':'username key is required','blank':'username is required'})
    mobile_number=CharField(error_messages={'required':'mobile_number key is required','blank':'mobile_number is required'})
    gender=CharField(error_messages={'required':'gender key is required ','blank':'gender is required'})
    profile_image=ImageField(error_messages={'required':'profile_image is required','blank':'profile_image field is required'})
    Id_proof=FileField(error_messages={'required':'id_proof key is required','blank':'id_proof field is required'})
    
    def validate(self,data):
        username=data.get('username')
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise ValidationError("Username already exists")
        return data

    def update(self, validated_data):
        obj=User.objects.create(email=validated_data.get('email'),username=validated_data.get('username'),
                                mobile_number=validated_data.get('mobile_number'),
                                profile_image=validated_data.get('profile_image'),
                                id_proof=validated_data.get('id_proof'))
        
        obj.save()
        return validated_data


class LoginSerializer(Serializer):
    email=CharField(error_messages={'required':'email key is required','blank':'email is required'})
    password=CharField(error_messages={'required':'password key is required','blank':'password is required'})
    token=CharField(read_only=True,required=False)

    def validate(self,data):
        qs=User.objects.filter(email=data.get('email'))
        if not qs.exists():
            raise ValidationError("No account with this email")

        user=qs.first()
        if user.check_password(data.get('password'))==False:
            raise ValidationError("Invalid Password")
        payload =  jwt_payload_handler(user)
        token   =  jwt_encode_handler(payload)
        data['token'] ='JWT '+str(token)
        return data




class ProductSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields=('__all__')