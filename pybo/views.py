from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from .models import Question

def index(request):
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date') #질문목록 데이터 얻기 order -by 작성일시 역순으로정렬
    context={'question_list':question_list}
    return render(request,'pybo/question_list.html',context) #render는 파이썬 데이터를 템플릿에 적용, html로 반환

def detail(request, question_id):    #질문의 내용 출력 함수
    """
    pybo 내용 출력
    """
    #question=Question.objects.get(id=question_id)  #get은 개체가 하나일때만 씀
    question = get_object_or_404(Question, pk=question_id) # 페이지가 넘어가면 404 에러표시
    context={'question':question}
    return render (request,'pybo/question_detail.html',context)
# Create your views here.
