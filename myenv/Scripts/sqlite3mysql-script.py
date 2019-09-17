#!d:\web_create_project\myenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sqlite3-to-mysql==1.2.12','console_scripts','sqlite3mysql'
__requires__ = 'sqlite3-to-mysql==1.2.12'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('sqlite3-to-mysql==1.2.12', 'console_scripts', 'sqlite3mysql')()
    )
