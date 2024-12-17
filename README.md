# 🧠 Conceptile - Python/Django intern assessment

## 🚀 Project Overview
In this assignment, I have created a quiz application from a set of simple 20 questions.
I have implemeneted simple django's User models user authentication system with both 
register and login part. User can start the quiz and end quiz anytime they want, and view the correct and wrong choices they made. 

It has a simple UI implemented using bootstrap

### Hosted Service
🔗 Live Application: https://conceptile-assignment.onrender.com/auth/login/
- Render Service may take upto 50s to load, due to free plan.

![image](https://github.com/user-attachments/assets/1d06f4b0-7094-408d-ad79-126f1a5b0c6a)


## ✨ Features
- User Authentication
- Random Question Generation
- Real-time Quiz Tracking
- Simple and Intuitive Interface using Bootstrap

## 🛠️ Tech Stack
- Django
- Python 3.9+
- Bootstrap
- SQLite (Development)
- PostgreSQL (Production)[Used SupaBase] { for local development uncomment the sqllite code written in root settings}

## 🔧 Local Setup

### Prerequisites
- Python 3.9+
- Poetry (Recommended for virtual environment)
- Git

### Installation Steps

#### 1. Clone the Repository
```bash
git clone https://github.com/adwaithpj/conceptile-assignment
cd quiz-master
```

#### 2. Set Up Virtual Environment with Poetry 🐍
```bash
# Install Poetry if not already installed
pip install poetry

# Create virtual environment and install dependencies
poetry install
```

#### 3. Environment Configuration
```bash
# Activate virtual environment
poetry shell

# Run migrations
python manage.py makemigrations
python manage.py migrate
```
#### 4. Run Development Server
```bash
python manage.py runserver
```

## 🌐 Deployment

### Hosted Service
🔗 Live Application: https://conceptile-assignment.onrender.com/auth/login/

#### Login Credentials
You can create a account in  the register page.

## 🔐 Authentication Flow

### Login Process
1. Navigate to login page
2. Enter credentials
3. Upon successful authentication, redirected to quiz start page
4. Begin your quiz adventure! 🚀

### Authentication Details
- Built using Django's built-in authentication system
- Secure password hashing
- Session-based authentication

## 📝 Quiz Mechanics
- Randomly selected multiple-choice questions
- Real-time tracking of:
  - Total questions answered
  - Correct answers
  - Incorrect answers
- No time limit
- Immediate feedback after each question

## 🛡️ Security Features
- CSRF Protection
- Login Required for Quiz Access
- Secure User Sessions

## 💡 Assumptions & Limitations
- Questions pre-populated in database
- Single user authentication


## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

## 🐛 Reporting Issues
Please report issues [here](https://github.com/adwaithpj/conceptile-assignment/issues)

## 🌟 Support
If you found this project helpful, please consider starring the repository!

### Made with ❤️ and 🐍 Django
