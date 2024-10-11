set PYTHONPATH=%cd%
python src/bot.py 
python -m unittest tests.test_utils.test_report_generator
