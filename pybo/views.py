from django.shortcuts import render
from django.shortcuts import render,get_object_or_404, redirect #redirect란?
from django.utils import timezone
from .models import Question
from .forms import QuestionForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    """
    pybo 목록 출력
    """
    page = request.GET.get('page', '1')  # 페이지
    #조회
    question_list = Question.objects.order_by('-create_date') #질문목록 데이터 얻기 order -by 작성일시 역순으로정렬
    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request,'pybo/question_list.html',context) #render는 파이썬 데이터를 템플릿에 적용, html로 반환


def detail(request, question_id):    #질문의 내용 출력 함수
    """
    pybo 내용 출력
    """
    #question=Question.objects.get(id=question_id)  #get은 개체가 하나일때만 씀
    question = get_object_or_404(Question, pk=question_id) # 페이지가 넘어가면 404 에러표시
    context={'question':question}
    return render (request,'pybo/question_detail.html',context)

@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question=get_object_or_404(Question, pk=question_id)
    #question.answer_set.create(content=request.POST.get('content'),create_date=timezone.now())
    # 답변을 생성하기 위해 question.asnswer_set.create 를 사용,
    # request.POST.get('content')는 POST로 전송된 폼(form) 데이터 항목 중 content 값을 의미
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author=request.user #author 속성에 로그인 계정 저장
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):  #중요!
    """
    pybo 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # author 속성에 로그인 계정 저장
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context)
# Create your views here.
