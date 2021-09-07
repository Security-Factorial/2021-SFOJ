from django.db.models.fields import NullBooleanField
from django.db.models import Q
from django.http.response import HttpResponseBase
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import BoardForm,UserForm
from .models import *
from django.utils import timezone
from django.core.paginator import Paginator

# main
def index(request):
    return render(request, 'sfoj_system/index.html')



# 문제 리스트 조회
def list(request):
    # parameter
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'old':
        board_list = Board.objects.order_by('Reg_date')
    else:  # recent
        board_list = Board.objects.order_by('-Reg_date')

    # 검색
    if kw:
        board_list = board_list.filter(
            Q(Title__icontains=kw) |  # 제목검색
            Q(Content__icontains=kw) |  # 내용검색
            Q(UserID__username__icontains=kw)  # 문제 글쓴이검색
        ).distinct()

    # 페이징 처리
    paginator = Paginator(board_list, 15)  # 한 페이지에 15개씩
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj, 'page': page, 'kw': kw, 'so': so}
    return render(request, 'sfoj_system/Board_list.html', context)

# 문제 상세
def detail(request, board_index):
    board = get_object_or_404(Board, pk=board_index)
    context = {'Board': board}
    return render(request, 'sfoj_system/Board_detail.html', context)

# 문제 업로드
def uploads(request):
    # post ==> uploads화면에서 저장하기 버튼을 눌렀을 때
    # get ==> list화면에서 문제 업로드 버튼을 눌렀을때
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.UserID = request.user #request에서 로그인한 user를 가져옴
            board.Reg_date = timezone.now()
            board.save()
            return redirect('sfoj_system:list')
    else:
        form = BoardForm()
    context = {'form':form}
    return render(request,'sfoj_system/Board_uploads.html',context)

# 회원가입
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('sfoj_system:index')
    else:
        form = UserForm()
    return render(request, 'common:signup', {'form': form})