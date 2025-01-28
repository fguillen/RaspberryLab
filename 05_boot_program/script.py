#!/usr/bin/env python3

from datetime import datetime

current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open("/tmp/script_test.log", "a") as log_file:
    log_file.write(f"{current_date}\n")
