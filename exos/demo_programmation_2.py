"""
Ceci est un programme montrant quelque chose de plus complexe.

Ce programme utilise des dates avec le module datetime qui ne sera pas
abordé dans cette formation.
"""

import datetime as dt

today = dt.date.today()
xmas = today.replace(month= 12, day=25)
to_xmas = xmas - today

print(f"Il reste {to_xmas.days} jours jusqu'à Noël")
