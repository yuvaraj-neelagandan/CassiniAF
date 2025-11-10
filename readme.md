# install 
# pip install -r requirements.txt


# --- Run tests + generate Allure report ---

# pytest -m smoke --alluredir=reports

# pytest --alluredir=reports
# allure serve reports



# --- How to get GoRest API Token ---
# 1. Visit: https://gorest.co.in/
# 2. Click on 'Get Access Token'
# 3. Sign in (Google/GitHub)
# 4. Copy your token and paste it into .env as:
# GOREST_TOKEN=your_token_here