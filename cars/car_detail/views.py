from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.decorators import method_decorator
from utility.query_builder import QueryBuilder
from django.views.decorators.csrf import csrf_exempt
from configConstants.messages import Messages
from cerberus import Validator
from utility.request_error_format import request_error_messages_formate


# Create your views here.

# This function is used to search cars
@api_view(['GET'])
def search_cars(request):
    try:
        request.page_number = int(request.GET["page_number"]) if request.GET["page_number"] else 0
        request.page_limit = int(request.GET["page_limit"]) if request.GET["page_limit"] else 100

        schema = {
            "search_text": {'type': 'string', 'required': True, 'empty':True},
            "page_limit": {'type': 'integer', 'required': True, 'empty': True},
            "page_number": {'type': 'integer', 'required': True, 'empty': True}
        }
        instance = {
            "search_text":request.GET['search_text'],
            "page_limit": request.page_limit,
            "page_number": request.page_number
        }
        v = Validator()
        if not v.validate(instance, schema):
            return Response(request_error_messages_formate(v.errors), status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    try:
        res = []
        page_limit = request.page_limit
        page_number = request.page_number
        db = QueryBuilder()
        db.cursor.callproc('get_car_detail', [request.GET['search_text'],page_limit,page_number])
        result = db.cursor.fetchall()
        for row in result:
            fetchResult={'cars': row[0]}
            res.append(fetchResult)
        if len(res) > 0:
            return Response({'data':res,'message':Messages.RECORD_FOUND}, status=status.HTTP_200_OK)
        else:
            return Response({'data':res,'message':Messages.NO_RECORD_FOUND}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
            print(str(e))
            return Response({'error': Messages.SOMETHING_WENT_WRONG}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    
   


