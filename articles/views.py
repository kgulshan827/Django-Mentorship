from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticleForm

def articleList(request):
    articles = Articles.objects.all().order_by('date')
    return render(request, 'articleList.html', { 'articles': articles })

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return redirect('list')
    else:
      form = ArticleForm()
    return render(request,'articleForm.html',{'form':form})