
# new-py-dev 🚀

Welcome to the **new-py-dev** repository. This project serves as a foundational data inference pipeline and backend routing service for AI and analytics workflows.

## 🛠 Tech Stack
* **Language:** Python 3.10+
* **Framework:** FastAPI
* **Database/Auth:** Supabase

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/BLVCK-MAMBA-6/new-py-dev.git](https://github.com/BLVCK-MAMBA-6/new-py-dev.git)
   cd new-py-dev



2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```


3. Install dependencies:
```bash
pip install -r requirements.txt

```



## 🚀 Quick Start

1. Set up your environment variables in a `.env` file in the root directory:
```env
SUPABASE_URL=your-supabase-url
SUPABASE_KEY=your-supabase-key

```


2. Run the FastAPI development server:
```bash
uvicorn main:app --reload

```


3. Navigate to `http://127.0.0.1:8000/docs` in your browser to access the interactive Swagger API documentation.

## 🤝 Contributing

1. Create a new feature branch (`git checkout -b feature/amazing-feature`).
2. Commit your changes (`git commit -m 'Add some amazing feature'`).
3. Push to the branch (`git push origin feature/amazing-feature`).
4. Open a Pull Request
