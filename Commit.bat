git add .
git commit -m "PULL"
git pull master origin
python setup.py sdist bdist_wheel
twine upload dist/*