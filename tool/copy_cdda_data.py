#!/usr/bin/env -S python
# -*- coding: utf-8 -*-
import io
import sys
from pathlib import Path
from shutil import copyfile

# MSYS2での文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 基準ディレクトリ
src_base = '../../CataclysmDDA-dev'
dst_base = './'

# コピー対象のファイルリスト
file_list = [
    'lang/mo/ja/LC_MESSAGES/cataclysm-dda.mo',
    'data/json/items/generic/bedding.json',
    'data/json/furniture_and_terrain/terrain-floors-indoor.json',
]

# ファイルをコピーする
for file in file_list:
    src = Path(src_base, file)
    dst = Path(dst_base, file)
    dst.parent.mkdir(parents=True, exist_ok=True)
    copyfile(src, dst)
    print(dst)
