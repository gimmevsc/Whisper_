# **Web Messenger Application**

This project is a full-stack web messenger application built using **Django** (backend) and **React** (frontend).

---

## **Setup**



#### Clone the repository:
```bash
git clone https://github.com/gimmevsc/whisper.git
cd <your-repository-folder>
```
### **1. Backend - Django Setup**

#### Create and activate a virtual environment:
##### For Mac/Linux:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

##### For Windows:
```
python -m venv venv
venv\Scripts\activate
```

#### Install the required dependencies:
```bash
pip install -r requirements.txt
```

#### Set Up Environment Variables
Create a .env file in the project root by copying .env.example:
```bash
cp .env.example .env
```

#### Run migrations:
``` bash
cd whisper

python3 manage.py makemigrations register
python3 manage.py makemigrations chat 
python3 manage.py makemigrations reset_password

python3 manage.py migrate
```

#### Start the Django server:
##### For Mac/Linux/Win:

```bash
python3 manage.py runserver
```

##### The backend server will start at: http://127.0.0.1:8000

### **2. Frontend - React Setup**

#### Clone the repository (if you haven't already):
```bash
git https://github.com/gimmevsc/whisper.git
cd <your-repository-folder>
```

#### Checkout the front branch:
```bash
cd frontend
```
#### Install dependencies:
```bash
npm install
```
#### Start the React development server:
```bash
npm start
```

The React app will run at: http://localhost:3000

The program will work on: http://localhost:3000
