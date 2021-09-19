#!/usr/bin/env -S python
# -*- coding: utf-8 -*-
import io
import json
import sys

# MSYS2での文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# プレフィックス & サフィックス
build_prefix = 'build_'
remove_prefix = 'remove_'
const_prefix = 'constr_'
olight_suffix = '_olight'

# 素材のデータを読み込む
with open('data/json/furniture_and_terrain/terrain-floors-indoor.json') as f:
    olid = json.load(f)

# id索引の辞書にする
tfi_dict = {
    item['id']: item for item in olid
}

# olightのみ抜き出す
tfi_ol_dict = {
    key: tfi_dict[key] for key in tfi_dict if key.endswith(olight_suffix)
}

# 出力用データ
data = []
cg_build = {
    "type": "construction_group",
    "id": f"{build_prefix}floor{olight_suffix}",
    "name": "天井灯を設置する"
}
data.append(cg_build)
cg_remove = {
    "type": "construction_group",
    "id": f"{remove_prefix}floor{olight_suffix}",
    "name": "天井灯を除去する"
}
data.append(cg_remove)

for olid in tfi_ol_dict:
    # ID処理
    postid = olid
    # リノリウムは例外処理する
    if postid == 't_linoleum_gray_floor_olight':
        preid = 't_linoleum_gray'
    elif postid == 't_linoleum_whitefloor_olight':
        preid = 't_linoleum_white'
    else:
        preid = postid[:-len(olight_suffix)]
    # 設置
    const_build = {
        "type": "construction",
        "id": f"{const_prefix}{postid}",
        "group": cg_build["id"],
        "category": "CONSTRUCT",
        "required_skills": [
            ["fabrication", 4],
            ["electronics", 4]
        ],
        "time": "30 m",
        "tools": [
            [["soldering_iron", 10], ["toolset", 10]]
        ],
        "qualities": [
            [{"id": "HAMMER", "level": 2}],
            [{"id": "SCREW", "level": 1}]
        ],
        "components": [
            [["betavoltaic", 2]],
            [["power_supply", 1]],
            [["cable", 2]],
            [["light_bulb", 1], ["e_scrap", 1]],
            [["plastic_chunk", 1]]
        ],
        "pre_terrain": preid,
        "post_terrain": postid
    }
    data.append(const_build)
    # 除去
    const_remove = {
        "type": "construction",
        "id": f"{const_prefix}{remove_prefix}{postid}",
        "group": cg_remove["id"],
        "category": "CONSTRUCT",
        "required_skills": [
            ["fabrication", 4],
            ["electronics", 4]
        ],
        "time": "30 m",
        "tools": [
            [["soldering_iron", 10], ["toolset", 10]]
        ],
        "qualities": [
            [{"id": "HAMMER", "level": 2}],
            [{"id": "SCREW", "level": 1}]
        ],
        "byproducts": [
            {"item": "betavoltaic", "count": [2, 2]},
            {"item": "power_supply", "count": [1, 1]},
            {"item": "cable", "charges": [2, 2]},
            {"item": "e_scrap", "count": [1, 1]},
            {"item": "plastic_chunk", "count": [1, 1]}
        ],
        "pre_terrain": postid,
        "post_terrain": preid
    }
    data.append(const_remove)


# ダンプ
json_text = json.dumps(data, ensure_ascii=False)
print(json_text)
