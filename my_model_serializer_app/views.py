from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import ContactSerializer
from .models import Contact

class ContactAPIView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        data = request.data
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        return Response({"msg":"Successful saved"})
    
    def get(self, request):
        querySet = Contact.objects.all()    # if i wanna individual value then replace all() => .get(id=1) & many=False
        serializer = ContactSerializer(querySet, many=True)
        return Response(serializer.data)
