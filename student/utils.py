from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import status

class BaseCRUDAPIController(APIView):
    """
    Abstract CRUD api methods
    """
    model = None
    serializer = None
    permission_classes = (AllowAny,)

    def post(self,request):
        post_data=self.serializer(data=request.data)
        if post_data is None:
            return Response(post_data.errors, f"Invalid post data")
        else:
            if post_data.isvalid():
                post_data.save()
                return Response(post_data.data,status=status.HTTP_201_CREATED)
            return Response(post_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self,id):
        get_data = self.model.objects.get(id=id)
        if get_data is None:
            return f"item where id = {id} does not exist"
        else:
            serializer = self.serializer(get_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
           
    def put(self,request,id):
        put_data=self.model.objects.get(id=id)
        if put_data is None:
            return Response(put_data.errors,f"invalid data,try again")
        else:
            serializer = self.serializer(put_data, request.data)
            if serializer.isvalid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,id):
        delete_data=self.model.objects.get(id=id)
        if delete_data.isNone():
            return Response(delete_data.errors,f"item cannot be deleted")
        else:
            delete_data.delete(status=status.HTTP_200_OK, message="Item successfully deleted")



        


    