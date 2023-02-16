# check_assets.py

"""
Performs several checks on asset folder contents including:
 - metadata content
 - folder content
"""

import argparse
import json
from pathlib import Path
import sys

SK_FOLDERS = {'Default',
              'Light',
              'Medium-Light',
              'Medium',
              'Medium-Dark',
              'Dark'}


def main():

    ap = argparse.ArgumentParser()
    ap.add_argument("assets",
                    help="Path to asset root folder",
                    type=Path)
    opts = ap.parse_args()

    errors = False

    for jp in opts.assets.rglob("../**/metadata.json"):
        with open(jp, 'r', encoding="utf-8") as jf:
            md = json.load(jf)

        uc = md.get('unicode')
        cn = md.get('cldr')
        print(cn+": U+"+str(uc).upper())
        ucbase = uc.split(" ")[0]

        try:
            with open(Path("C:/Users/Crescent/Repositories/Microsoft/fluentui-emoji/assets/"+cn+"/Color/"+cn+" color.svg"), "r+", encoding="utf-8") as emojifile:
                currentemojioutput = open("C:/Users/Crescent/.emojioutput/"+uc+".svg", "w")
                for line in emojifile:
                    currentemojioutput.write(line)

        except IOError:
            with open("C:/Users/Crescent/Repositories/Microsoft/fluentui-emoji/assets/"+cn+"/Default/Color/"+cn+" color default.svg","r+", encoding="utf-8") as emojifile_d:
                currentemojioutput_d = open("C:/Users/Crescent/.emojioutput/"+uc+".svg", "w")
                for line in emojifile_d:
                    currentemojioutput_d.write(line)


if __name__ == '__main__':
    sys.exit(main())
