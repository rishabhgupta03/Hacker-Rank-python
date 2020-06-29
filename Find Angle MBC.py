# -*- coding: utf-8 -*-
import math
ab = int(input())
bc = int(input())
bmc  = math.degrees(math.atan2(ab,bc))
print(f'{round(bmc)}°')
