"""Original pen illustrations for Atul's GitHub profile. No network access."""

from html import escape
from pathlib import Path
import random

from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen

ROOT = Path(__file__).resolve().parents[1]
FONTS = {name: TTFont(ROOT / 'assets/fonts' / f'{name}.woff2') for name in ('pen', 'reader')}
THEMES = {
    'light': ('#eeeae0', '#3b3a36', '#69675e', '#60715d', '#936957'),
    'dark': ('#20241f', '#eeeae0', '#c3c4b7', '#b6c6a6', '#d6a18a'),
}
TEXT_LEFT = 44
DOODLE_CENTERS = {
    'tube': (342, 63), 'reset': (346, 70), 'sheetato': (345, 61),
    'botato': (344, 66), 'halo': (341, 69), 'corner': (333, 72),
}


def lettering(words, x, y, size, font='pen', color='var(--ink)'):
    face = FONTS[font]
    glyphs = face.getGlyphSet()
    mapping = face.getBestCmap()
    scale = size / face['head'].unitsPerEm
    cursor = 0
    pieces = []
    for char in words:
        glyph = glyphs[mapping[ord(char)]]
        pen = SVGPathPen(glyphs, ntos=lambda n: f'{n:.2f}'.rstrip('0').rstrip('.'))
        glyph.draw(pen)
        pieces.append(f'<path transform="translate({cursor:.2f} 0)" d="{pen.getCommands()}"/>')
        cursor += glyph.width
    return f'<g aria-label="{escape(words)}" fill="{color}" transform="translate({x} {y}) scale({scale} {-scale})">{"".join(pieces)}</g>'


def line(d, color='var(--ink)', width=1.7, extra=''):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'


def svg(body, width, height, theme, title, motion=False):
    paper, ink, muted, olive, clay = THEMES[theme]
    css = f':root{{--paper:{paper};--ink:{ink};--muted:{muted};--olive:{olive};--clay:{clay}}}'
    if motion:
        css += '''
        .push{transform-origin:660px 291px;animation:push 5.8s ease-in-out infinite}
        .rock{transform-origin:761px 252px;animation:rock 5.8s ease-in-out infinite}
        .eyes{transform-box:fill-box;transform-origin:center;animation:blink 7.3s linear infinite}
        @keyframes push{0%,15%,90%,100%{transform:rotate(0deg)}45%,65%{transform:translate(4px,-1px) rotate(4deg)}}
        @keyframes rock{0%,20%,90%,100%{transform:rotate(0deg)}45%,65%{transform:translate(3px,-1px) rotate(5deg)}}
        @keyframes blink{0%,42%,45%,100%{transform:scaleY(1)}43%,44%{transform:scaleY(.08)}}
        '''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">{escape(title)}</title><style>{css}</style><path fill="var(--paper)" d="M0 0H{width}V{height}H0Z"/>{body}</svg>\n'


def meowl():
    return '''<g class="push" stroke="var(--ink)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path fill="var(--paper)" d="M620 279Q609 263 617 237L621 218L617 191Q621 182 638 202Q653 195 669 202Q684 185 686 193L683 220Q698 240 685 266Q679 282 661 289Q636 297 620 279Z"/>
    <path fill="none" d="M622 218L624 201L633 211M673 210L680 201L678 217M625 246Q621 268 630 277M635 287L628 295L640 293M656 289L658 296L666 291M622 232L608 227M621 238L608 242M677 233L690 229M679 239L693 244"/>
    <path fill="var(--paper)" d="M677 248Q686 234 703 229L706 237Q695 250 681 260Q674 258 677 248Z"/>
    <path fill="var(--olive)" opacity=".14" stroke="none" d="M624 245Q613 271 632 284L640 287Q623 268 635 247Z"/>
    <g class="eyes"><ellipse fill="var(--paper)" cx="638" cy="224" rx="11" ry="13"/><ellipse fill="var(--paper)" cx="664" cy="224" rx="11" ry="13"/>
    <ellipse fill="var(--ink)" cx="641" cy="225" rx="6" ry="8"/><ellipse fill="var(--ink)" cx="667" cy="225" rx="6" ry="8"/>
    <path stroke="var(--paper)" d="M642 221L643 222M668 221L669 222"/></g>
    <path fill="none" d="M626 207L641 211M658 211L675 206M645 239L650 242L654 238M650 242L650 246M650 246Q643 251 640 246M650 246Q656 251 660 246M643 262Q648 267 653 262M638 273L642 275M650 277L654 275"/>
    </g>'''


