# 🚀 FastAPI Starter Template

A minimal and clean FastAPI starter template with modular structure and versioned APIs.  
Built for quick project bootstrapping and easy scalability.

## 🛠 Features

- FastAPI with modular structure
- Versioned API routing (`v1`)
- `.env` config with `example.env`
- `pyproject.toml` + `uv` support

## 🚀 Getting Started

```bash
git clone https://github.com/mahdijafaridev/fastapi-starter.git your-project-name
cd fastapi-starter-template
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
cp example.env .env
fastapi dev app/main.py
````

Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

## 📁 Structure

```
app/
├── main.py
├── settings.py
├── utils/
└── api/
    ├── router.py
    └── v1/
        ├── router.py
        ├── endpoints/
        └── schemas/
```

## 📄 License

MIT © [Mohammad Mahdi Jafari](https://github.com/mahdijafaridev)
