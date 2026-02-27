import os
import subprocess
import sys
import time

import psutil

target = sys.argv[1]
target_args = sys.argv[2:]

disk_size = os.path.getsize(target)

proc = subprocess.Popen([target, *target_args])
ps = psutil.Process(proc.pid)

peak_rss = 0
start = time.perf_counter()

while proc.poll() is None:
    try:
        peak_rss = max(peak_rss, ps.memory_info().rss)
    except psutil.NoSuchProcess:
        break
    time.sleep(0.001)

elapsed = time.perf_counter() - start
exit = proc.wait()

print(f"""
Disk size: {disk_size} bytes ({disk_size / 1024} KB or {disk_size / 1024 / 1024} MB)
Peak RSS: {peak_rss} bytes ({peak_rss / 1024} KB or {peak_rss / 1024 / 1024} MB)
Wall time: {elapsed} seconds
Exit code: {exit}""")
