import re
from pathlib import Path
import subprocess
import sys
from tqdm.auto import tqdm
from typing import List, Set, Union


class UtilityMethods:
    def __init__(self):
        pass

    @staticmethod
    def absolute_file_path(relative_path: Union[str, Path]) -> str:
        p = Path(relative_path)
        return str(p.resolve())

    @staticmethod
    def file_complete_name(path: Union[str, Path]) -> str:
        p = Path(path)
        return p.name

    def file_path_list(self, input_dir: Union[str, Path], extension_list: Union[List[str], Set[str]], name_only=False):
        file_path_list = []
        input_path = Path(input_dir)
        if input_path.is_dir():
            if input_path.exists():
                path_list = (p.resolve() for p in input_path.glob("**/*") if p.suffix[1:] in extension_list)

                for path in path_list:
                    if name_only:
                        file_path_list.append(self.file_complete_name(path))
                    else:
                        file_path_list.append(self.absolute_file_path(path))
                file_path_list = sorted(file_path_list, key=self.natural_key)

        return file_path_list

    @staticmethod
    def natural_key(str_line):
        """See http://www.codinghorror.com/blog/archives/001018.html"""
        return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', str_line)]


def main():
    um = UtilityMethods()
    dir_path = 'labs_received'
    file_path_list = um.file_path_list(dir_path, ['ipynb'])
    for p in tqdm(file_path_list, position=0, leave=True, file=sys.stdout, colour="green"):
        command = ['jupyter', 'trust', f"{p}"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        # Print the output on the same line
        tqdm.write(stdout.decode(), end='')


if __name__ == '__main__':
    main()
