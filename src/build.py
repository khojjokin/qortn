"""Builds the Qortn website: index.html as one self-contained page, plus privacy.html and terms.html.

The templates in src/ hold the pages; this fills in the logo (brand/qortn-mark-white-192.png: the site is black, so the
mark is white), the large mark (brand/qortn-mark-white-512.png, used once as a CSS variable for the hero and the background watermark), the
wordmark (from brand/make.py), the footer's wordmark mask and the app's screens from img/ as data URIs.
The legal pages load the small mark from /brand/ instead, so they stay a few kilobytes.
Run: python3 src/build.py   (after python3 brand/make.py if the logo changed)
"""
import base64, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(ROOT, 'brand'))
from make import RATIO, VIEWBOX, d as WORD  # noqa: E402


def data(path, kind):
    return f'data:{kind};base64,' + base64.b64encode(open(path, 'rb').read()).decode()


MARK = data(os.path.join(ROOT, 'brand', 'qortn-mark-white-192.png'), 'image/png')
MARK_BIG = data(os.path.join(ROOT, 'brand', 'qortn-mark-white-512.png'), 'image/png')


def word(h):
    return (f'<svg viewBox="{VIEWBOX}" height="{h}" width="{round(h * RATIO, 1)}" aria-hidden="true">'
            f'<path d="{WORD}" fill="currentColor"/></svg>')


def lockup(h, src=MARK):
    return (f'<img src="{src}" width="{round(h * 1.5)}" height="{round(h * 1.5)}" alt="" style="margin:-{round(h * .25)}px -{round(h * .1)}px">'
            f'{word(round(h * 1.04))}'
            '<span style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">Qortn</span>')


mask_svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VIEWBOX}"><path d="{WORD}"/></svg>'
page = open(os.path.join(HERE, 'index.template.html')).read()
page = page.replace('{{logo_nav}}', lockup(22)).replace('{{logo_foot}}', lockup(24))
page = page.replace('{{mark_big}}', MARK_BIG)
page = page.replace('{{wordmask}}', data_uri if (data_uri := 'data:image/svg+xml;base64,' + base64.b64encode(mask_svg.encode()).decode()) else '')
page = page.replace('{{word_ratio}}', str(RATIO))
page = re.sub(r'\{\{img:(\w+)\}\}', lambda m: data(os.path.join(ROOT, 'img', m.group(1) + '.webp'), 'image/webp'), page)
assert '{{' not in page, re.findall(r'\{\{[^}]+\}\}', page)
open(os.path.join(ROOT, 'index.html'), 'w').write(page)
print(f'index.html {len(page) // 1024} KB')

# The legal pages: the same lockup, with the mark as a file rather than inline.
for name in ('privacy', 'terms'):
    legal = open(os.path.join(HERE, name + '.template.html')).read()
    legal = legal.replace('{{logo_nav}}', lockup(22, '/brand/qortn-mark-white-192.png'))
    assert '{{' not in legal, re.findall(r'\{\{[^}]+\}\}', legal)
    open(os.path.join(ROOT, name + '.html'), 'w').write(legal)
    print(f'{name}.html {len(legal) // 1024} KB')
