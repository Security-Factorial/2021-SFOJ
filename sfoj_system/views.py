from django.db.models.fields import NullBooleanField
from django.http.response import HttpResponseBase
from django.shortcuts import get_object_or_404, render, redirect

# Create your views here.
from django.http import HttpResponse

from .forms import BoardForm
from .models import *
from django.utils import timezone

# main
def index(request):
    return render(request, 'sfoj_system/index.html')

# 문제 리스트 조회
def list(request):
    board_list = Board.objects.order_by('Reg_date')
    context = {'Board_list': board_list}
    return render(request, 'sfoj_system/Board_list.html', context)

# 각 문제 조회
def detail(request, board_index):
    board = get_object_or_404(Board, pk=board_index)
    context = {'Board': board}
    return render(request, 'sfoj_system/Board_detail.html', context)

# 문제 업로드
def uploads(request):
    """
    문제 업로드
    """
    # post ==> uploads화면에서 저장하기 버튼을 눌렀을 때
    # get ==> list화면에서 문제 업로드 버튼을 눌렀을때
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.Reg_date = timezone.now()
            board.save()
            return redirect('sfoj_system:list')
    else:
        form = BoardForm()
    context = {'form':form}
    return render(request,'sfoj_system/Board_uploads.html',context)

