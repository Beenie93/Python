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

__3. 프로그램이 어떠한 행위를 할 필요는 없지만 구문이 필요할 경우 Python에서 사용될 수 있는 문법은 무엇일까요?__   
   
pass문은 무의미한 작업입니다. 실행할 때 아무런 일도 일어나지 않습니다. 반드시 소문자로 "pass"를 사용해야 합니다. "Pass"로 작성할 경우 
“NameError: name Pass is not defined.” 라는 에러를 마주할 수 있습니다. Python 문법은 대소문자를 구별합니다.   
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
출력 결과:   
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

__11. Python 모듈 "re"를 사용하여 email id를 확인하는 정규표현식을 작성해보세요.__   
   
[코딩 도장](https://dojang.io/mod/page/view.php?id=2454) 추가 설명 - 정규표현식은 일정한 규칙을 가진 문자열을 표현하는 방법입니다. 문자열 속에서 특정한 규칙으로 된 문자열을 검색한 뒤 추출하거나 바꿀 때, 문자열이 정해진 규칙에 맞는지 판단할 때 사용합니다.   
   
Python은 정규표현식 모듈 "re"를 가지고 있습니다.   
서브도메인에 있는 .com과 .co.를 검사하여 email id를 확인할 수 있는 "re" 표현법을 확인해보세요.   
```python
import re
print(re.search(r"[0-9a-zA-Z.]+@[a-zA-Z]+\.(com|co\.in)$","micheal.pages@mp.com"))
```   

__12. 다음 코드의 결과가 무엇일까요? 코드에 에러가 있나요?__   
   
```python
list = ['a', 'b', 'c', 'd', 'e']
print (list[10:])
```   
위의 코드의 결과는 []입니다. IndexError와 같은 어떠한 에러도 있지 않습니다.   
   
원소 수를 넘어가는 인덱스를 사용하여 리스트로부터 원소를 불러오는 것(예를 들어, 문제에서 주어진 list[10]에 접근하려는 시도)은 IndexError를 발생시킬 수 있습니다. 하지만, 단지 리스트에서 아이템의 갯수가 넘어가는 인덱스로부터 슬라이스하는 것은 IndexError라는 결과를 가져오지 않습니다. 그냥 빈 리스트만 반환하게 됩니다.   

__13. Python에서 switch 또는 case문이 있나요? 그렇지 않다면 같은 기능을 하는 대체가 무엇인가요?__   
   
Python은 switch문이 없습니다. 하지만 switch 함수를 작성하여 사용할 수 있습니다.   

__14. Python이 연속되는 숫자를 반복하기 위해서 사용하는 내장 함수는 무엇인가요?__   
   
range()는 반복문을 통해 반복하기 위해 사용되어지는 숫자들의 리스트를 생성합니다.   
```python
for i in range(5):
    print(i)
```   
range() 함수는 파라미터 두 세트가 필요합니다.
- __range(stop)__
  - stop: 0부터 시작하여 생성할 수 있는 정수의 갯수 ex) range(3) == [0,1,2]   
- __range([start], stop[, step])__   
  - start: 연속된 숫자의 시작 값   
  - stop: 연속된 숫자의 상한 값   
  - step: 연속을 발생시키기 위한 증가 요소   
- __주의할 점__   
  - 오직 정수만 가능하다.   
  - 매개변수는 양수 또는 음수가 될 수 있습니다.   
  - range() 함수는 인덱스가 0부터 시작합니다.   

__15. try-except block 내부에서 가능한 문법은 무엇일까요?__   
   
__try-except__ block에서 사용할 수 있는 두 옵션이 있습니다.   
- "else" 절
  - try block에서 예외를 생성하지 않을 때 코드의 일부을 실행시키고 싶을 경우 유용합니다.   
- "finally" 절   
  - 예외가 발생하든 안하든 개의치않고 일부 코드를 실행시키기를 원할 경우 유용합니다.   

__16. Python에서 string은 무엇인가요?__   
   
Python에서 string은 글자와 숫자로 된 연속이며 immutable한 객체입니다. 한번 값을 할당되면 수정을 허락하지 않습니다. Python에서는 join(), replace(), split() 같은 string을 변화시켜주는 함수들을 제공합니다. 하지만 이 중 어느 것도 원래 객체를 변경하지는 않습니다.   

__17. Python에서 slicing은 무엇인가요?__   
   
slicing은 string의 한 부분을 추출하거나 list의 부분을 추출하기 위한 일련의 작업입니다. string(text)는 인덱스가 0부터 시작하고 n번째 글자는 text[n-1]에 담겨있습니다. Python은 인덱스를 뒤바꿀 수 있습니다. 예를 들어, 음수를 가지고 반대 방향으로 만들 수 있습니다. slice()는 또한 slice 객체를 생성하는 생성자 함수를 가지고 있습니다. 결과는 range(start,stop,step)에 의해 언급되어진 지시의 집합입니다. slice() 함수는 3개의 매개변수를 허용합니다.   
1. start - slicing을 시작할 시작 숫자   
2. stop - slicing의 끝을 나타내는 숫자   
3. step - 인덱스가 증가하는 값 (default = 1)   

__18. Python에서 %s는 무엇인가요?__   
   
Python은 어떠한 값이든 string으로 formatting 하는것을 지원합니다. 다소 복잡한 표현이 있을 수도 있습니다.   
   
