from asyncore import read
import numbers
from turtle import title
from venv import create
from rest_framework import serializers
from studentportalapp.models import Book

class BookSerializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True)
    title =serializers.CharField()
    number_of_pages = serializers.IntegerField()
    publish_date=serializers.DateField()
    quantity=serializers.IntegerField()

    def create(self, data):
        return Book.objects.create(**data) 

    def update(self,instance,data):
        instance.title=data.get('title',instance.title)
        instance.number_of_pages=data.get('number_of_pages',instance.number_of_pages)
        instance.publish_date=data.get('publish_date',instance.publish_date)
        instance.quantity=data.get('quantity',instance.quantity)
        
        instance.save()
        return instance