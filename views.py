from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import models

OVER_SCHOOL = ['GIAM_DOC_SO', 'TRUONG_PHONG']

def index(request):
    if not request.user.is_authenticated():
        return render_to_response("index.html", context_instance=RequestContext(request)) 
    elif request.user.is_superuser or request.user.get_profile().position in OVER_SCHOOL :
        return render_to_response("index.html", context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('school_index'))

@models.permalink
def get_absolute_url(self):
        return 'profiles_profile_detail', (), { 'username': self.user.username }
get_absolute_url = models.permalink(get_absolute_url)
