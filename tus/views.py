# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.utils.crypto import get_random_string
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView


def home(request):
    return render_to_response('base.html')


@api_view(['POST'])
def files_root(request, format=None):
    filename = get_random_string(32)
    headers = {
        'Location': reverse('file-upload', kwargs={'filename': filename})
    }
    return Response(status=201, headers=headers)


class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def head(self, request, filename, format=None):
        # TODO: Implement right offset header
        return Response(status=204, headers={'Offset': 0})

    def patch(self, request, filename, format=None):
        file_obj = request.FILES['file']
        # TODO: Implement uploaded chunk handing
        return Response(status=204)
