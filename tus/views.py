# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from rest_framework import views
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response


def home(request):
    return render_to_response('base.html')


class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)

    def patch(self, request, filename, format=None):
        file_obj = request.FILES['file']
        return Response(status=204)