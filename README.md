# Qortn

The website and brand of **Qortn**, the software studio that makes [Community](https://seventhdayadventist.online).

## The website
`index.html` is the whole site in one file (styles, script and images included). It works on any
static host. Cloudflare Pages is configured in `wrangler.toml`; it publishes the repository root
directly, with no build command required. For Git integration, use `.` as the build output directory
and leave the build command blank. To deploy with Wrangler, run:

```
npx wrangler pages deploy .
```

To change it, edit `src/index.template.html` and run:

```
python3 src/build.py
```

That rebuilds `index.html`, filling in the logo, the wordmark and the app screens from `img/`.

The sections, top to bottom:
1. A sticky see-through top bar.
2. The opening statement.
3. Community shown on a Mac and an iPhone.
4. The App Store banner.
5. A sideways tour of five screens.
6. Community on the big screen.
7. Platforms.
8. About Qortn.
9. A footer where the wordmark catches a moving band of violet light.

The site follows light and dark mode, and stops its animations for visitors who have asked for reduced motion.

## The logo
The mark is the crystal winged figure in violet and blue (`brand/qortn-logo-original.jpg`). It is cut out of
its white background so it sits on light and dark. The wordmark "qortn" is Outfit SemiBold (SIL Open Font
License, in `fonts/`), turned into shapes so it needs no font.

| File in `brand/` | Use |
| --- | --- |
| `qortn-mark-1024.png`, `-512`, `-192` | The mark on a transparent background |
| `qortn-icon-1024.png` | App or social icon (the mark on near-black) |
| `qortn-wordmark.svg` / `qortn-wordmark-light.svg` | "qortn" for light / dark backgrounds |
| `qortn-logo-original.jpg` | The original artwork |

`python3 brand/make.py` remakes these from the original.

© Qortn. All rights reserved.
