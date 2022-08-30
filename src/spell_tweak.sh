#!/usr/bin/bash

target_path=.

if [ $# -ge 1 ]; then
    target_path=$1
fi

# type が SPELL で
# difficulty が設定されていて
# valid_targets の項目数が 1 で、且つ hostile である項目に
# valid_targets に ground を追加するMODを生成する
find $target_path -name '*.json' -exec jq -c '.[] | select(.type != null) | select(.type == "SPELL")' {} + \
    | jq 'select(.difficulty != null)' \
    | jq 'select(.valid_targets != null) | select(.valid_targets | length == 1 and .[0] == "hostile")' \
    | jq '{id: .id, type: .type, name: .name, "copy-from": .id, extend: { valid_targets: [ "ground" ] }}' \
    | jq -s
