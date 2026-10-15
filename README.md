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
