import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import os
F=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','fonts','Outfit-%s.ttf')
def word(text, weight='SemiBold', track=-30):
    f=TTFont(F%weight); gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm
    asc=f['hhea'].ascent
    x=0; d=[]
    for ch in text:
        g=cmap[ord(ch)]; pen=SVGPathPen(gs)
        tp=TransformPen(pen,(1,0,0,-1,x,0)); gs[g].draw(tp)
        d.append(pen.getCommands()); x+=gs[g].width+track
    return ' '.join(d), x-track, upm
if __name__=='__main__':
    d,w,upm=word('rayot', sys.argv[1] if len(sys.argv)>1 else 'SemiBold')
    print(w,upm); open('word.d','w').write(d)
