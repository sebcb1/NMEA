from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from api.models import Trame
import logging

logger = logging.getLogger(__name__)

def trames(request):

    logger.error('### api/trames started')

    if request.method=='POST':
        logger.error('### api/trames method: POST')
        value=request.GET["content"]
        logger.error('### api/trames var value:'+ str(value))
        trame = Trame(content=value)
        trame.save()
        return HttpResponse("{ error: False }\n")
    else:
        return HttpResponse("{ error: True, msg: 'Only POST allowed'}\n")

    
