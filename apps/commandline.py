from cmdapi import *
import os

stack = [0]

running = True
path = "/"
debug = False

while running:
    cmd = input("-> ").replace('top', str(stack[-1]))
    args = filter(cmd)
    running, debug, path = run(args, stack, cmd, path)