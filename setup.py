import os
os.system("pip install pyarmor==7.6.0")
os.system("pyarmor obfuscate bot.py")
os.system("python dist/bot.py")