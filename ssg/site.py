from genericpath import exists, isdir
from os import mkdir
from pathlib import Path
import shutil
from ssg.parsers import Parser

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)
        self.parsers = None
        # ToDo: In constructor body set new instance variable parsers to expression parsers or []
        
        
    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)
        if path.exists(directory):
            shutil.rmtree(directory)
        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)
            elif path.is_file():
                Site.run_parser(path)

    def load_parser(extension):
        for parser in self.parsers:
            if Parser.valid_extension(extension):
                return parser

    def run_parser(path):
        parser = Site.load_parser(path.suffix)

        if parser is not None:
            Parser.parse(path, Parser.source, Parser.dest)
        else:
            print("Not Implemented")
