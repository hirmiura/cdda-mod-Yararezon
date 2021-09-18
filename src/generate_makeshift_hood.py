#!/usr/bin/env -S python
# -*- coding: utf-8 -*-
import io
import json
import sys

from cdda_gettext import gt

# MSYS2での文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


hood_prefix = 'makeshift_hood'

# フードの素材のIDリスト
compos = [
    'sheet',
    'blanket',
    'down_blanket',
    'fur_blanket',
    'quilt',
    'quilt_patchwork',
]

# 素材のデータを読み込む
with open('data/json/items/generic/bedding.json') as f:
    bedding = json.load(f)

data = []

for bid in compos:
    # 素材データ
    mat = next((b for b in bedding if b['id'] == bid), None)
    name = gt.ngettext(mat['name']['str'], None, 1)  # gettextで和名
    encumbrance = mat['armor'][0]['encumbrance']
    # フード
    hood = {
        "id": f"{hood_prefix}_{bid}",
        "type": "ARMOR",
        "copy-from": bid,
        "name": {"str": f"簡易フード({name})"},
        "description": f"{name}で作った簡易フードです。嵩張りますが暖かいです。",
        "armor": [
            {
                "encumbrance": encumbrance,
                "coverage": 100,
                "covers": ["head", "mouth"]
            }
        ]
    }
    data.append(hood)
    # レシピ
    recipe = {
        "result": f"{hood_prefix}_{bid}",
        "type": "recipe",
        "category": "CC_ARMOR",
        "subcategory": "CSC_ARMOR_HEAD",
        "skill_used": "survival",
        "difficulty": 0,
        "time": "3 m",
        "reversible": True,
        "autolearn": True,
        "components": [
            [[bid, 1]]
        ]
    }
    data.append(recipe)


# ダンプ
json_text = json.dumps(data, ensure_ascii=False)
print(json_text)
