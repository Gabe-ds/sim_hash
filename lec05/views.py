from django.shortcuts import redirect, render
from django.views.generic import DeleteView, FormView, ListView

from .lec05_process import *
from lec04.models import ImageData
from .forms import *
from .models import *

class DetailView(ListView):
    template_name = 'lec05/detail.html'
    model = ImageData
    
    # def post(self, request, *args, **kwargs):
        
    
class SimilarityView(ListView):
    template_name = 'lec05/similarity.html'
    model = ImageData
    
class DoAHashView(FormView):
    template_name = 'lec05/do_ahash.html'
    form_class = UploadImageAHashForm
    
    def form_valid(self, form):
        image = AHashData()
        image.image = form.cleaned_data["image"]
        get_ahash = average_hash(image.image)
        image.ahash = np2hash(get_ahash)
        image.save()
        
        # print(get_ahash)
        # print(np2hash(get_ahash))
        
        return redirect("lec05:ahash_list")
    
class AHashListView(ListView):
    template_name = 'lec05/ahash_list.html'
    model = AHashData
    
    def check(self, request, *args, **kwargs):
        f_value = request.POST.get('check[]')
        check_value = request.POST.getlist("check[]")
        
        for i in len(check_value):
            if f_value[0].ahash == check_value[i+1]:
                text = 'あります．' + i
            else:
                safe = 'ありません．'
        
        print(check_value)
        context = {
            'text': text,
            'safe': safe,
        }
        
        return render(request, 'lec05/check.html', context)
    
class DeleteView(DeleteView):
    template_name = 'lec05/delete.html'
    model = AHashData
    success_url = '/lec05/ahash_list'