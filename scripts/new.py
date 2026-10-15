#!/usr/bin/env python3
"""학습 저장소 보조 스크립트.

  python scripts/new.py topic "Linear Regression"        # 새 주제 (번호 자동)
  python scripts/new.py exp eda "house price outlier"    # 주제 안에 새 실험
  python scripts/new.py index                            # 루트 README 목차 갱신
"""
import argparse
import re
import shutil
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOPICS = ROOT / "topics"
TEMPLATES = ROOT / "templates"
START, END = "<!-- TOPICS:START -->", "<!-- TOPICS:END -->"


def slugify(s: str) -> str:
    s = re.sub(r"[^\w\s-]", "", s.strip().lower(), flags=re.UNICODE)
    return re.sub(r"[\s_]+", "-", s)


def topic_dirs():
    return sorted(p for p in TOPICS.iterdir() if p.is_dir())


def next_number() -> int:
    nums = [int(m.group(1)) for p in topic_dirs() if (m := re.match(r"(\d+)-", p.name))]
    return max(nums, default=0) + 1


def find_topic(key: str) -> Path:
    key = key.strip("/").split("/")[-1]
    for p in topic_dirs():
        bare = p.name.split("-", 1)[-1]
        if key in (p.name, bare) or (key.isdigit() and p.name.startswith(f"{int(key):02d}-")):
            return p
    sys.exit(f"주제를 찾을 수 없음: {key}  (있는 주제: {[p.name for p in topic_dirs()]})")


def render(text: str, **kw) -> str:
    for k, v in kw.items():
        text = text.replace("{{" + k + "}}", v)
    return text


def cmd_topic(args):
    name = f"{next_number():02d}-{slugify(args.name)}"
    dest = TOPICS / name
    if dest.exists():
        sys.exit(f"이미 존재: {dest}")
    shutil.copytree(TEMPLATES / "topic", dest)
    readme = dest / "README.md"
    readme.write_text(render(readme.read_text(encoding="utf-8"),
                             TITLE=args.name, DATE=str(date.today())), encoding="utf-8")
    print(f"생성: topics/{name}")
    cmd_index(args)


def cmd_exp(args):
    topic = find_topic(args.topic)
    dest = topic / "experiments" / f"{date.today()}_{slugify(args.name)}"
    if dest.exists():
        sys.exit(f"이미 존재: {dest}")
    (dest / "figures").mkdir(parents=True)
    (dest / "figures" / ".gitkeep").touch()
    tpl = (TEMPLATES / "experiment.md").read_text(encoding="utf-8")
    (dest / "README.md").write_text(
        render(tpl, TITLE=args.name, DATE=str(date.today()), TOPIC=topic.name), encoding="utf-8")
    print(f"생성: {dest.relative_to(ROOT)}  (notebook.ipynb 는 직접 추가하세요)")
    cmd_index(args)


def topic_title(p: Path) -> str:
    r = p / "README.md"
    if r.exists():
        for line in r.read_text(encoding="utf-8").splitlines():
            if line.startswith("# "):
                return line[2:].strip()
    return p.name


def count(p: Path, sub: str) -> int:
    d = p / sub
    return sum(1 for x in d.iterdir() if not x.name.startswith(".")) if d.exists() else 0


def cmd_index(_args=None):
    readme = ROOT / "README.md"
    rows = ["| # | 주제 | 이론 | 실습 | 실험 |", "|---|---|---|---|---|"]
    for p in topic_dirs():
        rows.append(f"| {p.name.split('-')[0]} | [{topic_title(p)}](topics/{p.name}/) "
                    f"| {count(p, 'theory')} | {count(p, 'practice')} | {count(p, 'experiments')} |")
    if len(rows) == 2:
        rows.append("| - | (아직 없음) | | | |")
    block = f"{START}\n" + "\n".join(rows) + f"\n{END}"
    text = readme.read_text(encoding="utf-8")
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    readme.write_text(new, encoding="utf-8")
    print("README 목차 갱신 완료")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("topic"); t.add_argument("name"); t.set_defaults(fn=cmd_topic)
    e = sub.add_parser("exp"); e.add_argument("topic"); e.add_argument("name"); e.set_defaults(fn=cmd_exp)
    i = sub.add_parser("index"); i.set_defaults(fn=cmd_index)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
