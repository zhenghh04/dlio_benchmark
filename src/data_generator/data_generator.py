from abc import ABC, abstractmethod

from src.utils.argument_parser import ArgumentParser
import math
import os


class DataGenerator(ABC):

    def __init__(self):
        self._arg_parser = ArgumentParser.get_instance()
        self.data_dir = self._arg_parser.args.data_folder
        self.record_size = self._arg_parser.args.record_length
        self.file_prefix = self._arg_parser.args.file_prefix
        self.num_files = self._arg_parser.args.num_files
        self.num_samples = self._arg_parser.args.num_samples
        self._file_prefix = None
        self._dimension = None

    @abstractmethod
    def generate(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
        self._dimension = int(math.sqrt(self.record_size))
        self._file_prefix = os.path.join(self.data_dir, self.file_prefix)