from django.shortcuts import redirect, render
from django.views.generic import DeleteView, FormView, ListView

from .lec04_process import *
from lec05.lec05_process import *
from .forms import *
from .models import *

class UploadView(FormView):
    template_name = 'lec04/upload.html'
    form_class = UploadImageForm
    
    def form_valid(self, form):
        image = ImageData()
        image.image = form.cleaned_data["image"]
        rgb_list = ext_mean_rgb(image.image)
        image.r = rgb_list[0]
        image.g = rgb_list[1]
        image.b = rgb_list[2]
        image.save()
        
        return redirect("lec04:upload_list")
    
class UploadListView(ListView):
    template_name = 'lec04/upload_list.html'
    model = ImageData
    
    def post(self, request, *args, **kwargs):
        checks_value = request.POST.getlist('checks[]')
        
        # 選択した画像をdbから呼び出す
        for i in range(len(checks_value)):
            if i == 1:
                img_1 = ImageData.objects.get(pk=int(checks_value[i]))
            else:
                img_2 = ImageData.objects.get(pk=int(checks_value[i]))
        
        X = np.array([img_1.r, img_1.g, img_1.b])
        Y = np.array([img_2.r, img_2.g, img_2.b])
        
        # コサイン類似度を求める
        result = comp_sin(X, Y)
        
        context = {
            "img_1": img_1.id,
            "img_2": img_2.id,
            "img_1_path": img_1.image,
            "img_2_path": img_2.image,
            "result": result,
        }
        
        return render(request, 'lec05/similarity.html', context)
    
class DeleteView(DeleteView):
    template_name = 'lec04/delete.html'
    model = ImageData
    success_url = '/lec04/upload_list'