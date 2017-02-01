# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

from django.http import HttpResponse
import csv

try:
        import Image
except ImportError:
        from PIL import Image
import pytesseract

global i
i = 0

def list(request):
    global i
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            i += 1 
            # import ipdb;ipdb.set_trace()
            d = Document.objects.get(id=i)
            
            #print d.docfile
            k=pytesseract.image_to_string(Image.open(d.docfile))
            #print k
            handle = open('data.txt', 'a+')
            handle.write(k)
            handle.close()

            txt_file = r"data.txt"
            csv_file = r'mycsv.csv'

            in_txt = csv.reader(open(txt_file, "rb"), delimiter = ' ')
            out_csv = csv.writer(open(csv_file, 'wb'))

            out_csv.writerows(in_txt)

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myproject.myapp.views.list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
