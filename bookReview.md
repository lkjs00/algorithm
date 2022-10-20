## 파이썬 알고리즘 인터뷰

- 125 Valid Palindrome

    문자열 s에서 s를 뒤집을 때 : s[::-1]

* 344 Reverse String

    리스트 s에서 s를 뒤집을 때 : s.reverse()

* 937 Reorder Log Files

    람다 표현식 : letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

* 1 Two Sum

    딕셔너리는 해시 테이블로 구현되어 있어서, 조회는 평균적으로 O(1)에 가능하다.

    따라서 리스트를 딕셔너리로 바꿔 조회하면 더욱 빠르다.
