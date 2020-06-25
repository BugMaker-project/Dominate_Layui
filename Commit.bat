git add .
git commit -m "PULL"
git push origin master
python setup.py sdist bdist_wheel
twine upload dist/*