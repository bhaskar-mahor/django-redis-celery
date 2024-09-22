from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utils.tasks import celery_task
# Create your views here.
class Users(APIView):
    '''
    '''
    def post(self, request):
        return Response({'isSuccess':True})
    
    def get(self,request):
        try:
            data = {'email_list':['example@mail.com','example1@mail.com','example2@mail.com']}
            task = celery_task.delay(data)
            print(f"Task ID: {task.id}")
            # Return the task ID in the response
            return Response({'isSuccess': True, 'task_id': task.id}, status=status.HTTP_200_OK)
            
        except Exception as e:
            print("get method error ",e)