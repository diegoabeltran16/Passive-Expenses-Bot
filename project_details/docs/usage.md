$env:PYTHONPATH = "$PWD"
python src/bot.py 

set PYTHONPATH=%cd%
python -m unittest discover tests/test_utils       