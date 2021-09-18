#!/usr/bin/env -S python
# -*- coding: utf-8 -*-
import os
import gettext

domain = "cataclysm-dda"
localedir = "lang/mo"
lang = ["ja"]
gt = None


def init(localedir=localedir):
    global gt
    path = os.path.normpath(os.path.expanduser(os.path.expandvars(localedir)))
    if not os.path.exists(path):
        raise FileNotFoundError(
            f'localedir = "{localedir}" が見つかりません\n'
            f'path = "{path}"')
    if not os.path.isdir(path):
        raise NotADirectoryError(
            f'localedir = "{localedir}" がディレクトリではありません\n'
            f'path = "{path}"')
    if gettext.find(domain, path, languages=lang) is None:
        raise FileNotFoundError(
            "moファイルが見つかりません\n"
            f'gettext.find("{domain}", "{path}", languages={lang})')
    gt = gettext.translation(domain, path, languages=lang)
    # gt.install()


# 初期化
init()