흔한 관행 중 하나는 값들을 %s format specifier를 가지고 string으로 만드는 것입니다. Python에서 formatting 작업은 C 함수 printf()가 가진 것처럼 유사한 syntax를 가지고 있습니다.   

__19. Python에서 string은 immutable or mutable 인가요?__   

string은 immutable합니다.   
   
예를 들어 봅시다. "str" 변수가 string 값을 가지고 있는 있을 경우 변수를 담고 있는 컨테이너를 변화시킬 수 없습니다. 예를 들어, 변수의 값을 의미하고 있는 string이 가지는 값만 수정할 수 있습니다.   

__20. Python에서 index는 무엇인가요?__   
   
index는 string 또는 정렬된 list에서 위치를 나타내는 정수 데이터형입니다.   
   
Python에서, string은 문자 리스트입니다. 0 ~ 길이 - 1 까지인 index를 사용하여 string에 접근할 수 있습니다.   

예시로, string "Program" 에서 index는 이런식으로 생길 수 있습니다:   
```python
Program 0 1 2 3 4 5
```   

__21. Python에서 Docstring은 무엇인가요?___   
   
docstring은 아래의 나오는 Python constructs에서 첫 서술이 되는 유일한 텍스트입니다.   
   
Module, Function, Class, or Method definition.   
   
docstring은 string객체의 속성__doc__ 을 추가함으로써 얻을 수 있습니다.   
   
__22. Python programming에서 함수는 무엇인가요?__   
   
함수는 재사용가능한 개체이며 코드 블럭을 나타내는 객체입니다. 코드 재사용성을 높이고 프로그램에 모듈화를 가져옵니다.   
   
Python은 print()와 같은 많은 내장 함수를 제공하고 사용자 정의 함수를 생성할 수 있는 능력을 제공합니다.   

__23. Python에서 얼마 만큼의 기본형 함수들이 이용 가능한가요?__   
   
Python은 두 가지 기본형 함수를 제공합니다.   
   
1. 내장 함수   
2. 사용자 정의 함수   
   
내장 함수는 Python언어의 부분으로 볼수 있습니다. print(), dir(), len() 그리고 abs() 등이 있습니다.   

__24. Python에서 어떻게 함수를 작성하나요?__   
   
아래의 방식으로 함수를 만들 수 있습니다.   

1단계 - 함수를 작성하기 위해서, 단어 def를 작성한 후 함수 이름을 붙여줍니다.   
2단계 - 매개변수를 작성하고 괄호를 사용하여 에워쌉니다. 마지막에 :을 붙여줍니다.   
3단계 - 엔터를 누른 후, 실행에 필요한 Python코드를 작성해줍니다.   
```python
def seongbeen(age,nationality):
    age = 100
    nationality = None
```   

__25. Python에서 함수 호출 또는 호출가능한 객체는 무엇인가요?__   
   
Python에서 함수는 호출가능한 객체로 다뤄집니다. 인자들을 허용하고 튜플 형식으로 다수 값 또는 단일 값을 반환합니다. 이외에도, Python은 같은 범주에서 설치하는 클래스 인스턴스 또는 클래스 같은 다른 구성도 가지고 있습니다.   

__26. Python에서 사용되는 단어 return은 무엇인가요?__   
   
함수의 목적은 입력을 받고 결과를 반환하는 겁니다.   
   
return은 호출하는 곳에 값을 다시 보내기 위한 함수에서 사용하는 Python 표현법입니다.   

__27. Python에서 "Call by value"는 무엇인가요?__   
   
call-by-valud에서 하나의 표현이나 값인 인자는 함수 안에서 각각의 변수로 만들어집니다.   
   
Python은 이러한 변수를 function-level scope내의 지역변수로 간주합니다. 이러한 변수에 대한 어떠한 변화도 함수 외부에 반영되지 않고 함수 내에서만 남아있게 됩니다.   

__28. Python에서 "Call by Reference"는 무엇인가요?__   
   
“call-by-reference”와 “pass-by-reference”를 교대해서 사용할 수 있습니다. 참조에 의해서 인자를 전달할 경우, 단순 복사보다 함수에 내포된 참조로서 이용할 수 있습니다. 이러한 경우에, 인자에 대한 모든 수정을 호출자가 볼 수 있습니다.   
   
이러한 설계는 지역 복사를 해야하는 필요성을 없애기때문에 더 많은 시간, 공간 효율성을 가져오는 장점을 가지고 있습니다.   
   
반면에, 단점은 함수 호출동안 뜻하지 않게 변수가 수정되어질 수 있다는 것입니다. 그러므로, 프로그래머는 이러한 불안정성을 피하기 위한 코드를 작성해야 할 필요가 있습니다.   

__29. trunc() 함수의 반환 값은 무엇인가요?__   
   
trunc() 함수는 출력 결과로 정수 값을 제공하고 특정 표현식으로부터의 소수 값을 제거하는 수학적인 동작을 수행합니다.   

__30. Python 함수는 반드시 값을 반환해야 하나요?__   
   
함수가 값을 꼭 반환할 필요는 없습니다. 그러나, 반환해야만 한다면, None을 반환 값으로 사용할 수 있습니다.   

__31. Python에서 continue가 하는 일은 무엇인가요?__   
   
continue는 실행되지 않은 부분에서 모든 명령어들을 유지하면서 loop문 안에서 다음 반복을 수행할 수 있게 통제하는 파이썬의 jump statement입니다.   
   
continue문은 "while" 과 "for"문에 적용할 수 있습니다.

__32. Python에서 id() 함수의 목적은 무엇인가요?__   
   
