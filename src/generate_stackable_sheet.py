#!/usr/bin/env -S python
# -*- coding: utf-8 -*-
import io
import json
import sys

# MSYS2での文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# 除外リスト
except_id_list = [
    'sheet_kevlar_layered',  # セーブファイル読み込み時にクラッシュする
]

# 生地のデータを読み込む
with open('data/json/items/resources/tailoring.json') as f:
    tailoring = json.load(f)

# 生地のリスト
sheets = [
    t for t in tailoring if t['id'].startswith('sheet_')
]

# 除外リストを適用する
for s in sheets:
    for ex in except_id_list:
        if s['id'] == ex:
            sheets.remove(s)

data = []

for s in sheets:
    # 上書きデータ作成
    item = {}
    item['id'] = s['id']
    item['type'] = s['type']
    item['name'] = s['name']
    item['copy-from'] = s['id']
    item['stackable'] = True
    data.append(item)

# IDでソートする
data.sort(key=lambda item: item['id'])

# ダンプ
json_text = json.dumps(data, ensure_ascii=False)
print(json_text)
