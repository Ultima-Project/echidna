from os import listdir, getpid
from random import choice
from time import time
from discord import __version__ as discord_version
from platform import python_version
from psutil import Process, virtual_memory, cpu_percent
from humanize import naturaldelta


def random_file(path):
    file = choice(listdir(path))
    return path+file


def stats():
    proc = Process()
    with proc.oneshot():
        uptime = naturaldelta(time()-proc.create_time())
        uptime = uptime[:-6]
        cpu_usage = int(cpu_percent())
        mem_total = virtual_memory().total >> 20
        pid = getpid()
        py = Process(pid)
        memoryUse = py.memory_info()[0] * 10**6

    fields = [
        ('Uso della CPU', str(cpu_usage) + '%', True),
        ('Utilizzo della memoria', str(memoryUse)[:2] + ' MB', True),
        ('Totale memoria', str(mem_total) + ' MB', True),
        ('Discord.py', discord_version, True),
        ('Python', python_version(), True),
        ('Uptime', uptime, True)
    ]

    return fields
