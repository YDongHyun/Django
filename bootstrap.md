* 기본클래스
container - 화면크기에 따라 조정
container-fluid - 무조건 화면을 꽉채움





//============

* 화면 크기 설정

<div class="col-[전체]-[부분]"></div>



	- 전체 넓이

    xs (  < 768px : 폰)

    sm ( >= 768px : 태블릿)

    md ( >= 992px : 노트북)

    lg ( >= 1200px : 데스크탑)



	- 부분 크기 : 1~12



//========

* 테이블

	- .table-condensed : 압축 크기

<table class="table table-condensed">



	- 반응형 테이블

<div class="table-responsive">          

  <table class="table">





//========

* 이미지

	- 반응형 이미지

<img class="img-responsive" src="img_chania.jpg" alt="Chania" width="460" height="345"> 



	- 갤러리

<div class="thumbnail">



	- 반응형 Embeds(iframe)

 <div class="embed-responsive embed-responsive-16by9">

  <iframe class="embed-responsive-item" src="..."></iframe>

</div> 





//========



* border 모양 변화 - 가장자리 라운드 모양으로 

<div class="well well-lg">Large Well</div>





* 닫히는 알림판

  <div class="alert alert-success alert-dismissible">

    <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>

    <strong>Success!</strong> This alert box could indicate a successful or positive action.

  </div>



//=========

* 버튼

https://www.w3schools.com/bootstrap/bootstrap_buttons.asp





* 아이콘 제공 - Glyphicons

Glyphicons

https://www.w3schools.com/bootstrap/bootstrap_glyphicons.asp

https://www.w3schools.com/bootstrap/bootstrap_ref_comp_glyphs.asp

https://glyphicons.bootstrapcheatsheets.com/

https://marcoceppi.github.io/bootstrap-glyphicons/



<p>Envelope icon: <span class="glyphicon glyphicon-envelope"></span></p>    



	- 색 변경

<span class="glyphicon glyphicon-user" style="color: blue"></span>

	

	- 크기 변경

<i class="glyphicon glyphicon-camera" style="font-size: 50px; color: blue"></i>





//=========

* 드롭다운 메뉴

<div class="dropdown">



	- Accordion 

https://www.w3schools.com/bootstrap/tryit.asp?filename=trybs_collapsible_accordion&stacked=h





Navigation Bar

https://www.w3schools.com/bootstrap/bootstrap_navbar.asp





Inputs 장식

https://www.w3schools.com/bootstrap/bootstrap_forms_inputs2.asp



* Carousel Plugin(회전목마, 그림 슬라이드)

https://www.w3schools.com/bootstrap/bootstrap_carousel.asp



* Modal - 팝업 상자

https://www.w3schools.com/bootstrap/bootstrap_modal.asp





//===============

* 툴팁, Tooltip 

	tooltip.js 만 포함 가능

<li><a href="#" data-toggle="tooltip"  title="Hooray!" >Top</a></li>



	- 색깔, 크기 변경

<style>

.tooltip2 + .tooltip > .tooltip-inner {background-color: #f00; font-size: 14px; }

</style>



<li><a href="#" data-toggle="tooltip"  class="tooltip2" title="Hooray!" >Top</a></li>



//===============

Affix Plugin

	- 스크롤시 고정되는 부분 생성







//============================================================

//참고

Bootstrap

	- 트위터에서 만든 웹 디자인 프레임워크

	- 반응형 웹을 만들기 위한 모든 요소를 담고 있음(폰트, 버튼, 아이콘 등)





< 기본 예제 >

https://www.w3schools.com/bootstrap/bootstrap_get_started.asp



<!DOCTYPE html>

<html lang="en">

<head>

  <title>Bootstrap Example</title>

  <meta charset="utf-8">

  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

</head>

<body>



<div class="container">

  <h1>My First Bootstrap Page</h1>

  <p>This is some text.</p> 

</div>



</body>

</html>







//============

< 예제 > 

offcanvas layout pattern

	- 메뉴

http://bootstrapk.com/examples/offcanvas/#



Theme example

	- table

http://bootstrapk.com/examples/theme/





//=============================

< 부트스트랩을 로컬에 설치 >

http://bootstrapk.com/getting-started/

* npm 설치

curl -L https://npmjs.org/install.sh | sudo sh

	- 또는 Node.js 설치





* Bootstrap 설치

npm install bootstrap



* SASS 설치

	- *.sass 파일을 *.css 파일로 변환

npm install -g sass



* Grunt 설치

	- 패키지 빌드 자동화 툴

npm install -g grunt-cli





//=============================

< CSS PreProcessor >

	CSS vendor prefixes 

	- CSS 를 구조적 언어로 편리하게 작성한후 CSS로 변환



* SASS 

	- 설치

npm install -g sass





	- test.sass 

$font-stack:    Helvetica, sans-serif

$primary-color: #333

body

  font: 100% $font-stack

  color: $primary-color





	- 변환

sass test.sass test.css







//===================

* Grunt (빌드 시스템)

	- JavaScript Task Runner, JavaScript 프로젝트 관리를 위한 build-tool

	- 프로젝트 build시에 원하는 작업( concatenating, minifying, validating 등) 자동화



Grunt 소개 및 사용법

http://nuli.navercorp.com/sharing/blog/post/1132682
