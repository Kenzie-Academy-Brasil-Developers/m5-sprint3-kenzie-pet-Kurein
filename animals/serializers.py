from rest_framework import serializers
from rest_framework.views import status

from animals.models import Animal
from characteristics.models import Characteristic
from groups.models import Group

from groups.serializers import GroupSerializer
from characteristics.serializers import CharacteristicSerializer

class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField(max_length=15)

    group = GroupSerializer()

    characteristics = CharacteristicSerializer(many=True)

    def create(self, validated_data):
        print("depois de validar", validated_data)
        group = validated_data.pop("group")
        characteristics = validated_data.pop("characteristics")

        group, _ = Group.objects.get_or_create(group)

        animal = Animal.objects.create(**validated_data, group=group)

        for item in characteristics:
            item, _ = Characteristic.objects.get_or_create(**item)
            animal.characteristics.add(item)

        return animal

    def update(self, instance, validated_data):

        if validated_data.get("sex"):
            raise ValueError({"error": "You cannot update sex property"}, status.HTTP_422_UNPROCESSABLE_ENTITY)

        if validated_data.get("group"):
            raise ValueError({"error": "You cannot update group property"}, status.HTTP_422_UNPROCESSABLE_ENTITY)

        if validated_data.get("characteristics"):
            raise ValueError({"error": "You cannot update characteristics property"}, status.HTTP_422_UNPROCESSABLE_ENTITY)

        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.save()

        return instance