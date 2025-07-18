# 📝 Flask To-Do App with MongoDB

A clean, full-stack CRUD To-Do application built with **Flask**, **Python**, and **MongoDB**.  
Built from scratch to learn and showcase backend and web development skills.

> Author: Mohan Krishna  
> GitHub: [mohankrishna36](https://github.com/mohankrishna36)

---

## 🚀 Features

- ✅ Add new tasks with priority & status
- ✏️ Edit or update tasks
- 🗑️ Delete tasks
- 📋 View tasks in a styled Bootstrap table
- 📦 MongoDB for data storage
- 💡 Flash messages for user feedback
- 🎨 Responsive UI with Bootstrap

---

## 🧰 Tech Stack

- Python 3.x
- Flask
- MongoDB (via PyMongo)
- Jinja2 templates
- Bootstrap 5

---

## 🗂️ Project Structure

Flask-To-Do-App-with-MongoDB/
├─ flask_app/
│ ├─ init.py # App factory
│ ├─ routes.py # Routes / views
│ └─ templates/
│ ├─ index.html
│ └─ edit.html
├─ db.py # MongoDB connection
├─ task_operations.py # CRUD operations
├─ utils.py # Time formatting & validators
├─ app.py # Main entry point
├─ requirements.txt
├─ README.md
└─ .gitignore


## ⚙️ Setup Instructions

Follow these steps to run the app locally:

```bash
# 1. Clone this repo
git clone https://github.com/mohankrishna36/Flask-To-Do-App-with-MongoDB.git
cd Flask-To-Do-App-with-MongoDB

# 2. Create and activate virtual environment
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app.py
Visit: http://127.0.0.1:5000 in your browser

🌍 Environment Variables (Optional)
You can set up a .env file for secrets (optional but recommended):

MONGO_URI=mongodb://localhost:27017/
SECRET_KEY=your_secret_key_here


🌱 Future Improvements
🧑 User authentication (Login/Signup)

🕓 Due dates and reminders

🔔 Notification system

🌗 Dark mode support

📱 Responsive mobile UI

🤝 Contributing
Feel free to fork this repo, open issues, or submit PRs.
This is a personal learning project — open to improvements.

📬 Connect with Me
🔗 LinkedIn: http://www.linkedin.com/in/mohan-krishna-aruru-84a338237

💻 GitHub: mohankrishna36
