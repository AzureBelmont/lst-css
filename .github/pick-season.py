"""Choose which theme season.css should be a copy of today.

Holidays win over the base season, and only for their window. If the chosen
theme has not been built yet, fall back so that season.css always points at a
real file — a 404 is worse for anyone using it than a slightly-off theme.

Prints  theme=<name>  for the workflow to read.
"""
import datetime, os, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

d  = datetime.date.today()
md = (d.month, d.day)

HOLIDAYS = [
    ((10, 24), (11,  1), 'halloween'),
    ((12, 15), (12, 26), 'yule'),
    (( 2, 10), ( 2, 15), 'valentine'),
]
SEASONS = [
    ((12, 1, 2), 'winter'),
    (( 3, 4, 5), 'spring'),
    (( 6, 7, 8), 'summer'),
    (( 9,10,11), 'harvest'),
]
# used only when the season we actually want has not been built yet
FALLBACK = ['harvest', 'halloween', 'winter', 'spring', 'summer']

def exists(name):
    return os.path.isfile(os.path.join(REPO, name + '.css'))

season = next(n for months, n in SEASONS if d.month in months)
holiday = next((n for s, e, n in HOLIDAYS if s <= md <= e), None)

for candidate, why in [(holiday, 'holiday'), (season, 'season')] + [(f, 'fallback') for f in FALLBACK]:
    if candidate and exists(candidate):
        print('theme=' + candidate)
        print('reason=' + why)
        sys.exit(0)

print('theme=')
print('reason=nothing built yet')
