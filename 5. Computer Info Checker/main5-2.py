#Print readable format for your PC

import psutil

cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000)
print(f"cpu speed: {cpu_current_ghz}GHz")

cpu_core = psutil.cpu_count(logical=False)
print(f"core: {cpu_core}")

memory = psutil.virtual_memory()
memory_total = round(memory.total / 1024**3)
print(f"memory: {memory_total}GB")

disk = psutil.disk_partitions()
for p in disk:
    print(p.mountpoint, p.fstype, end=' ')
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024**3)
    print(f"disk size: {disk_total}GB")

net = psutil.net_io_counters()
sent = round(net.bytes_sent / 1024**3, 1)    
recv = round(net.bytes_recv / 1024**3, 1)    
print(f"sent: {sent}Mb receive: {recv}Mb")