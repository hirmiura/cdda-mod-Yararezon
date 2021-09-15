#!/usr/bin/env -S python
# -*- coding: utf-8 -*-
import sys
import io
import json
import subprocess


# MSYS2での文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


hood_prefix = 'makeshift_hood'

#    BaseID            Name                    Enc
compos = [
    ['sheet',            'シーツ',               15],
    ['blanket',          'ブランケット',         35],
    ['down_blanket',     'ブランケット(羽毛)',   45],
    ['fur_blanket',      'ブランケット(毛皮)',   55],
    ['quilt',            'キルトケット',         40],
    ['quilt_patchwork',  'キルトケット(羊毛)',   50],
]


data = []

for bid, name, enc in compos:
    # フード
    hood = {
        "id": f"{hood_prefix}_{bid}",
        "type": "ARMOR",
        "copy-from": bid,
        "name": { "str": f"簡易フード({name})" },
        "description": f"{name}で作った簡易フードです。嵩張りますが暖かいです。",
        "armor": [
            {
            "encumbrance": enc,
            "coverage": 100,
            "covers": [ "head", "mouth" ]
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
            [ [ bid, 1 ] ]
        ]
    }
    data.append(recipe)


# ダンプ
json_text = json.dumps(data, ensure_ascii=False)
print(json_text)
