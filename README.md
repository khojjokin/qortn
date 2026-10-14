# Qortn

The website and brand of **Qortn**, an independent software studio. Its first app is Community.

## The website
`index.html` is the whole site in one file (styles, script and images included), with the studio's own
`privacy.html` and `terms.html` beside it. It works on any
static host. Cloudflare Pages is configured in `wrangler.toml`; it publishes the repository root
directly, with no build command required. For Git integration, use `.` as the build output directory
and leave the build command blank. To deploy with Wrangler, run:

```
npx wrangler pages deploy .
```

To change it, edit `src/index.template.html` (or `src/privacy.template.html`, `src/terms.template.html`) and run:

```
python3 src/build.py
```

That rebuilds `index.html`, `privacy.html` and `terms.html`, filling in the logo, the wordmark and the app screens from `img/`.

The sections, top to bottom:
1. A sticky see-through top bar (About, How we build, Our apps, Contact).
2. The opening statement: Qortn, the studio, with its mark. The mark also sits very faintly behind the whole page.
3. Who we are, and how we build (three values).
4. Our apps: Community, with a headline, a line, one "Open Community" link and five iPhones fanned out (Map,
   a community page (Sabbath Prayer Circle), the Bible in front, the weekly lesson and the Hymnal). The phones are drawn in CSS; their screens
   are `img/map`, `community`, `bible`, `lessons` and `hymnal.webp`, captured from the app's demo build in dark
   mode at 390 points wide. On a phone the line-up shows the middle three.
5. A sideways tour of the same five screens (Bible, a community, Map, lessons, Hymnal).
6. Community on the big screen: a laptop showing a community page, Sabbath Prayer Circle (`img/maccommunity.webp`, the demo build at
   1440 × 900 at 2×, dark).
7. Platforms.
8. A footer (Qortn, contact, the Privacy policy and Terms of use) where the wordmark catches a moving band of violet light.

The site is always black (true black page, near-black surfaces, white text and the white mark), whatever the
visitor's light or dark setting, and stops its animations for visitors who have asked for reduced motion.

## The logo
The mark is the crystal winged figure in violet and blue (`brand/qortn-logo-original.jpg`). It is cut out of
its white background so it sits on light and dark. The wordmark "qortn" is Outfit SemiBold (SIL Open Font
License, in `fonts/`), turned into shapes so it needs no font.

| File in `brand/` | Use |
| --- | --- |
| `qortn-mark-1024.png`, `-512`, `-192` | The mark on a transparent background |
| `qortn-mark-white-1024.png`, `-512`, `-192` | The mark in white (soft white facets), used by the black website |
| `qortn-icon-1024.png` | App or social icon (the mark on near-black) |
| `qortn-wordmark.svg` / `qortn-wordmark-light.svg` | "qortn" for light / dark backgrounds |
| `qortn-logo-original.jpg` | The original artwork |

`python3 brand/make.py` remakes these from the original, and the site's `favicon-32.png`, `icon-192.png` and
`apple-touch-icon.png` (the white mark on black).

© Qortn. All rights reserved.
