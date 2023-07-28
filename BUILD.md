Build package and publish to pypi:

```bash
yes | rm -rf dist/*
python3 -m build

# local install
pip3 install --force-reinstall --no-deps dist/dinov2_retrieval-0.0.2-py3-none-any.whl

# upload
python3 -m twine upload  dist/*
```
