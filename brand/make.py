"""Qortn brand files: the wordmark "qortn" (Outfit SemiBold, OFL, turned into shapes) and the logo in
the sizes the apps and the website use. The mark itself is the owner's own artwork
(qortn-logo-original.jpg), cut out of its white background so it sits on light and dark.
Run: python3 brand/make.py
"""
import os
import numpy as np
from PIL import Image
from word import word

HERE = os.path.dirname(os.path.abspath(__file__))
d, ww, _ = word('qortn', 'SemiBold', -28)
VB_TOP, VB_H = -700, 915  # the letters sit on y = 0; ascenders reach up to about -700, descenders down to about 215
VIEWBOX = f'-10 {VB_TOP} {round(ww + 20)} {VB_H}'
RATIO = round((ww + 20) / VB_H, 4)


def cut_out():
    """The mark on a transparent square, keeping its own colours (so the pale facets stay on dark)."""
    im = Image.open(os.path.join(HERE, 'qortn-logo-original.jpg')).convert('RGB')
    im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)
    a = np.asarray(im).astype(np.float32) / 255
    dist = np.max(1 - a, axis=2)
    alpha = np.clip((dist - 0.035) * 6, 0, 1)
    k = np.clip(dist / 0.2, 0, 1)
    un = np.clip((a - (1 - k)[..., None]) / np.where(dist > 0, k, 1)[..., None], 0, 1)
    rgb = np.where((alpha < 1)[..., None], un, a)
    img = Image.fromarray((np.dstack([rgb, alpha]) * 255).round().astype(np.uint8), 'RGBA')
    img = img.crop(img.getchannel('A').point(lambda v: 255 if v > 10 else 0).getbbox())
    w, h = img.size
    s = max(w, h)
    pad = int(s * 0.04)
    sq = Image.new('RGBA', (s + 2 * pad, s + 2 * pad), (0, 0, 0, 0))
    sq.paste(img, ((s + 2 * pad - w) // 2, (s + 2 * pad - h) // 2))
    return sq


if __name__ == '__main__':
    mark = cut_out()
    for size in (1024, 512, 192):
        mark.resize((size, size), Image.LANCZOS).save(os.path.join(HERE, f'qortn-mark-{size}.png'))
    # App / social icon: the mark on the studio's near-black.
    icon = Image.new('RGBA', (1024, 1024), (13, 10, 20, 255))
    m = mark.resize((820, 820), Image.LANCZOS)
    icon.paste(m, (102, 102), m)
    icon.convert('RGB').save(os.path.join(HERE, 'qortn-icon-1024.png'))
    for name, fill in (('qortn-wordmark.svg', '#14101F'), ('qortn-wordmark-light.svg', '#FFFFFF')):
        open(os.path.join(HERE, name), 'w').write(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{VIEWBOX}"><path d="{d}" fill="{fill}"/></svg>\n')
    print('ok', RATIO)
