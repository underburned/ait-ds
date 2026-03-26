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
    dir_path = Path('labs_received/labs_AIT-DS_2026')
    groups = ['6401-010302D', '6402-010302D', '6403-010302D', '6404-010302D', '6405-010302D']
    path_list: List[Path] = []

    regexp_str = r'^(?P<Surname>[А-ЯЁа-яё]+)\s(?P<Name>[А-ЯЁа-яё]+)\s(?P<MiddleName>[А-ЯЁа-яё]+)$'

    for g_name in groups:
        with open(dir_path / f'{g_name}.txt', 'r', encoding='utf8') as f:
            for line in f.readlines():
                m_res = re.search(regexp_str, line)
                if m_res is not None:
                    surname = m_res.group('Surname')
                    name = m_res.group('Name')
                    middle_name = m_res.group('MiddleName')
                    path_list.append(dir_path / f'{g_name}' / f'{surname}_{name[0]}{middle_name[0]}')

    for p in tqdm(path_list, position=0, leave=True, file=sys.stdout, colour="green"):
        p.mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    main()
