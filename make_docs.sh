cd ./docs_pntl/ 
make html
cd ..
rm -rf ./docs
mv ./docs_pntl/_build/html ./docs
