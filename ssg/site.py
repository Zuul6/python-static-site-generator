from genericpath import exists, isdir
from os import mkdir
from pathlib import Path
import os
import shutil

class Site:
    def __init__(self, source, dest):
        source = Path(source)
        dest = Path(dest)
        
    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        if path.exists(directory):
            shutil.rmtree(directory)
        mkdir(directory, parents=True, exist_ok=True)

    def build(self):
        mkdir(self.dest, parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if isdir(path):
                Site.create_dir(path)