# Makefile
CDDA_JSON_FORMATTER:=tool/json_formatter.exe

.PHONY: all generate format


all: generate format


# JSON¶¬
generate: yararezon_mod/const_floor_olight.json
	./src/generate_floor_olight.py | $(CDDA_JSON_FORMATTER) > $<


# JSON®Œ`
format lint: format-mod format-preset

format-mod:
	find yararezon_mod -name '*.json' -print0 | xargs -P 0 -0 -L 1 $(CDDA_JSON_FORMATTER)

format-preset:
	find yararezon_preset -name '*.json' -print0 | xargs -P 0 -0 -L 1 $(CDDA_JSON_FORMATTER)
