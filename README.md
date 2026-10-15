# AI Study

개인 AI 학습 기록 저장소. 이론 · 실습 · 직접 시도한 실험을 주제별로 정리합니다.

## 주제 목차
<!-- 아래 표는 `python scripts/new.py index` 로 자동 갱신됩니다 -->
<!-- TOPICS:START -->
| # | 주제 | 이론 | 실습 | 실험 |
|---|---|---|---|---|
| - | (아직 없음) | | | |
<!-- TOPICS:END -->

## 구조
```
ai-study/
├── topics/            # 주제별 학습 (이 안을 직접 채움)
│   └── NN-주제/
│       ├── README.md      # 요약, 로드맵, 실험 목록
│       ├── theory/        # 이론 정리 (md)
│       ├── practice/      # 따라하기 노트북
│       ├── experiments/   # 직접 시도 (날짜_이름/ 단위)
│       └── references.md
├── shared/            # 공용 유틸
├── data/              # 데이터 (git 제외, 출처만 기록)
├── templates/         # 주제/실험 템플릿
└── scripts/new.py     # 주제/실험 생성, 목차 갱신
```

## 사용법
```bash
python scripts/new.py topic "EDA"                       # topics/01-eda 생성
python scripts/new.py exp eda "titanic baseline"        # 실험 폴더 생성 (번호/이름 모두 가능)
python scripts/new.py index                             # 목차 갱신
```

## 초기 설정
```bash
uv sync                      # 환경 설치 (또는 pip install -e .)
uv run nbstripout --install  # 노트북 출력 자동 제거 (커밋 전 필터)
```

## 규칙
- **theory**: 거의 안 바뀌는 지식 / **practice**: 정답이 있는 따라하기 / **experiments**: 내가 가설을 세워 해본 것
- 실험은 성공/실패 상관없이 README에 기록
- 커밋 메시지: `[eda] titanic 결측치 처리 실험 추가`
- 큰 데이터·모델은 올리지 않고 `data/README.md` 에 출처만 기록

- 이론: topics/01-eda/theory/01-basics.md처럼 번호를 붙인 마크다운 파일
- 따라하기: topics/01-eda/practice/01-pandas-profiling.ipynb처럼 강의나 책을 따라 한 노트북
- 참고 자료: topics/01-eda/references.md에 링크 정리

## 실험 기록
: 새로운 데이터나 방법으로 시도할 때마다 실험 폴더를 만듭니다.

```bash
python scripts/new.py exp eda "titanic baseline"
```
topics/01-eda/experiments/2026-10-15_titanic-baseline/ 폴더가 생깁니다. 그 안에서 다음을 하세요.

1. notebook.ipynb를 직접 만들어 작업합니다. 아래 코드를 첫 셀에 넣으면 공용 유틸과 데이터 경로를 쓸 수 있습니다.
```python
import sys; sys.path.append("../../../..")   # 저장소 루트까지 올라가는 경로
from shared.utils import DATA_DIR, set_seed
set_seed(42)
```
2. 그래프 이미지는 figures/에 저장합니다.
3. 작업이 끝나면 README.md의 목적, 방법, 결과, 배운 점을 채웁니다. 실패한 실험도 꼭 기록하세요.
4. 주제 README의 "실험 목록" 표에 한 줄을 추가합니다.

같은 주제에 다른 데이터로 또 시도하고 싶으면 7단계를 반복하면 됩니다. 날짜가 붙은 폴더가 병렬로 쌓입니다.

## 데이터
데이터 파일은 data/ 폴더에 넣어 쓰되, git에는 올라가지 않습니다. 대신 data/README.md 표에 출처와 다운로드 방법을 한 줄 적어 두세요. 나중에 다른 컴퓨터에서 같은 데이터를 다시 받을 수 있습니다.
