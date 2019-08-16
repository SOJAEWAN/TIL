# 1. 문제
# list, str, dict, int, complex, map, range

# 2. 문제
• __init__ : 인스턴스 객체가 생성될 때 자동으로 호출되는 함수
• __del__ : 객체가 소멸되는 과정에서 자동으로 호출되는 함수
• __str__ : 특정 객체를 print() 할때 보이는 값을 정의해주는 메서드
• __repr__ : 그냥 객체 자체를 출력하는 값을 정의해주는 메서드


# 3. 문제
# list
# .sort() : 정렬
# .append() : 리스트 마지막에 요소 추가

# str
# .upper() : 문자열을 모두 대문자로 만들어 반환
# .lower() : 문자열을 모두 소문자로 만들어 반환
# .swapcase() : 대문자 -> 소문자 / 소문자 -> 대문자

# dict
# .get() : key로 value 뽑기
# .update() : 딕셔너리에 key_value 추가(동일한 key라면 value Error)

# set
# .pop() : 임의의 요소를 제거해 반환
# .remove() : set에서 요소를 삭제하고 없으면 에러
# .discard() : set에서 요소를 삭제하고 없어도 에러 x