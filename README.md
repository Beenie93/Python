# Python

### 100 Essential Python Interview Questions - Python 필수 면접 질문 100 가지   
#### 직접 번역을 하기때문에 틀리거나 어색한 부분이 있을  말씀해주시면 감사하겠습니다. 수정하겠습니다.

__1. Python은 무엇이고, 장점은 무엇이며 그리고 PEP8을 아십니까?__
- Python은 성공적인 인터프리터 언어 중 하나입니다. Python 문서를 작성할 때, 실행 전 컴파일이 필요없습니다.   

  __Python 프로그래밍의 장점__   
  * Python은 동적인 언어입니다. 변수들은 선언하면서 데이터 타입을 정의할 필요 없습니다.   
  오류 없이 var1 = 101, var2 = "You are an engineer" 같이 변수 선언을 가능하게 해줍니다.   
  * Python은 컴포지션과 상속과 같은 클래스들을 정의할 수 있는 것과 같은 객체 지향 프로그래밍을 지원합니다.   
  public 또는 private 같은 접근 지정자를 사용하지 않습니다.
  * Python에서 함수들은 일급 객체 같습니다. 함수를 매개변수로 넘기거나 다른 함수들로부터 반환하는 변수에 할당할 수 있습니다.
  * Python을 이용하여 개발하는 것은 빠르지만 가끔 컴파일된 언어보다 느립니다. 운좋게도, Python은 코드를 최적화 할 수 있게 하기 위해 "C" 언어 확장을 가능하게 할 수 있습니다.
  * Python은 웹 기반 앱, 자동화 테스트, 데이터 모델링, 빅데이터 분석과 같이 많이 사용됩니다. 또는, Python을 다른 언어들과 작업을 할 수 있게 glue layer로서 이용할 수 있습니다.

  __PEP 8.__   
  PEP 8은 권장된 코딩 집합인 최신 Python 코딩 표준 규격입니다. Python 코드를 조금 더 읽기 쉽게 전달해주게 해줍니다.   

__2. 다음 Python 코드의 출력은 어떻게 나올까요?__
```python   
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3
```   
   __result__   
```python
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
```   
매번 extendList 함수가 호출 될때마다 list 인자가 []의 디폴트 값에 초기화 될 것이라고 생각하면서 list1 = [10] 이고 list3 = ['a']라고 잘못되게 예상할지도 모릅니다.   
   
그러나, 새로운 리스트는 함수가 정의된 후 한번 생성된 것을 얻는 것으로 동작합니다. 그리고 해당 리스트는 누군가 entendList 함수를 list 인자 없이 호출할때마다 사용되어집니다. 표현의 계산이 호출하는 동안이 아니라 함수 정의 시간에 발생하기 때문에 이러한 방식으로 동작합니다.   
   
따라서 list1 과 list3은 같은 디폴트 리스트에서 동작합니다. 반면에 list2는 (리스트 파라미터 값으로서 빈 리스트를 줌으로써) 자신 고유의 리스트를 생성한 개별 객체에서 실행됩니다.   
   
extendList 함수의 정의는 다음과 같은 방식으로 변경될 수 있습니다.   
```python
def extendList(val, list=None):
  if list is None:
    list = []
  list.append(val)
  return list
```   
이렇게 수정된 결과로, 출력값은   
```python
list1 = [10]
list2 = [123]
list3 = ['a']
```   

__3. 프로그램이 어떠한 행위를 할 필요는 없지만 구문이 필요할 경우 Python에서 사용될 수 있는 명령문은 무엇일까요?__   
   
pass 명령문은 무의미한 작업입니다. 실행할 때 아무런 일도 일어나지 않습니다. 반드시 소문자로 "pass"를 사용해야 합니다. "Pass"로 작성할 경우 
“NameError: name Pass is not defined.” 라는 에러를 마주할 수 있습니다. Python 명령문은 대소문자를 구별합니다.   
```python
letter = "hai sethuraman"
for i in letter:
    if i == "a":
        pass
        print("pass statement is execute ..............")
    else:
        print(i)
```   

__4. Python에서 '~'를 사용하여 홈 디렉토리를 얻기위한 프로세스는 무엇일까요?__   
   
os 모듈을 임포트한 뒤 아래와 같이 한줄을 작성하세요.
```python
import os
print (os.path.expanduser('~'))
```   
Output:   
```python
/home/runner
```   

__5. Python에서 내장된 자료형은 무엇이 있을까요?__   
   
Python이 지원하는 가장 일반적으로 사용되는 자료형이 있습니다.   
- Immutable built-in datatypes of Python   
  - Numbers
  - Strings
  - Tuples   

- Mutable built-in datatypes of Python   
  - List
  - Dictionaries
  - Sets   

__6. Python app에서 버그를 찾거나 정적 분석을 수행하는 방법은?__   
   
- 정적 분석기인 PyChecker를 사용할 수 있습니다. Python 프로젝트에서 버그를 확인하고 버그와 관련된 복잡성과 유형을 보여줍니다.   
- Python 모듈이 코딩 표준을 만족하는지 확인하는 Pylint를 사용할 수도 있습니다.   

__7. 언제 Python decorator가 사용되나요?__   
   
Python decorator은 기능을 빠르게 조정하는 Python 구문에서 사용하는 relative change(어떻게 번역할 지 모르겠습니다. 아시는 분 알려주시면 감사하겠습니다.) 입니다.   

__8. 튜플과 리스트 사이에 주된 차이점은 무엇인가요?__   
   
__List vs. Tuple__   
튜플과 리스트 사이에 주된 차이점은 리스트는 mutable하지만 튜플은 immutable한 것 입니다.   
튜플은 해쉬되어질 수 있습니다. 예를 들어, 튜플을 딕셔너리의 키로 사용합니다.   

__9. Python은 어떻게 메모리 관리를 하나요?__   
   
- Python은 메모리를 유지하기 위해 private heap을 사용합니다. 그래서 heap은 모든 파이썬 객체와 자료구조를 담고 있습니다. 이 영역은 오직 Python 인터프리터에게만 접근할 수 있게 하고 프로그래머는 사용할 수 없습니다.   
- 그리고 Python 메모리 관리자가 이러한 private heap을 다룹니다. Python 객체들을 위한 메모리 할당 요청이 필요합니다.   
- Python은 사용하지 않는 모든 메모리를 구조하고 heap 공간에서 빼내는 내장된 garbage collector를 사용합니다.   

__10. lambda와 def 사이에 주된 차이점은 무엇인가요?__   
   
__Lambda vs. def__   
- Def는 다양한 표현을 담을 수 있지만 lambda는 단일 표현 함수입니다.   
- Def는 함수를 생성하고 이름을 명시하여 나중에 호출할 수 있게 합니다. Lambda는 함수 객체를 형성하고 반환합니다.   
- Def는 return문을 가질 수 있습니다. Lambda는 return문을 가질 수 없습니다.   
- Lambda는 리스트와 딕셔너리 내부에서 사용될 수 있게 지원합니다.   

__11. 


## Reference
* TechBeamers
<https://www.techbeamers.com/python-interview-questions-programmers/>


