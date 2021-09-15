#!/usr/bin/env -S python
# -*- coding: utf-8 -*-
import sys
import io
import json
import subprocess


# MSYS2での文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


build_prefix = 'build'
remove_prefix = 'remove'
const_prefix = 'constr'
olight_suffix = 'olight'

#    Pre_Terrain         Post_Terrain                    Name
floors = [
    ['t_thconc_floor',   '{pre}_{olight_suffix}',        'コンクリート'],
    ['t_floor',          '{pre}_{olight_suffix}',        '木'],
    ['t_metal_floor',    '{pre}_{olight_suffix}',        '金属'],
    ['t_strconc_floor',  '{pre}_{olight_suffix}',        '強化コンクリート'],
    ['t_linoleum_gray',  '{pre}_floor_{olight_suffix}',  'リノリウム']
]


data = []
cg_build = {
    "type": "construction_group",
    "id": f"{build_prefix}_floor_{olight_suffix}",
    "name": "天井灯を設置する"
}
data.append(cg_build)
cg_remove = {
    "type": "construction_group",
    "id": f"{remove_prefix}_floor_{olight_suffix}",
    "name": "天井灯を除去する"
}
data.append(cg_remove)

for preid, postid, fname in floors:
    # 前処理
    postid = postid.format(pre=preid, olight_suffix=olight_suffix)
    # 設置
    const_build = {
        "type": "construction",
        "id": f"{const_prefix}_{postid}",
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
            [{ "id": "HAMMER", "level": 2 }],
            [{ "id": "SCREW", "level": 1 }]
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
        "id": f"{const_prefix}_{remove_prefix}_{postid}",
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
            [{ "id": "HAMMER", "level": 2 }],
            [{ "id": "SCREW", "level": 1 }]
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

# 整形
#subprocess.run('tool/json_formatter.exe', input=json_text, encoding='utf-8')
