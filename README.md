<div align="center">

# 🛍️ Django Store

### A Modern E-Commerce Web Application

A web-based online store built with Python, Django, HTML, CSS, JavaScript, and Bootstrap.

[Features](#-features) •
[Screenshots](#-screenshots) •
[Installation](#-installation) •
[Technologies](#-technologies-used) •
[Contact](#-contact)

</div>

---

## 📖 About the Project

**Django Store** is an e-commerce web application developed using the Django framework.

The project provides a foundation for an online shopping website, including product browsing, product details, user authentication, user profiles, and shopping cart functionality.

It was developed as a practical project to improve my skills in Python, Django, front-end development, database management, and Git.

## ✨ Features

- 🛒 **Product Browsing** — Explore available products.
- 🔍 **Product Details** — View detailed information about individual products.
- 💰 **Product Pricing** — Display product prices and discounts.
- 🖼️ **Product Images** — Display product images.
- 🔐 **User Authentication** — Log in and log out of user accounts.
- 👤 **User Profiles** — Manage user profile information.
- 🛍️ **Shopping Cart** — Add products to the cart when logged in.
- 🎨 **Responsive UI** — A clean interface designed with HTML, CSS, and Bootstrap.
- 🌿 **Simple Theme** — Switch to a simplified visual theme.
- 📰 **News Section** — Display news and announcements on the homepage.

## 📸 Screenshots

### 🏠 Home Page

![Django Store Homepage](screenshots/homepage.png)

*The homepage featuring the navigation bar, news section, theme toggle, and footer.*

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Django | Backend web framework |
| HTML5 | Page structure |
| CSS3 | Styling and layout |
| Bootstrap | Front-end components and styling |
| JavaScript | Interactive features |
| SQLite | Development database |
| Git | Version control |
| GitHub | Source code hosting |

## 📂 Project Structure

The project is organized into Django applications and templates.

```text
Store/
├── accounts/
├── selling/
│   └── static/
│       └── store/
│           └── css/
├── templates/
│   └── 404.html
├── screenshots/
│   └── homepage.png
├── manage.py
├── requirements.txt
└── README.md
```

*Note: This is a simplified overview. The exact directory structure may vary depending on the current project files.*

## ⚙️ Installation

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
![Django Store Homepage](screenshots/homepage.png)
```

### 2. Navigate to the Project Directory

```bash
cd Store
```

### 3. Create a Virtual Environment

```bash
python3 -m venv venv
```

### 4. Activate the Virtual Environment

**Linux / macOS:**

```bash
source venv/bin/activate
```

**Windows:**

```powershell
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Create an Administrator Account (Optional)

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 🔒 Security Notes

This project is intended for development and learning purposes.

Before deploying it to production:

- Set `DEBUG = False`.
- Configure `ALLOWED_HOSTS` for your domain.
- Keep the Django secret key out of public source code.
- Configure static and media file handling.
- Use a production-ready web server and review Django's deployment checklist.

## 🚀 Future Improvements

Potential improvements for future versions include:

- 🔎 Product search and filtering.
- 📦 Order management.
- 💳 Online payment integration.
- ⭐ Product ratings and reviews.
- 📱 Further improvements to mobile responsiveness.
- 🚀 Production deployment.

These are possible future enhancements, not claims about existing functionality.

## 🎯 What I Learned

Through this project, I practiced:

- Building web applications with Django.
- Working with Django models, views, URLs, and templates.
- Implementing user authentication and profile functionality.
- Managing product information and images.
- Building shopping cart functionality.
- Styling web pages with CSS and Bootstrap.
- Using Git and GitHub to manage project development.

## 👨‍💻 Developer

**Alireza Afshari**

Aspiring Python and Django Developer interested in web development and artificial intelligence.

- **GitHub:** [@alireza2040afshari-web](https://github.com/alireza2040afshari-web)
- **Project Repository:** [Django Store](https://github.com/alireza2040afshari-web/Store)

---

<div align="center">

**Built with Python and Django 🐍**

</div>
