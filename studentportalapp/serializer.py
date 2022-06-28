# from rest_framework import serializers
# from studentportalapp.models import Book

# class BookSerializer(serializers.Serializer):
#     id =serializers.IntegerField(read_only=True)
#     title =serializers.CharField()
#     number_of_pages = serializers.IntegerField()
#     publish_date=serializers.DateField()
#     quantity=serializers.IntegerField()

#     def create(self, data):
#         return Book.objects.create(**data) 

#     def update(self,instance,data):
#         instance.title=data.get('title',instance.title)
#         instance.number_of_pages=data.get('number_of_pages',instance.number_of_pages)
#         instance.publish_date=data.get('publish_date',instance.publish_date)
#         instance.quantity=data.get('quantity',instance.quantity)
        
#         instance.save()
#         return instance
from django.forms import ValidationError
from rest_framework import serializers
from studentportalapp.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"

    def validate_title(self, value):
        if  value =="violance":
            raise ValidationError("No violance please")
        return value    

    def validate(self,data):
          if data["number_of_pages"]>200 and data["quantity"]>600:
            raise ValidationError("too heavy")
          return data