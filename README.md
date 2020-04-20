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

__51.

## Reference
* TechBeamers
<https://www.techbeamers.com/python-interview-questions-programmers/>


