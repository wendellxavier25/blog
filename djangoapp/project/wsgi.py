import os
from pathlib import Path
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

BASE_DIR =  Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR.parent / 'dotenv_files' / '.env', override=True)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()