id()는 Python 내장 함수 중 하나입니다.   
```python
Signature: id(object)
```   
하나의 매개변수를 허용하고 입력 객체와 연관된 유일한 식별자를 반환합니다.   

__33. Python에서 *args는 무슨 일을 하나요?__   
   
*args를 함수 헤더에서 매개변수로 사용할 수 있습니다. n개의 인자를 전달할 수 있는 능력입니다.   
   
이러한 인자체계는 함수에 이름을 가진 인자를 전달하는것을 허락하지 않습니다.   
   
*args 사용의 예:
```python
# Python code to demonstrate 
# *args for dynamic arguments 
def fn(*argList):  
    for argx in argList:  
        print (argx) 
    
fn('I', 'am', 'Learning', 'Python')
```   
출력 결과:
```python
I
am
Learning
Python
```   

__34. Python에서 **kwargs는 무슨 일을 하나요?__   
   
함수 선언에서 **kwargs를 사용할 수 있습니다. 키워드나 이름을 가진 n개의 인자를 전달할 수 있습니다.   
**kwargs 사용의 예:
```python
# Python code to demonstrate 
# **kwargs for dynamic + named arguments 
def fn(**kwargs):  
    for emp, age in kwargs.items(): 
        print ("%s's age is %s." %(emp, age)) 
    
fn(John=25, Kalley=22, Tom=32)
```   
출력 결과:
```python
John's age is 25.
Kalley's age is 22.
Tom's age is 32.
```   

__35. Python은 main()를 가지고 있나요?__   
   
main()은 대부분의 프로그래밍 언어에서 첫번째로 호출되는 진입점 함수입니다.   
   
Python은 인터프리터 기반이기때문에, 코드를 한줄씩 연속적으로 실행시킵니다.   
   
Python은 main() 함수를 가집니다. 그러나 Python script를 직접적으로 클릭하거나 명령어 라인에서 시킬때마다 실행되어집니다.   
   
Python default main()함수를 오버라이드 할 수도 있습니다. 아래의 코드를 봐주세요.   
```python
print("Welcome")
print("__name__ contains: ", __name__)
def main():
    print("Testing the main function")
if __name__ == '__main__':
    main()
```   
출력 결과:   
```python
Welcome
__name__ contains:  __main__
Testing the main function
```   

__36. Python에서 __ name __ 은 무엇을 하나요?__   
   
__ name __ 은 유일한 변수입니다. Python은 main() 함수를 드러내지 않기 때문에, 인터프리터가 스크립트를 실행할 때 먼저 level 0 indentation에 있는 코드를 실행합니다.   
   
main()이 호출되는지 보기 위해서, " __ main __ " 과 비교하는 절에서 __ name __ 을 사용합니다.   

__37. Python에서 "end"의 목적은 무엇인가요?__   
   
Python의 print() 함수는 항상 끝에 새 줄을 출력합니다. print() 함수는 'end'로 알려진 옵션 매개변수를 허용합니다. end의 값은 '\n'로 자동적으로 설정되어 있습니다. print문안에 있는 end 문자를 원하는 값으로 변경할 수 있습니다.   
```python
# Example: Print a  instead of the new line in the end.
print("Let's learn" , end = ' ')  
print("Python") 

# Printing a dot in the end.
print("Learn to code from techbeamers" , end = '.')  
print("com", end = ' ')
```   
출력 결과:   
```python
Let's learn Python
Learn to code from techbeamers.com
```   

__38. Python에서 언제 "break"를 사용하나요?__   
   
Python은 loop로부터 나오기 위한 break문을 제공합니다. 코드에서 break가 될때마다, 즉시 loop로부터 나오게 됩니다.   
   
중첩 loop문에서 break는 내부 loop문에서 나오게 됩니다.   

__39. Python에서 continue와 pass 사이의 차이점은 무엇인가요?__   
   
continue문은 loop가 다음 반복을 할 수 있게 합니다.   
   
반면에, pass문은 아무것도 하지 않고, 평소처럼 나머지 코드가 실행됩니다.   
   
__40. Python에서 len() 함수는 무엇을 하나요?__   
   
Python에서, len()은 중요한 string 함수입니다. 입력 string의 길이를 보여줍니다.   
```python
>>> some_string = 'techbeamers'
>>> len(some_string)
11
```   

__41. Python에서 chr() 함수는 무엇을 하나요?__   
   
chr()함수는 3.0 버전에서 제거되었다 Python 3.2에서 재추가 되었습니다.   
   
Unicode code point가 정수인 문자를 나타내는 string을 반환합니다.
   
예를 들어, chr(122)은 string 'z'를 반환하고 chr(1212)는 string ‘Ҽ’를 반환합니다.

__42. Python에서 ord() 함수는 무엇을 하나요?__   
   
ord(char)은 1 크기의 string을 가지고 Unicode type 객체의 경우 Unicode code 형식 문자를 나타내는 정수를 반환하고 8-bit string type의 경우 byte 값을 반환합니다.   
```python
>>> ord("z")
122
```   

__43. Python에서 rstrip()은 무엇인가요?__   
   
Python은 끝에 여백 문자를 제외한 string을 복사하는 rstrip() 함수를 제공합니다.   
   
rstrip()은 인자 값을 기반한 문자를 오른쪽 끝에서 제외합니다. 예시로, 문자 그룹에 언급된 string은 제외됩니다.   
   
rstrip의 선언:
```python
str.rstrip([char sequence/pre>
```   
```python
#Example
test_str = 'Programming    '
# The trailing whitespaces are excluded
print(test_str.rstrip())
Programming
```   

__44. Python에서 여백은 무엇인가요?__   
   
여백은 간격과 분리를 위해서 사용하는 문자입니다.   
   
Python에는 tab과 space가 있습니다.   
   
__45. Python에서 isalpha()는 무엇인가요?__   
   
내장 함수 isalpha()는 string을 다루는 함수입니다.   
   
string에 있는 모든 문자가 alphabet type이면 True, 아니면 False를 반환합니다.   

__46. Pyhton에서 split()를 어떻게 사용하나요?__   
   
split() 함수는 string에서 큰 조각을 더 작은 덩어리 또는 sub-strings으로 자르기 위한 함수입니다. 분리 기준 문자를 명시하여 쪼개거나 자동적으로 설정된 space를 사용하여 쪼갤 수 있습니다.   
```python
#Example
str = 'pdf csv json'
print(str.split(" "))
print(str.split())
```   
출력 결과:
```python
['pdf', 'csv', 'json']
['pdf', 'csv', 'json']
```   

__47. Python에서 join 함수는 무엇을 하나요?__   
   
join()은 string, list, tuple에서 가능하며 값을 합치고 통합된 값을 반환합니다.   

__48. Python에서 title() 함수는 무엇을 하나요?__   
   
title()은 각 단어에서 첫번째 문자를 대문자로 나머지 문자들을 소문자로 변환하는 함수입니다.   
```python
#Example
str = 'lEaRn pYtHoN'
print(str.title())
```   
출력 결과:
```python
Learn Python
```   
__49. CPython의 어느 것이 Python과 다르게 만드나요?__   
   
CPython은 중심부가 C로 개발되었습니다. Python-ish 코드를 C 언어로 번역시키기위해 사용되는 인터프리터 loop를 실행시킵니다.   

__50. 어느 package가 가장 빠른 Python 형태일까요?__   
   
PyPy는 성능을 향상시키기 위해 CPython 수행을 이용하면서 최대 호환성을 제공한다.   
   
PyPy가 CPython보다 거의 5배 빠르다.   

__51. Python언어에서 GIL은 무엇인가요?__   
   
Python은 동시에 여러 파이썬 코드(bytecode)를 실행할 때에 여러 스레드를 사용할 경우, 다수의 스레드를 동기화하여 단 하나의 thread만이 Python object에 안전한 접근을 하게하는 mutex인 GIL(the global interpreter lock)을 지원합니다.

__52. 어떻게 Python 스레드는 안전한가요?__   
   
Python은 스레드에게 안전한 접근을 보장합니다. 동기화를 하기 위해 GIL mutex를 사용합니다. 스레드가 언제든지 GIL lock을 잃을 수 있다면, 반드시 thread-safe한 코드를 작성해야 합니다.   

__53. Python 어떻게 메모리를 관리하나요?__   
   
Python은 내부적으로 각 모든 객체와 데이터 구조를 가지는 heap manager를 이용합니다.   
   
이러한 heap manager는 객체에 대한 heap 공간의 할당과 해제를 담당합니다.   

__54. Python에서 tuple은 무엇인가요?__   
   
tuple은 immutable한 모음 데이터형입니다.   
   
list의 연속성과 비슷한 점을 가지고 있습니다. 그러나 tuple과 list의 다른점은 tuple은 변경이 불가하지만 list는 변경이 가능합니다.   
   
또한, tuple은 소괄호()로 둘러싸지만 list는 대괄호[]로 둘러쌉니다.   

__55. dictionary는 무엇인가요?__   
   
dictionary는 객체들의 모음을 저장한 Python에서 연관배열로 알려진 자료구조입니다.   
   
모음은 하나의 연관된 값을 가진 키들의 집합입니다. 이것을 hash, map, 또는 hashmap이라 부를 수 있습니다.   
   
__56. Python에서 set 객체를 무엇인가요?__   
   
set은 비정렬된 모음 객체입니다. 유일하고 immutable한 객체를 저장합니다.   

__57. Python에서 어떻게 dictionary를 사용하나요?__   
   
dictionary는 다른 객체(values)들의 그룹에 대응하는 객체(keys)들의 그룹을 가지고 있습니다. dictionary는 유일한 keys와 values가 대응된 것을 나타냅니다.   
   
mutable하지만 보통 변경하지 않습니다. keys와 연관된 values는 어떠한 Python 자료형도 될 수 있습니다.   

__58. Python list는 linked list인가요?__   
   
Python list는 C-style linked list와 다르게 길이가 변경 가능한 배열입니다.   
   
내부적으로, 다른 객체를 참조하기 위한 인접배열을 가지고 있으며 list head 구조에서 배열 값과 길이를 가르키는 포인터를 가지고 있습니다.   
   
__59. Python에서 class는 무엇인가요?__   
   
Python은 객체지향프로그래밍을 지원하고 거의 모든 OOP 특징을 제공합니다.   
   
Python class는 객체들을 생성하기 위한 설계도입니다. 멤버변수을 정의하고 관련된 행동을 얻습니다.   
   
키워드 "class"를 사용하여 만들 수 있습니다. 객체는 생성자로부터 만들어집니다. 이러한 객체는 클래스의 instance를 의미합니다.   
   
__60. Python class에서 Attributes과 Methods는 무엇인가요?__   
   
class는 정의된 기능들이 하나도 없다면 쓸모가 없습니다. 속성들을 추가함으로써 쓸모있게 만들 수 있습니다. 속성은 데이터와 함수를 담는 컨테이너의 역할을 합니다. class 내부에 직접적으로 명시하여 속성들을 추가할 수 있습니다.   
```python
>>> class Human:
...     profession = "programmer" # specify the attribute 'profession' of the class
>>> man = Human()
>>> print(man.profession)
programmer
```   
속성들이 추가된 후에, 함수를 정의할 수 있습니다. 일반적으로, 함수를 methods로 부를 수 있습니다. methods 선언에서, 반드시 키워드 "self"를 첫번째 인자로 두어야합니다.   
```python
>>> class Human:
    profession = "programmer"
    def set_profession(self, new_profession):
        self.profession = new_profession      
>>> man = Human()
>>> man.set_profession("Manager")
>>> print(man.profession)
Manager
```   
__61. class attributes의 값들이 런타임에 어떻게 할당되나요?__   
   
런타임에 속성들에 대한 값들을 지정할 수 있습니다. init method를 추가하고 input을 객체 생성자에게 전달해야합니다. 이것을 설명하는 예를 봅시다.   
```python
>>> class Human:
    def __init__(self, profession):
        self.profession = profession
    def set_profession(self, new_profession):
        self.profession = new_profession

>>> man = Human("Manager")
>>> print(man.profession)
Manager
```   

__62. Inhertance는 무엇인가요?__   
   
__[코딩 도장](https://dojang.io/mod/page/view.php?id=2396) 추가 설명__ - 클래스 상속은 물려받은 기능을 유지한채로 다른 기능을 추가할 때 사용합니다. 기능을 물려주는 클래스를 기반 클래스, 상속을 받아 새롭게 만드는 클래스를 파생 클래스라고 합니다.   
   
상속은 클래스를 만들 때 ( )(괄호)를 붙이고 괄호 안에 기반 클래스 이름을 넣어줍니다.   
```python
class 기반클래스이름:
    코드
 
class 파생클래스이름(기반클래스이름):    # 기반 클래스를 상속받음
    코드
```   
기반 클래스의 속성에 접근하거나 메서드를 호출할 때는 super() 뒤에 .을 붙여서 사용합니다. 또는, super(파생클래스, self) 형식으로 사용할 수도 있습니다.   
```python
class 기반클래스이름:
    def __init__(self):
        self.속성 = 값
 
class 파생클래스이름(기반클래스이름):
    def __init__(self):
        super().__init__()              # super()로 기반 클래스의 메서드 호출
        super().속성                    # super()로 기반 클래스의 속성에 접근
        super(파생클래스, self).속성    # super에 파생 클래스와 self를 넣는 형식
```   
__다중 상속__   
   
다중 상속은 여러 기반 클래스로부터 상속을 받아서 파생 클래스를 만드는 방법입니다. 클래스를 만들 때 ( )(괄호) 안에 클래스 이름을 ,(콤마)로 구분해서 넣어줍니다.   
```python
class 기반클래스이름1:
    코드
 
class 기반클래스이름2:
    코드
 
class 파생클래스이름(기반클래스이름1, 기반클래스이름2):    # 다중 상속 사용하기
    코드
```   

본문 - 상속은 파생 class가 기반 class의 특성에 대한 접근을 하게 하는 OOP 메카니즘입니다. 기반 class의 기능들을 파생 class로 이월합니다.   
   
공통 코드는 기반 class가 가지고 있고 파생 class 객체는 상속을 통해 해당 코드에 대한 접근을 할 수 있습니다. 아래의 예를 확인해보죠.   
```python
class PC: # Base class
    processor = "Xeon" # Common attribute
    def set_processor(self, new_processor):
        processor = new_processor

class Desktop(PC): # Derived class
    os = "Mac OS High Sierra" # Personalized attribute
    ram = "32 GB"

class Laptop(PC): # Derived class
    os = "Windows 10 Pro 64" # Personalized attribute
    ram = "16 GB"

desk = Desktop()
print(desk.processor, desk.os, desk.ram)

lap = Laptop()
print(lap.processor, lap.os, lap.ram)
```   
출력 결과:   
```python
Xeon Mac OS High Sierra 32 GB
Xeon Windows 10 Pro 64 16 GB
```   

__63. composition은 무엇인가요?__   
   
composition은 상속의 종류입니다. base class로부터 약간 다르게 상속됩니다. 예를 들어, derived class의 멤버로서 동작하는 base class의 instance 변수를 사용함으로써 상속이 됩니다.   
   
composition을 설명하기 위해서, derived class에서 base class를 instance화하고 이러한 instance를 사용해야합니다.   
```python
class PC: # Base class
    processor = "Xeon" # Common attribute
    def __init__(self, processor, ram):
        self.processor = processor
        self.ram = ram

    def set_processor(self, new_processor):
        processor = new_processor

    def get_PC(self):
        return "%s cpu & %s ram" % (self.processor, self.ram)

class Tablet():
    make = "Intel"
    def __init__(self, processor, ram, make):
        self.PC = PC(processor, ram) # Composition
        self.make = make

    def get_Tablet(self):
        return "Tablet with %s CPU & %s ram by %s" % (self.PC.processor, self.PC.ram, self.make)

if __name__ == "__main__":
    tab = Tablet("i7", "16 GB", "Intel")
    print(tab.get_Tablet())
```   
출력 결과:   
```python
Tablet with i7 CPU & 16 GB ram by Intel
```   

__64. error와 exception은 무엇인가요?__   
   
error는 비정상적 종료를 야기하는 코딩 이슈입니다.   
   
반면에, exception은 프로그램의 일반적인 흐름을 중단하는 외부 이벤트의 발생으로 인해 생깁니다.   
   
__65. try/except/finally를 가지고 어떻게 exception을 처리하나요?__   
   
__[코딩 도장](https://dojang.io/mod/page/view.php?id=2425) 추가 설명__ - 예외란 코드 실행 중에 발생한 에러를 뜻합니다. 예외 처리를 하려면 try에 실행할 코드를 넣고 except에 예외가 발생했을 때 처리할 코드를 넣어줍니다. 그리고 else는 예외가 발생하지 않았을 때 코드를 실행하며 finally는 예외 발생 여부와 상관없이 항상 코드를 실행합니다.   
```python
try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    예외 발생 여부와 상관없이 항상 실행할 코드
```   
try의 코드가 에러 없이 잘 실행되면 except의 코드는 실행되지 않으며 try의 코드에서 에러가 발생했을 때만 except의 코드가 실행됩니다.   
   
except에 예외 이름을 지정하면 특정 예외가 발생했을 때만 처리 코드를 실행할 수 있습니다. 그리고 except에서 as 뒤에 변수를 지정하면 발생한 예외의 에러 메시지를 받아옵니다.   
```python
try:
    실행할 코드
except 예외이름:            # 특정 예외가 발생했을 때만 처리 코드를 실행
    예외가 발생했을 때 처리하는 코드
 
try:
    실행할 코드
except 예외이름 as 변수:    # 발생한 예외의 에러 메시지가 변수에 들어감
    예외가 발생했을 때 처리하는 코드
```   

본문 - exception과 같은 에러를 처리하기위해 try,except,finally 구조를 사용합니다. try block 아래에 에러발생 가능성이 있는 코드를 작성합니다. except block에 에러 발생시 작동시킬 코드를 작성합니다. 어떠한 경우에서라도 마지막에 실행되어야만 하는 코드는 finally block에 와야합니다.   
```python
try:
    print("Executing code in the try block")
    print(exception)
except:
    print("Entering in the except block")
finally:
    print("Reached to the final block")
```   
출력 결과:   
```python
Executing code in the try block
Entering in the except block
Reached to the final block
```   

__66. 어떻게 미리 정의된 조건에 대한 exception을 발생시킬까요?__   
   
__[코딩 도장](https://dojang.io/mod/page/view.php?id=2425) 추가 설명__ - 예외를 발생시킬 때는 raise에 Exception을 지정하고 에러 메시지를 넣습니다.   
```python
try:
    raise Exception(에러메시지)    # 예외를 발생시킴
except Exception as e:             # 예외가 발생했을 때 실행됨
    print(e)                       # Exception에 지정한 에러 메시지가 e에 들어감
```   
except 안에서 raise만 사용하면 현재 예외를 다시 상위 코드 블록으로 넘깁니다.   
```python
def 함수A():
    try:
        raise Exception(에러메시지)    # 예외를 발생시킴
    except Exception as e:             # 함수 안에서 예외를 처리함
        raise                          # raise만 사용하면 현재 예외를 다시 상위 코드 블록으로 넘김
 
try:
    함수A()
except Exception as e:                 # 하위 코드 블록에서 예외가 발생해도 실행됨
    print(e)
```   
__예외 만들기__   
   
예외를 만들 때는 Exception을 상속받아서 새로운 클래스를 만들고, __init__ 메서드에서 기반 클래스의 __init__ 메서드를 호출하면서 에러 메시지를 넣어줍니다. 예외를 발생시킬 때는 raise에 새로 만든 예외를 지정해줍니다.   
```python
class 예외이름(Exception):    # 예외 만들기
    def __init__(self):
        super().__init__('에러메시지')
 
raise 예외                    # 예외 발생 시키기
```   

본문 - 조건에 따라 exception을 일으킬 수 있습니다.   
   
예를 들어, 사용자가 홀수만 입력하게 한다면, 짝수 입력 시 exception을 일으킵니다.   
```python
# Example - Raise an exception
while True:
    try:
        value = int(input("Enter an odd number- "))
        if value%2 == 0:
            raise ValueError("Exited due to invalid input!!!")
        else:
            print("Value entered is : %s" % value)
    except ValueError as ex:
        print(ex)
        break
```   
출력 결과:   
```python
Enter an odd number- 2
Exited due to invalid input!!!
```   
```python
Enter an odd number- 1
Value entered is : 1
Enter an odd number-
```   

__67. iterators는 무엇인가요?__   
   
__[코딩 도장](https://dojang.io/mod/page/view.php?id=2425) 추가 설명__ - 클래스에서 __iter__, __next__ 메서드를 구현하면 이터레이터가 됩니다. 또한, 이렇게 만든 이터레이터는 반복 가능한 객체이면서 이터레이터입니다. 이터레이터(제너레이터)는 변수 여러 개에 값을 저장하는 언패킹이 가능합니다.   
```python
class 이터레이터이름:
    def __iter__(self):
        return self
 
    def __next__(self):
        값 생성 코드, 반복을 끝내려면 StopIteration 예외를 발생시킴
 
이터레이터객체 = 이터레이터()    # 이터레이터 객체 생성
이터레이터.__next__()            # 이터레이터에서 값을 차례대로 꺼냄
next(이터레이터)                 # next 함수 사용
 
for i in 이터레이터():    # 이터레이터를 반복문에 사용
    pass
```
클래스에 __getitem__ 메서드를 구현하면 인덱스로 접근할 수 있는 이터레이터가 됩니다. 이때는 __iter__와 __next__ 메서드는 생략해도 됩니다.   
```python
class 이터레이터이름:
    def __getitem__(self, index):
        인덱스에 해당하는 값을 반환하는 코드, 지정된 범위를 벗어났다면 IndexError 예외를 발생시킴
 
이터레이터객체 = 이터레이터()    # 이터레이터 객체 생성
이터레이터객체[인덱스]           # 인덱스로 접근
```

본문 - iterator는 다음 요소로 이동하게 하는 배열같은 객체입니다. for문과 같은 loop에서 사용합니다.   
   
Python library는 iterator의 번호를 가지고 있습니다. 예를 들어, list는 iterator이고 loop문을 통해 사용할 수 있습니다.   

__68. iterable과 iterator사이에 차이점은 무엇인가요?__   
   
__[코딩 도장](https://dojang.io/mod/page/view.php?id=2425) 추가 설명__ - 반복 가능한 객체는 문자열, 리스트, 튜플, range, 딕셔너리, 세트 등이 있습니다. 반복 가능한 객체에서 __iter__ 메서드 또는 iter 함수를 호출하면 이터레이터가 나옵니다. 이터레이터에서 __next__ 메서드 또는 next 함수를 호출하면 반복 가능한 객체의 요소를 차례대로 꺼낼 수 있습니다. 반복 가능한 객체는 요소를 한 번에 하나씩 꺼낼 수 있는 객체이고, 이터레이터는 __next__ 메서드를 사용해서 차례대로 값을 꺼낼 수 있는 객체입니다.      
```python
이터레이터 = 반복가능한객체.__iter__()    # 반복가능한 객체에서 이터레이터를 얻음
이터레이터.__next__()                     # 반복 가능한 객체의 요소를 차례대로  꺼냄
 
이터레이터 = iter(반복가능한객체)         # iter 함수 사용
next(이터레이터)                          # next 함수 사용
```   

본문 - set, list, tuple, dictionary, list 같은 모음 자료형은 모두 iterable한 객체이기도 하지만 iterator를 반환하는 iterable한 container입니다.   
   
__69. generator는 무엇인가요?__   
   
__[코딩 도장](https://dojang.io/mod/page/view.php?id=2425) 추가 설명__ - 제너레이터는 이터레이터를 생성해주는 함수이며 함수 안에서 yield 키워드만 사용하면 됩니다. 제너레이터 함수를 호출하면 제너레이터 객체가 반환되고, 제너레이터 객체에서 __next__ 메서드 또는 next 함수를 호출하면 yield까지 실행한 뒤 yield에 지정한 값이 반환값으로 나옵니다.   
```python
def 제너레이터이름():     # 제너레이터 함수를 만듦
    yield 값              # yield로 값을 발생시킴
 
제너레이터객체 = 제너레이터()    # 제너레이터 객체 생성
제너레이터객체.__next__()        # __next__ 메서드를 호출하면 yield에 지정한 값이 반환값으로 나옴
next(제너레이터)                 # next 함수 사용
 
for i in 제너레이터():           # 제너레이터를 반복문에 사용
    pass
```   
yield는 값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보합니다.   
   
yield from을 사용하면 값을 여러 번 바깥으로 전달합니다.   
```python
yield from 반복가능한객체
yield from 이터레이터
yield from 제너레이터객체
```   
__제너레이터 표현식__   
   
리스트 표현식을 [ ](대괄호) 대신 ( )(괄호)로 묶으면 제너레이터 표현식이 됩니다.   
```python
(식 for 변수 in 반복가능한객체)
(i for i in range(100))
```   

본문 - generator는 iterator와 같이 동작하는 함수를 선언할 수 있게 해주는 기능이며 for문에서 사용될 수 있습니다.   
```python
# Simple Python function
def fn():
    return "Simple Python function."

# Python Generator function
def generate():
    yield "Python Generator function."

print(next(generate()))
```   
출력 결과:   
```python
Python Generator function.
```   

__70. closures은 무엇인가요?__   
   
__[코딩 도장](https://dojang.io/mod/page/view.php?id=2370) 추가 설명__ - 클로저는 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가 함수를 호출할 때 다시 꺼내서 사용하는 함수를 뜻합니다. 따라서 클로저는 지역 변수와 코드를 묶어서 사용하고 싶을 때 활용합니다. 또한, 클로저에 속한 지역 변수는 바깥에서 직접 접근할 수 없으므로 데이터를 숨기고 싶을 때 활용합니다.   
```python
def calc():    # calc 함수 안에 mul_add 함수를 만듦
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환
 
c = calc()    # c에 저장된 함수가 클로저
print(c(1), c(2), c(3), c(4), c(5))    # 8 11 14 17 20
```   
클로저는 람다 표현식으로도 만들 수 있습니다.   
```python
def calc():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환
```   

본문 - closures는 다른 함수에 의해 반환된 함수 객체입니다. 코드 중복을 제거하기 위해 사용합니다.   
   
아래의 예에서, 숫자들을 곱하기 위한 간단한 closure를 작성했습니다.   
```python
def multiply_number(num):
    def product(number):
        'product() here is a closure'
        return num * number
    return product

num_2 = multiply_number(2)
print(num_2(11))
print(num_2(24))

num_6 = multiply_number(6)
print(num_6(1))
```   
출력 결과:   
```python
22
48
6
```   

__71. Decorator는 무엇인가요?__   
   
__[코딩 도장](https://dojang.io/mod/page/view.php?id=2454) 추가 설명__ - 데코레이터는 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용합니다.   
데코레이터는 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용합니다. 먼저 데코레이터는 호출할 함수를 매개변수로 받고, 호출할 함수를 감싸는 함수 wrapper를 만듭니다. 그리고 wrapper 함수 안에서는 매개변수로 받은 func를 호출하고, 함수 바깥에서는 return을 사용하여 wrapper 함수 자체를 반환합니다. 데코레이터를 사용할 때는 호출할 함수 위에 @데코레이터를 형식으로 지정해줍니다.   
```python
def 데코레이터이름(func):    # 데코레이터는 호출할 함수를 매개변수로 받음
    def wrapper():           # 호출할 함수를 감싸는 함수
        func()               # 매개변수로 받은 함수를 호출
    return wrapper           # wrapper 함수 반환
 
@데코레이터                  # 데코레이터 지정
def 함수이름():
    코드
```
__함수의 매개변수와 반환값을 처리하는 데코레이터__   
   
데코레이터에서 함수의 매개변수와 반환값을 처리할 때는 wrapper 함수의 매개변수를 호출할 함수의 매개변수와 똑같이 지정하고, func에 매개변수를 넣어서 호출하고 반환하면 됩니다.   
```python
def 데코레이터이름(func):                     # 데코레이터는 호출할 함수를 매개변수로 받음
    def wrapper(매개변수1, 매개변수2):        # 호출할 함수의 매개변수와 똑같이 지정
        return func(매개변수1, 매개변수2)     # func에 매개변수를 넣어서 호출하고 반환값을 반환
    return wrapper                            # wrapper 함수 반환
 
@데코레이터                                   # 데코레이터 지정
def 함수이름(매개변수1, 매개변수2):           # 매개변수는 두 개
    코드 
```   
   
__매개변수가 있는 데코레이터__   
   
매개변수가 있는 데코레이터는 값을 지정해서 동작을 바꿀 수 있습니다. 이때는 데코레이터가 사용할 매개변수를 지정하고, 실제 데코레이터 역할을 하는 real_decorator 함수를 만듭니다. 그다음에 real_decorator 함수 안에서 wrapper 함수를 만들어줍니다.   
```python
def 데코레이터이름(매개변수):                    # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):                    # 호출할 함수를 매개변수로 받음
        def wrapper(매개변수1, 매개변수2):       # 호출할 함수의 매개변수와 똑같이 지정
            return func(매개변수1, 매개변수2)    # func를 호출하고 반환값을 반환
        return wrapper                           # wrapper 함수 반환
    return real_decorator                        # real_decorator 함수 반환
 
@데코레이터(인수)                                # 데코레이터를 지정하면서 인수를 넣음
def 함수이름(매개변수1, 매개변수2):
    코드
```   
__클래스로 데코레이터 만들기__   
   
클래스로 데코레이터를 만들 때는 인스턴스를 함수처럼 호출하게 해주는 __call__ 메서드를 구현하고, __call__ 메서드에서 호출할 함수의 매개변수를 처리해줍니다.   
```python
class 데코레이터이름:
    def __init__(self, func):    # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func         # 호출할 함수를 속성 func에 저장
 
    def __call__(self, 매개변수1, 매개변수2):     # __call__에서 호출할 함수의 매개변수 처리
        return self.func(매개변수1, 매개변수2)    # self.func에 매개변수를 넣어서 호출하고
                                                  # 반환값을 반환
@데코레이터                      # 데코레이터 지정
def 함수이름(매개변수1, 매개변수2):
    코드
```   

__매개변수가 있는 클래스 데코레이터 만들기__  
   
__init__ 메서드에서 데코레이터가 사용할 매개변수를 초깃값으로 받고, __call__ 메서드에서 호출할 함수를 매개변수를 받습니다. 그리고 __call__ 함수 안에서 wrapper 함수를 만들고 호출할 함수의 매개변수를 처리해주면 됩니다.   

```python
class 데코레이터이름:
    def __init__(self, 매개변수):    # 데코레이터가 사용할 매개변수를 초깃값으로 받음
        self.속성 = 매개변수         # 매개변수를 속성에 저장
 
    def __call__(self, func):                    # 호출할 함수를 매개변수로 받음
        def wrapper(매개변수1, 매개변수2):       # 호출할 함수의 매개변수 처리
            return func(매개변수1, 매개변수2)    # func를 호출하고 반환값을 반환
        return wrapper                           # wrapper 함수 반환
 
@데코레이터(인수)                    # 데코레이터를 지정하면서 인수를 넣음
def 함수이름(매개변수1, 매개변수2):
    코드
```   

본문 - 주어진 객체에 동적으로 새로운 기능을 추가할 수 있는 능력입니다. 아래의 예에서, 함수의 실행 전과 후의 메세지를 보여주기위한 간단한 예를 작성하였습니다.   

```python
def decorator_sample(func):
    def decorator_hook(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return decorator_hook

@decorator_sample
def product(x, y):
    "Function to multiply two numbers."
    return x * y

print(product(3, 3))
```   
출력 결과:   
```python
Before the function call
After the function call
9
```   


## Reference
* TechBeamers
<https://www.techbeamers.com/python-interview-questions-programmers/>


