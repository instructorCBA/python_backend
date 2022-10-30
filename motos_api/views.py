# motos_api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Moto
from .serializers import MotoSerializer

# First endpoint view; HTTP methods: GET-All Records POST-New Record
class MotoListApiView(APIView):

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the moto items for given requested user
        '''
        #todos = Moto.objects.filter(user = all)
        motos = Moto.objects
        serializer = MotoSerializer(motos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        '''
        Create the Moto with given moto data
        '''
        data = {
            'trademark': request.data.get('trademark'), 
            'model': request.data.get('model'), 
            'reference': request.data.get('reference'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        serializer = MotoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# Second endpoint view. HTTP methods: GET-Read Record PUT-Update Record DELETE-Delete Record
class MotoDetailApiView(APIView):

    def get_object(self, moto_id):
          '''
          Helper method to get the object with given moto_id
          '''
          try:
               return Moto.objects.get(id=moto_id)
          except Moto.DoesNotExist:
               return None

    # 3. Retrieve
    def get(self, request, moto_id, *args, **kwargs):
        '''
        Retrieves the Moto with given moto_id
        '''
        moto_instance = self.get_object(moto_id)
        if not moto_instance:
            return Response(
                {"res": "Object with moto id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MotoSerializer(moto_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, moto_id, *args, **kwargs):
        '''
        Updates the moto item with given moto_id if exists
        '''
        moto_instance = self.get_object(moto_id)
        if not moto_instance:
            return Response(
                {"res": "Object with moto id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'trademark': request.data.get('trademark'), 
            'model': request.data.get('model'), 
            'reference': request.data.get('reference'),
            'price': request.data.get('price'),
            'image': request.data.get('image'),
            'supplier': request.data.get('supplier'),
        }
        serializer = MotoSerializer(instance = moto_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, moto_id, *args, **kwargs):
        '''
        Deletes the moto item with given moto_id if exists
        '''
        moto_instance = self.get_object(moto_id)
        if not moto_instance:
            return Response(
                {"res": "Object with moto id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        moto_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )