import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if len(sys.argv) == 1:
        sys.argv[1:] = ["runserver", "127.0.0.1:8000", "--noreload"]
        # sys.argv[1:] = ["test"]
        # sys.argv[1:] = ["makemigrations"]
        # sys.argv[1:] = ["migrate"]

    execute_from_command_line(sys.argv)