def rock():
    body = '<g class="rock">'
    body += '<path d="M702 230C683 208 691 174 711 156Q744 130 780 146Q818 156 823 193Q829 226 805 247Q769 273 729 258Z" fill="var(--paper)" stroke="var(--ink)" stroke-width="2.1"/>'
    rng = random.Random(24)
    for _ in range(43):
        x, y = rng.uniform(708, 798), rng.uniform(164, 235)
        body += line(f'M{x:.1f} {y:.1f}q{rng.uniform(-28,28):.1f} {rng.uniform(-40,40):.1f} {rng.uniform(-14,14):.1f} {rng.uniform(-20,20):.1f}', 'var(--ink)', .8, 'opacity=".45"')
    body += line('M702 202L737 154L773 159L814 196L795 239L744 254L710 223M702 224L759 159L798 185L755 242L714 204M726 167L709 205L752 250M794 159L776 194L813 215', 'var(--ink)', 1.1)
    return body + '</g>'


def hero(theme, mobile=False, animated=True):
    art = line('M-5 330Q131 308 206 326T359 332Q403 332 456 316L517 320L558 297L601 299Q650 291 698 271T796 249Q861 226 965 154', width=2)
    art += line('M503 321l13 17l16-5l14 10M559 299l12 14l19-1l10 11M678 282l9 14l20-2l13 10M809 244l16 10l7-20M859 219l6 12l13-11', 'var(--muted)', 1)
    art += line('M355 277Q393 273 412 248L449 263L506 221L553 243L584 226M730 118Q739 101 752 110Q760 90 777 106Q790 96 801 112Q812 111 820 119Z', 'var(--muted)', .8, 'opacity=".5"')
    art += rock() + meowl()
    art += lettering('still pushing.', 534, 181, 22, color='var(--muted)')
    art += line('M599 192Q605 206 611 211M605 208L611 212L612 205', 'var(--muted)', 1)
    if mobile:
        body = lettering('atul kanodia.', 32, 64, 43)
        body += lettering('economics at ucl.', 32, 101, 24, 'reader')
        body += lettering('a little further.', 32, 170, 38)
        body += '<g transform="translate(-402 77) scale(1.02)">' + art + '</g>'
        body += lettering('games, data & things i made.', 32, 438, 23, 'reader')
        return svg(body, 520, 468, theme, 'Atul Kanodia. Economics at UCL. A scribbled meowl pushes a boulder uphill.', animated)
    body = lettering('atul kanodia.', TEXT_LEFT, 82, 55)
    body += lettering('economics at ucl.', TEXT_LEFT, 122, 25, 'reader')
    body += lettering('a little further.', TEXT_LEFT, 231, 54)
    body += lettering('games, data & things i made.', TEXT_LEFT, 270, 24, 'reader')
    return svg(art + body, 960, 370, theme, 'Atul Kanodia. Economics at UCL. A little further. A scribbled meowl pushes a boulder uphill.', animated)


