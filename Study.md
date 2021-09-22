### URL 하드코딩
<<<<<<< HEAD

URL 링크의 구조가 자주 변경된다면 템플릿에서 사용한 모든 URL들을 일일이 찾아가며 수정해야 하는 리스크가 발생한다. 
이러한 문제점을 해결하기 위해서는 해당 URL에 대한 실제 링크 대신 링크의 주소가 매핑되어 있는 별칭을 사용해야 한다.

### 템플릿 상속

템플릿 상속은 기본 틀이 되는 템플릿을 먼저 작성하고 다른 템플릿에서 그 템플릿을 상속해 사용하는 방법이다.



페이징 객체 `page_obj`에는 다음과 같은 속성들이 있다.

| 항목                 | 설명                                |
| :------------------- | :---------------------------------- |
| paginator.count      | 전체 게시물 개수                    |
| paginator.per_page   | 페이지당 보여줄 게시물 개수         |
| paginator.page_range | 페이지 범위                         |
| number               | 현재 페이지 번호                    |
| previous_page_number | 이전 페이지 번호                    |
| next_page_number     | 다음 페이지 번호                    |
| has_previous         | 이전 페이지 유무                    |
| has_next             | 다음 페이지 유무                    |
| start_index          | 현재 페이지 시작 인덱스(1부터 시작) |
| end_index            | 현재 페이지의 끝 인덱스(1부터 시작) |

페이징 기능코드이전 페이지가 있는지 체크`{% if question_list.has_previous %}`

이전 페이지 번호`{{ question_list.previous_page_number }}`

다음 페이지가 있는지 체크`{% if question_list.has_next %}`

다음 페이지 번호`{{ question_list.next_page_number }}`

페이지 리스트 루프`{% for page_number in question_list.paginator.page_range %}`

현재 페이지와 같은지 체크`{% if page_number == question_list.number %}`

