# 🧑‍💼 Employee Management System (Django)

A web-based **Employee Management System** built using the **Django Framework** and **SQLite3 database**.  
It allows administrators to manage employee information, contact details, and departmental data efficiently from a user-friendly web interface.

---

## 🚀 Features

- Add, edit, and delete employee records  
- Manage department and contact details  
- Admin panel for superuser access  
- Modular apps for clean organization (`About`, `Contact`, etc.)  
- Responsive frontend using Django templates and CSS  
- Easy deployment using PythonAnywhere  

---

## 🏗️ Project Structure

```
Employee_Management/
├── manage.py
├── db.sqlite3
├── Employee_Management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── About/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── About.html
└── Contact/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    └── templates/
        └── contact.html
```

---

## ⚙️ Installation & Local Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/Employee_Management.git
cd Employee_Management
```

### 2️⃣ Create and Activate a Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install Required Packages
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser
```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```

Now open your browser and visit:  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🗃️ Tech Stack

| Component | Technology |
|------------|-------------|
| Framework | Django |
| Database | SQLite3 |
| Frontend | HTML, CSS (Django Templates) |
| Deployment | PythonAnywhere |
| Version Control | Git + GitHub |

---

## 📦 Dependencies

Your `requirements.txt` file should contain:

```txt
Django>=5.0,<6.0
asgiref>=3.8,<4.0
sqlparse>=0.5,<1.0
tzdata>=2023.3,<2025.0
```

Optional (add if needed):
```txt
Pillow>=10.0,<11.0
whitenoise>=6.6,<7.0
gunicorn>=21.2,<22.0
python-dotenv>=1.0,<2.0
dj-database-url>=2.2,<3.0
```

---

## ☁️ Deployment on PythonAnywhere (with Static Files Setup)

### 1️⃣ Upload Your Project
- Log in to [PythonAnywhere](https://www.pythonanywhere.com)  
- Go to the **Files** tab and upload your ZIP file  
- Extract it in your home directory  

---

### 2️⃣ Create a Virtual Environment
In the **PythonAnywhere Console**, run:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3️⃣ Update Django Settings
In `Employee_Management/settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

---

### 4️⃣ Collect Static Files
In the console:
```bash
python manage.py collectstatic
```
This command gathers all static assets (CSS, JS, images) into the `staticfiles/` folder for deployment.

---

### 5️⃣ Configure the Web App in PythonAnywhere
1. Go to the **Web tab** → Click **Add a new web app**  
2. Choose **Manual configuration** → Select **Python 3.x**  
3. Set:
   - **Source code**: `/home/yourusername/Employee_Management`
   - **WSGI file**: `/home/yourusername/Employee_Management/Employee_Management/wsgi.py`

---

### 6️⃣ Set Up Static Files in the Web Tab
Add the following mapping in the **Static Files** section:
```
URL: /static/  
Directory: /home/yourusername/Employee_Management/staticfiles
```

---

### 7️⃣ Reload the Web App
Click **Reload** on the top right of the Web tab.

✅ Done!  
Your project is live at:  
**https://yourusername.pythonanywhere.com**

---

## 🧑‍💻 Author

**Ravi Maragada**  
🎓 Final Year Project — Django Web Development  
📧 *[your.email@example.com]*  

---

## 🪶 License

This project is licensed under the **MIT License** — feel free to use and modify it for learning or development.

---

✨ *A complete Employee Management System built with Django — simple, elegant, and ready for deployment!* ✨