def doodle(kind):
    if kind == 'tube':
        return line('M289 47L315 47L341 70L394 70M293 87L318 87L341 70L375 36', 'var(--clay)', 2.4) + ''.join(f'<circle cx="{x}" cy="{y}" r="4" fill="var(--paper)" stroke="var(--ink)"/>' for x,y in [(298,47),(341,70),(376,70),(318,87),(366,45)])
    if kind == 'reset':
        return line('M312 39L381 36L390 83L313 90Z M312 39L302 51L303 101L381 103L390 83M303 101L313 90M323 48L371 46L376 75L324 79Z') + lettering('check', 328, 67, 16)
    if kind == 'sheetato':
        return line('M330 28L365 38L378 68L351 94L322 78L315 49Z M330 28L338 58L365 38M338 58L378 68M338 58L351 94M315 49L338 58L322 78', 'var(--olive)', 2) + line('M395 32v12M389 38h12M297 77v10M292 82h10', 'var(--muted)')
    if kind == 'halo':
        return line('M301 37L383 40L378 90L344 86L329 101L329 85L298 81Z M313 53L367 55M312 63L354 65M312 72L343 73', 'var(--olive)')
    if kind == 'botato':
        return line('M295 82Q327 99 334 72T374 40L389 43M382 35L390 43L380 49', 'var(--olive)', 2, 'stroke-dasharray="3 6"') + line('M315 43L338 41L340 62L316 64Z M355 73L376 76L374 96L352 93Z')
    return '<g transform="translate(-128 -97) scale(.7)">' + meowl() + '</g>'


CARDS = [
    ('tube', 'tube reliability', 'which line lets you down?', 'eleven lines, one leaderboard.'),
    ('reset', 'codex resets', 'has tibo said anything yet?', 'announcements, replies & a check key.'),
    ('sheetato', 'sheetato', 'a game got me into statistics.', 'item prices, odds & expensive mistakes.'),
    ('botato', 'botato', 'put something in its way.', 'a small meowl finds another route.'),
    ('halo', 'halo', 'what did we agree again?', 'meeting notes you can trace back.'),
    ('corner', 'the meowl site', 'the rest of this notebook.', 'a hillside. a boulder. a few distractions.'),
]


def card(kind, title, first, second, theme, mobile=False):
    center_x, center_y = DOODLE_CENTERS[kind]
    if mobile:
        width, height = 520, 188
        body = line('M14 11Q260 9 506 12L506 175Q260 178 14 176Z', 'var(--muted)', .8)
        body += lettering(title, 32, 58, 33)
        body += lettering(first, 32, 114, 25, 'reader')
        body += lettering(second, 32, 145, 23, 'reader', 'var(--muted)')
        body += f'<g transform="translate(433 52) scale(.72) translate({-center_x} {-center_y})">{doodle(kind)}</g>'
        body += line('M466 159H484L478 153M484 159L478 165', width=1.5)
    else:
        width, height = 960, 132
        body = line('M16 11Q480 9 944 12L944 120Q480 122 16 120Z', 'var(--muted)', .8)
        body += lettering(title, TEXT_LEFT, 77, 33)
        body += lettering(first, 326, 57, 24, 'reader')
        body += lettering(second, 326, 89, 22, 'reader', 'var(--muted)')
        body += f'<g transform="translate(820 66) scale(.82) translate({-center_x} {-center_y})">{doodle(kind)}</g>'
        body += line('M891 66H915L907 59M915 66L907 73', width=1.6)
    return svg(body, width, height, theme, f'{title}: {first} {second}')


def main():
    for theme in THEMES:
        for mobile in (False, True):
            name = f'header-{theme}{"-mobile" if mobile else ""}.svg'
            (ROOT / 'assets' / name.replace('.svg', '-animated.svg')).write_text(hero(theme, mobile), encoding='utf-8')
            (ROOT / 'assets' / name.replace('.svg', '-still.svg')).write_text(hero(theme, mobile, animated=False), encoding='utf-8')
        for kind, title, first, second in CARDS:
            for mobile in (False, True):
                name = f'row-{kind}-{theme}{"-mobile" if mobile else ""}.svg'
                (ROOT / 'assets' / name).write_text(card(kind, title, first, second, theme, mobile), encoding='utf-8')


if __name__ == '__main__':
    main()
