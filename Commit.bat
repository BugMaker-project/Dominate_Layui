python setup.py sdist bdist_wheel
twine upload dist/*
git add .
git commit -m "PULL"
git push origin master