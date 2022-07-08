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