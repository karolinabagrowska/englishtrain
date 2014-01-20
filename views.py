from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.utils.translation import ugettext as _
from staticpage.models import Page


def home_page(request):
    """ view for each individual category page """
    

    
    title = _("Home page")
    text1 = Page.objects.get(pk=1)
    text2 = Page.objects.get(pk=2)
    text3 = Page.objects.get(pk=3)

    return render_to_response('index.html',
                              locals(),
                              context_instance=RequestContext(request))


