#!/bin/bash
set -e
echo "処理開始"

python3 ~/jekyll_workdir/openrtm_test/pukiwiki_to_md9_old.py
cat output.md >>index.md

sed -i 's/width="100;"/width="60%;"/g' index.md


python3 ~/jekyll_workdir/openrtm_test/dl_image3_fixed.py --start_url https://openrtm.org/openrtm/ja/node/"$1"


echo "処理終了"

