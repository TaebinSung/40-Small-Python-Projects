# pip install psutil
import psutil

cpu = psutil.cpu_freq()
cpu_core = psutil.cpu_count(logical=False)
memory = psutil.virtual_memory()
disk = psutil.disk_partitions()
net = psutil.net_io_counters()

print(f"""
cpu: {cpu}
cpu_core: {cpu_core}
memory: {memory}
disk: {disk}
net: {net}
""")