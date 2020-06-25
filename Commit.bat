git add .
git commit -m "PULL"
git push master origin
python setup.py sdist bdist_wheel
twine upload dist/*