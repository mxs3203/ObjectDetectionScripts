
mkdir Annotations
mkdir JPEGImages

mv test/*.xml Annotations/
mv train/*.xml Annotations/
mv valid/*.xml Annotations/
mv valid/*.jpg JPEGImages/
mv train/*.jpg JPEGImages/
mv test/*.jpg JPEGImages/

rm -r test
rm -r train
rm -r valid

python make_folder_and_files_for_pascal_voc.py

nano labels.txt
