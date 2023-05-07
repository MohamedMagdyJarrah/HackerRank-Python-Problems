import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    s = sorted(s)
    for i in range(3):
      print(*list(Counter(s).most_common()[i]))