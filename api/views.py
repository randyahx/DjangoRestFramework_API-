from api.models import Messages
from django.contrib.auth.models import User
from api.serializers import MessagesSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from api.permissions import IsOwnerOrReadOnly

"""Using Viewsets remove the need for individual view classes(MessagesListCreate, MessagesUpdateDelete)"""


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """/api/"""
    """Retrieve Objects, Convert into Json, Return Json"""
    """Get ALL or Create"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MessagesViewSet(viewsets.ModelViewSet):
    """/api/"""
    """Retrieve Objects, Convert into Json, Return Json"""
    """Get ALL or Create"""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer

    """Pass 'owner' as field when saving messages"""
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



"""Class based API, using generics the code below can be removed since it does everything"""
#
# class AccountsListCreate(APIView):
#     """/api/"""
#     """Retrieve Objects, Convert into Json, Return Json"""
#     """Get ALL or Create"""
#     def get(self, request, format=None):
#         api = Accounts.objects.all()
#         serializer = AccountsSerializer(api, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = AccountsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class AccountsGetUpdateDelete(APIView):
#     """format(urls.py) allows /account/2.json"""
#     """/api/<int:pk>"""
#     """Get specific object with pk, Update or Delete"""
#     def get_object(self):
#         try:
#             return Accounts.objects.get(pk=pk)
#         except Accounts.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         api = self.get_object(pk)
#         serializer = AccountsSerializer(api)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         api = self.get_object(pk)
#         serializer = AccountsSerializer(api, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         api = self.get_object(pk)
#         api.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#
#
# @api_view(['GET', 'POST'])
# def accounts_GETALLorCREATE(request, format=None):
#     """/api/"""
#     """Retrieve Objects, Convert into Json, Return Json"""
#     """Get ALL or Create"""
#     if request.method == 'GET':
#         api = Accounts.objects.all()
#         serializer = AccountsSerializer(api, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = AccountsSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @api_view(['GET', 'PUT', 'DELETE'])
# def accounts_GETPKorUPDATE(request, pk, format=None):  """format(urls.py) allows /account/2.json"""
#     """/api/<int:pk>"""
#     """Get specific object with pk, Update or Delete"""
#     try:
#         api = Accounts.objects.get(pk=pk)
#     except Accounts.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = AccountsSerializer(api)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = AccountsSerializer(api, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         api.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)