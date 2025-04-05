# Honeypot Threat Logger

A full-stack honeypot web application that logs real-time unauthorized connection attempts. Built with a React frontend, Flask backend, and MongoDB Atlas for storage. The app enriches each connection log with **IP Geolocation**, **WHOIS lookup**, and displays the data in a dynamic admin dashboard.

---

## 🧠 Features

- 🌐 Real-time logging of connection attempts  
- 📍 IP Geolocation (Country, City, ISP, etc.)  
- 🔍 WHOIS lookup (Organization, Registrar, etc.)  
- 🧾 Admin & User login system  
- 📊 Clean dashboard with sortable log table  
- ☁️ Hosted with environment-based config support  
- 🎯 Socket.IO for real-time updates  

---

## 🧱 Tech Stack

| Layer      | Tech Used                                    |
|------------|-----------------------------------------------|
| Frontend   | React, Tailwind CSS, Axios, Socket.io-client  |
| Backend    | Python Flask, Flask-SocketIO                  |
| Database   | MongoDB Atlas                                 |
| IP Data    | ipapi & ipwhois libraries                     |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/honeypot-threat-logger.git
cd honeypot-threat-logger
```

---

### 2. Backend Setup (Flask)

// I didnt do this block
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

pip install -r requirements.txt
```

Create a `.env` file in `backend/`:

```
MONGO_URI=your_mongo_connection_string
SECRET_KEY=your_secret_key
```

Run the backend:

```bash
python app.py
```

---

### 3. Frontend Setup (React)

```bash
cd frontend
npm install
```

Create a `.env` file in `frontend/`:

```
REACT_APP_BACKEND_URL=http://localhost:5000
```

Run the frontend:

```bash
npm start
```

---

### 📡 Real-Time Socket Setup

The app uses **Socket.IO** for real-time log updates.  
Ensure the backend Flask-SocketIO server and frontend are connected on the same port/domain or use proper CORS settings if cross-origin.

---

# Main steps according to me
## Run listener.py
## Run app.py
## Run frontend (npm start)
## Login is detected when connection is stimulated (eg: run nc localhost 2222)

---

### 🗃️ Directory Structure

```
honeypot-threat-logger/
├── backend/
│   ├── app.py
│   ├── socket_events.py
│   ├── routes/
│   └── utils/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── utils/
│   │   └── App.js
├── .gitignore
├── README.md
```

---

### 🛡️ Security Notes

- Make sure your MongoDB URI and secret keys are **never exposed**.
- Use **dotenv** and environment variables for production deployment.
- Validate IP and socket traffic carefully if hosting publicly.

---

## 🧑‍💻 Author

Built by **Saanvi**

---
