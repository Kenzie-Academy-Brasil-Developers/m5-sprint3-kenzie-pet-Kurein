from functools import partial
from rest_framework.views import APIView, Request, Response, status

from animals.models import Animal
from animals.serializers import AnimalSerializer


class AnimalView(APIView):
    def get(self, _:Request):
        animals = Animal.objects.all()
        serialized = AnimalSerializer(instance=animals, many=True)

        return Response({"animals": serialized.data}, status.HTTP_200_OK)

    def post(self, req:Request):
        serialized = AnimalSerializer(data=req.data)
        print("antes de validar", serialized)
        serialized.is_valid(raise_exception=True)
        serialized.save()

        return Response(serialized.data, status.HTTP_201_CREATED)

class AnimalIdView(APIView):
    def get(self, _:Request, animal_id):
        try:
            animal = Animal.objects.get(id=animal_id)
            serialized = AnimalSerializer(instance=animal)

            return Response({"animal": serialized.data}, status.HTTP_200_OK)
        except:
            return Response({"error": "animal does not exist"}, status.HTTP_404_NOT_FOUND)

    def patch(self, req:Request, animal_id):

        try:
            animal = Animal.objects.get(id=animal_id)
            serialized = AnimalSerializer(animal, req.data, partial=True)
            serialized.is_valid()

            serialized.save()

            return Response({"animal": serialized.data}, status.HTTP_200_OK)
        except ValueError as err:
            return Response(*err.args)
        except:
            return Response({"error": "animal does not exist"}, status.HTTP_404_NOT_FOUND)

    
    def delete(self, _:Request, animal_id):
        try:
            animal = Animal.objects.get(id=animal_id)
            animal.delete()

            return Response("", status.HTTP_204_NO_CONTENT)
        except:
            return Response({"error": "animal does not exist"}, status.HTTP_404_NOT_FOUND)