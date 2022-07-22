# Makefile
CDDA_JSON_FORMATTER:=tool/json_formatter.exe

.PHONY: all copy-data generate format lint format-mod format-preset


all: copy-data generate format


# cdda本体からデータをコピー
copy-data:
	tool/copy_cdda_data.py


# JSON生成
generate: yararezon_mod/const_floor_olight.json yararezon_mod/makeshift_hood.json yararezon_mod/stackable_sheet.json

yararezon_mod/const_floor_olight.json:
	src/generate_floor_olight.py | $(CDDA_JSON_FORMATTER) > $@

yararezon_mod/makeshift_hood.json:
	src/generate_makeshift_hood.py | $(CDDA_JSON_FORMATTER) > $@

yararezon_mod/stackable_sheet.json: data/json/items/resources/tailoring.json src/generate_stackable_sheet.py
	src/generate_stackable_sheet.py | $(CDDA_JSON_FORMATTER) > $@

yararezon_mod/no_collide_rail.json: data/json/furniture_and_terrain/terrain-railroads.json src/generate_no_collide_rail.py
	src/generate_no_collide_rail.py | $(CDDA_JSON_FORMATTER) > $@


# JSON整形
format lint: format-mod format-preset

format-mod:
	find yararezon_mod -name '*.json' -print0 | xargs -P 0 -0 -L 1 $(CDDA_JSON_FORMATTER)

format-preset:
	find yararezon_preset -name '*.json' -print0 | xargs -P 0 -0 -L 1 $(CDDA_JSON_FORMATTER)


# clean
clean:
	rm -f yararezon_mod/const_floor_olight.json yararezon_mod/makeshift_hood.json
