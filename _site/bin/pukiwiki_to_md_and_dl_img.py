#!/bin/bash


python3 ~/jekyll_workdir/openrtm_test/bin/pukiwiki_to_md9_old.py
cat output.md >>index.md
python3 ~/jekyll_workdir/openrtm_test/bin/dl_image3_fixed.py --start_url https://openrtm.org/openrtm/ja/node/"$1"

