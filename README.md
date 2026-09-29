# Python 기초: 텍스트 파일 요약 예제

Python의 함수, 모듈, 파일 읽기와 예외 처리를 하나의 실행 가능한 예제로 보여줍니다. `examples/text_summary.py`는 UTF-8 텍스트의 줄·단어·문자 수를 출력합니다.

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

## 구현 기준

파일은 `with open(..., encoding="utf-8")`으로 읽고, 읽기 오류와 사용법 오류는 서로 다른 종료 코드로 구분합니다. 자세한 입출력 동작은 [Python 파일 입출력 문서](https://docs.python.org/3.12/tutorial/inputoutput.html#reading-and-writing-files)를 참고합니다. 이 예제는 텍스트 통계의 정의와 오류 처리를 보여주며 운영 자동화 기능은 포함하지 않습니다.
