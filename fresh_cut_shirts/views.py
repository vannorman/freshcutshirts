import json
import uuid
import urllib
import datetime
import re 
import requests # for setting cookies

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.base import RedirectView
from django.utils import timezone
from django.contrib import auth
#from django.forms.util import ErrorList
from django.template.context import RequestContext
from django.shortcuts import render
from django.shortcuts import render, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

import markdown
md = markdown.Markdown()

#import requests

from fresh_cut_shirts.util import *
def simple_page(template):
	def handler(request):
		return renderWithNav(request, template)
	return handler


def home(request):
	obj = {}
    # look ma no SQL!
	obj['shirts'] = []
	obj['shirts'].append({
		"title" : "We are not the same",
		"link" : "",
        "description" : "Traditional pure meme",
		"images" : [	
            '/static/img/shirt_notthesame_pure.jpg'   
		],
	})
							

	return renderWithNav(request,'home.html', obj)

def file_a(request):
	return HttpResponse("7GN_wPd4X1PrCxmqKOrw9sHsAd0_uayFhOnWdEw6Ytc.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")

def file_b(request):
	return HttpResponse("Z9DF236bXRfXjvGlUflaI98PMWAKsG9qpGnrDXllb2o.HrFduo8MJADNQACN38q371h8yDpWwuARiTcP3lgNOOM")	


def test(request):
    return renderWithNav(request,"test.html", {})

