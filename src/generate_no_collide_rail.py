#!/usr/bin/env -S python
# -*- coding: utf-8 -*-
import io
import json
import sys

# MSYS2での文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# 除外リスト
except_id_list = [
]

# 地形データを読み込む
with open('data/json/furniture_and_terrain/terrain-railroads.json') as f:
    json_rail = json.load(f)

# レールのリスト
rails = [
    r for r in json_rail if 'flags' in r and 'RAIL' in r['flags']
]

# 除外リストを適用する
for r in rails:
    for ex in except_id_list:
        if r['id'] == ex:
            rails.remove(r)

data = []

for r in rails:
    # 上書きデータ作成
    item = {}
    item['id'] = r['id']
    item['type'] = r['type']
    item['name'] = r['name']
    item['copy-from'] = r['id']
    item['flags'] = r['flags']
    item['flags'].append('NOCOLLIDE')
    data.append(item)

# IDでソートする
data.sort(key=lambda item: item['id'])

# ダンプ
json_text = json.dumps(data, ensure_ascii=False)
print(json_text)
