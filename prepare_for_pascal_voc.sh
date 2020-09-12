
mkdir Annotations
mkdir JPEGImages

mv test/*.xml Annotations/
mv train/*.xml Annotations/
mv valid/*.xml Annotations/
mv valid/*.jpg JPEGImages/
mv train/*.jpg JPEGImages/
mv test/*.jpg JPEGImages/

rm test
rm train
rm valid

python3 make_folders_and_files_for_pascal_voc.py
