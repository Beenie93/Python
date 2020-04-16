# Python

### 100 Essential Python Interview Questions - 파이썬 필수 면접 질문 100 가지   
#### 직접 번역을 하기때문에 틀리거나 어색한 부분 있으면 말씀해주시면 감사하겠습니다. 수정하겠습니다.

1. 파이썬은 무엇이고, 장점은 무엇이며 그리고 PEP8을 아십니까?
- 파이썬은 성공적인 인터프리터 언어 중 하나입니다. 파이썬 문서를 작성할 때, 실행 전 컴파일이 필요없습니다.   

  __파이썬 프로그래밍의 장점__   
  * 파이썬은 동적인 언어입니다. 변수들은 선언하면서 데이터 타입을 정의할 필요 없습니다.   
  오류 없이 var1 = 101, var2 = "You are an engineer" 같이 변수 선언을 가능하게 해줍니다.   
  * 파이썬은 컴포지션과 상속과 같은 클래스들을 정의할 수 있는 것과 같은 객체 지향 프로그래밍을 지원합니다.   
  public 또는 private 같은 접근 지정자를 사용하지 않습니다.
  * 파이썬에서 함수들은 일급 객체 같습니다. 함수를 매개변수로 넘기거나 다른 함수들로부터 반환하는 변수에 할당할 수 있습니다.
  * 파이썬을 이용하여 개발하는 것은 빠르지만 가끔 컴파일된 언어보다 느립니다. 운좋게도, 파이썬은 코드를 최적화 할 수 있게 하기 위해 "C" 언어 확장을 가능하게 할 수 있습니다.
  * 파이썬은 웹 기반 앱, 자동화 테스트, 데이터 모델링, 빅데이터 분석과 같이 많이 사용됩니다. 또는, 파이썬을 다른 언어들과 작업을 할 수 있게 glue layer로서 이용할 수 있습니다.

  __PEP 8.__   
  PEP 8은 권장된 코딩 집합인 최신 파이썬 코딩 표준 규격입니다. 파이썬 코드를 조금 더 읽기 쉽게 전달해주게 해줍니다.   

2. 다음 파이썬 코드의 출력은 어떻게 나올까요?
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
3. 




## Reference
* TechBeamers
<https://www.techbeamers.com/python-interview-questions-programmers/>


