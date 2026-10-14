#!/usr/bin/env python3
"""依副檔名整理資料夾；預設只預覽，不會移動檔案。"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


CATEGORIES = {
    ".jpg": "圖片",
    ".jpeg": "圖片",
    ".png": "圖片",
    ".gif": "圖片",
    ".pdf": "文件",
    ".doc": "文件",
    ".docx": "文件",
    ".txt": "文件",
    ".csv": "試算表",
    ".xlsx": "試算表",
    ".zip": "壓縮檔",
    ".py": "程式碼",
}


def category_for(path: Path) -> str:
    """依副檔名回傳分類；沒有副檔名的檔案歸入「其他」。"""
    return CATEGORIES.get(path.suffix.lower(), "其他")


def available_destination(destination: Path) -> Path:
    """避免覆寫，必要時在檔名後加入序號。"""
    if not destination.exists():
        return destination
    for number in range(1, 10_000):
        candidate = destination.with_name(
            f"{destination.stem}_{number}{destination.suffix}"
        )
        if not candidate.exists():
            return candidate
    raise RuntimeError(f"找不到可用的檔名：{destination.name}")


def plan_moves(folder: Path) -> list[tuple[Path, Path]]:
    """建立移動計畫，只處理來源資料夾第一層的檔案。"""
    if not folder.is_dir():
        raise NotADirectoryError(f"不是資料夾：{folder}")

    moves = []
    for source in sorted(folder.iterdir(), key=lambda item: item.name.lower()):
        if not source.is_file():
            continue
        target_dir = folder / category_for(source)
        target = available_destination(target_dir / source.name)
        moves.append((source, target))
    return moves


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("folder", type=Path, help="要整理的測試資料夾")
    parser.add_argument(
        "--apply", action="store_true", help="確認後實際移動檔案（預設為預覽）"
    )
    args = parser.parse_args()

    try:
        moves = plan_moves(args.folder)
    except (NotADirectoryError, OSError) as error:
        parser.error(str(error))

    if not moves:
        print("沒有需要整理的檔案。")
        return 0

    for source, target in moves:
        print(f"{source.name} -> {target.parent.name}/{target.name}")

    if not args.apply:
        print("預覽模式：未修改任何檔案。若確認無誤，請加上 --apply。")
        return 0

    for source, target in moves:
        target.parent.mkdir(exist_ok=True)
        shutil.move(str(source), str(target))
    print(f"已移動 {len(moves)} 個檔案。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
