# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function
import sys

import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.terminal import TerminalFormatter


class HighlightRenderer(mistune.Renderer):
    def paragraph(self, text):
        return '{}\n\n'.format(text)

    def codespan(self, code):
        return '`{}`'.format(code)

    def block_code(self, code, lang):
        if not lang:
            lang = 'rust'
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = TerminalFormatter()
        text = highlight(code, lexer, formatter)
        return '{}\n'.format(text)

    def list(self, body, ordered=True):
        return '{}\n'.format(body)

    def list_item(self, text):
        return ' * {}\n'.format(text)

    def link(self, link, title, text):
        return link

    def autolink(self, link, is_email=False):
        return link

renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)


def main():
    if sys.version_info > (3,):
        code = sys.stdin.buffer.read()
    else:
        code = sys.stdin.read()
    print(markdown(code))
    return 0
