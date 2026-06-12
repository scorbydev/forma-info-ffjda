test:
	python -m pytest

sql-db:
	python 02_sql_licence_diagnostic/create_db.py

sql-demo:
	python 02_sql_licence_diagnostic/run_query.py "SELECT name FROM sqlite_master WHERE type='table';"

ocr-demo:
	python 04_pdf_ocr_agent/ocr_agent/cli.py --input 04_pdf_ocr_agent/samples/facture_stage_001.txt --type invoice --provider sample --output 04_pdf_ocr_agent/output.csv

