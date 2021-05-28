"""
Executed by copier.
"""
import os


def ignore_dotenv():
    """Add .env file to .gitignore"""

    with open(".gitignore", "a") as fp:
        fp.write(os.linesep)
        fp.write(".env")
        fp.write(os.linesep)


ignore_dotenv()
