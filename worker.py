#!/usr/bin/env python3.9
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import discord
    import web3
    import parsimonious
except ImportError:
    install('discord.py')
    install('web3')
    install('parsimonious==0.8.1')
    import discord
    import web3
    import parsimonious
