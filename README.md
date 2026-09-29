# Python 기초: 텍스트 파일 요약 예제

개인 Python 과정 노트의 **함수, 모듈, 파일 읽기, 예외 처리** 항목을 하나의 실행 가능한 예제로 재구성했습니다. `examples/text_summary.py`는 UTF-8 텍스트의 줄·단어·문자 수를 출력합니다. 이 코드는 노트에 있던 완성 프로그램의 복사본이 아니라, 해당 학습 범위에 맞춰 새로 작성한 예제입니다.

## 실행

Python 3.12.14에서 실행을 확인했습니다. 외부 패키지는 필요하지 않습니다.

```bash
python3 examples/text_summary.py examples/sample.txt
```

예상 출력:

```text
lines: 2
words: 5
characters: 33
```

파일을 찾을 수 없거나 UTF-8로 읽을 수 없으면 오류를 표준 오류로 출력하고 종료 코드 `1`을 반환합니다. 인자가 없거나 두 개 이상이면 사용법을 출력하고 종료 코드 `2`를 반환합니다.

## 계산 기준과 파일

- `lines`: `splitlines()`로 나눈 줄의 수입니다. 마지막 개행 문자만으로 빈 줄을 추가하지 않습니다.
- `words`: 공백으로 분리한 토큰의 수입니다. 한국어 형태소 분석 결과가 아닙니다.
- `characters`: 개행을 포함한 Python 문자열 길이이며, 바이트 수가 아닙니다.
- `examples/text_summary.py`: 인자 검사, 파일 읽기, 계산, 오류 처리를 담은 단일 실행 파일입니다.
- `examples/sample.txt`: 출력값을 재현할 입력 자료입니다.

## 노트의 표현을 현재 문법과 대조

노트의 `long int`와 “Python에는 switch~case가 없다”는 설명을 이 예제의 실행 기준으로 사용하지 않았습니다. Python 3.12에서는 정수에 `int`를 사용하고, `match`/`case` 문이 있습니다. 값 비교 `==`와 객체 동일성 비교 `is`도 다른 연산입니다. 파일 읽기에는 `with open(..., encoding="utf-8")`을 사용해 파일이 닫히도록 했습니다. 관련 기준은 [Python 내장형](https://docs.python.org/3.12/library/stdtypes.html), [match 문](https://docs.python.org/3.12/reference/compound_stmts.html#the-match-statement), [비교 연산](https://docs.python.org/3.12/reference/expressions.html#comparisons), [파일 입출력](https://docs.python.org/3.12/tutorial/inputoutput.html#reading-and-writing-files) 문서에서 확인할 수 있습니다.

이 저장소는 Python 문법 학습 예제이며, 운영 자동화나 기존 프로젝트의 개인 구현 성과를 주장하지 않습니다.
