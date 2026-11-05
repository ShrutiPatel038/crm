# E-commerce Product Management – Agile & DevOps (Set 3)

## a) Git
```bash
git init
git add . && git commit -m "Initial product app"
git checkout -b feature/product-filter
# edit app.py (add ?category= filter in /products)
git add app.py && git commit -m "Add product filter by category"
git checkout main
git merge feature/product-filter
git log --oneline --graph
```

## b) GitHub Actions
File: `.github/workflows/ci.yml` – runs on push to `main`, installs dependencies
(`pip install -r requirements.txt`), runs `validate_products.py` and `pytest`.
Push to GitHub, then check the **Actions** tab, or run `gh run list` – status should be a green tick (success).

## c) JIRA (Scrum project: "E-commerce App")
Create project → Scrum template → Backlog → Create issue (type Story).

| Story | Priority | Points |
|---|---|---|
| As a customer, I want to see a list of products so that I can browse items. | High | 3 |
| As a customer, I want to filter products by category so that I find items quickly. | Medium | 5 |
| As a customer, I want to view product details so that I can decide before buying. | Low | 2 |

Workflow: create sprint → drag stories into it → Start sprint →
move each story on the board **To Do → In Progress → Done** → Complete sprint.

## d) Docker
```bash
docker build -t product-app .
docker run -d --name product-container -p 5000:5000 product-app
docker ps
docker inspect product-container
docker logs product-container
# open http://localhost:5000/products
```

## e) PyTest
`price.py` (18% tax) and `test_price.py` – parameterized cases for normal price, zero,
boundary values (0.01, 1000000) and invalid input (-1, "abc", None).
```bash
pytest -v
```

## f) Selenium
`app.py` has a `/login` page (admin / admin123). `selenium_login.py` uses locators
(ID, NAME, XPATH), explicit waits (`WebDriverWait`) and asserts valid & invalid login.
```bash
python app.py          # terminal 1
python selenium_login.py   # terminal 2
```
