import time
import logging
import sys


a_logger = logging.getLogger()
a_logger.setLevel(logging.INFO)
format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(format)

a_logger.addHandler(stdout_handler)

mapper = {
  50: "L",
  40: "XL",
  10: "X",
  9: "IX",
  5: "V",
  4: "IV",
  1: "I",
  0: "."
}

def countdown(time_in_secs):
  
  while time_in_secs:
    mins, secs = divmod(time_in_secs, 60)
    timer = '\t{:s}:{:s}{:s}'.format(decimal_to_roman(mins), decimal_to_roman(secs), "     ")
    print(timer, end="\r")
    time.sleep(1)
    time_in_secs -= 1

def decimal_to_roman(num):
  value = ""
  val = num
  for key in mapper:
    if(key == 0): return value+mapper[key]

    quo = int(val / key)
    value = (value + (mapper[key] * quo)) if(quo > 0) else value
    val = val % key

  return value

countdown(1800)