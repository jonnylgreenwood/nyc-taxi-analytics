1. Nav to proj folder
   cd nyc-taxi-analytics
2. create venv
   python3 -m venv .venv
3. Activate venv
   source .venv/bin/activate
4. Install dependencies
   pip install requests beautifulsoup4 pandas duckdb pyarrow
5. freeze reqs
   pip freeze > requirements.txt
6. Add VS Code integration
   Python: Select Interpreter
7. Update .gitignore
   .venv/
   data/raw/
   __pycache__/