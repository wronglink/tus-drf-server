# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.utils.crypto import get_random_string
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.reverse import reverse


def home(request):
    return render_to_response('base.html')


@api_view(['POST'])
def files_root(request, format=None):
    filename = get_random_string(32)
    headers = {
        'Location': reverse('file-upload', kwargs={'filename': filename})
    }
    return Response(status=204, headers=headers)


@api_view(['PATCH'])
@parser_classes([FileUploadParser])
def file_upload(request, filename, format=None):
    file_obj = request.FILES['file']
    return Response(status=204)