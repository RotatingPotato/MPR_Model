import uvicorn
from src.api import app

def main():
    # 執行 FastAPI 伺服器
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()