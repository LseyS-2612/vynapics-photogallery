# Vynapics Gallery - Visual Storytelling Platform

**Vynapics** is a curated photo gallery application built with **Django**. It serves as a visual storytelling platform where users can share, manage, and discover high-quality photography. The project features a responsive masonry layout, a dynamic hero section with cinematic transitions, and a full user authentication system.

---

## 🚀 Features

### Core Functionality
* **User Authentication:** Secure registration, login, and logout system.
* **CRUD Operations:** Users can **Create** (upload), **Read** (view), **Update** (edit details), and **Delete** their own photos.
* **Dynamic Hero Section:** A JavaScript-powered slideshow featuring the latest uploads with a "fade-to-black" cinematic effect.
* **Category Filtering:** Filter visuals by categories (e.g., Architecture, Black and White, Film Look).
* **Lightbox & Download:** Click on photos to view them in full resolution with a direct download option.

### Technical Highlights
* **Backend:** Powered by Python & Django Framework.
* **Database:** SQLite for data persistence.
* **Frontend:** HTML5, CSS3 (Flexbox & CSS Grid), and Vanilla JavaScript.
* **Design:** Custom "Masonry" layout similar to Pinterest; Fully responsive UI.
* **Containerization:** Docker support included for easy deployment.

---

## 🛠️ Tech Stack

* **Language:** Python 3.11+
* **Framework:** Django 5.x
* **Image Processing:** Pillow
* **Containerization:** Docker
* **Version Control:** Git

---

## 📦 Installation & Setup

### Method 1: Standard Installation (Local)

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/LseyS-2612/vynapics-photogallery.git](https://github.com/LseyS-2612/vynapics-photogallery.git)
    cd vynapics-photogallery
    ```

2.  **Create and activate a virtual environment (Optional but recommended):**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (Admin):**
    Since the database is excluded from the repository for security, you need to create an initial admin user.
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the server:**
    ```bash
    python manage.py runserver
    ```
    Access the app at: `http://127.0.0.1:8000/`

---

### Method 2: Running with Docker 🐳

If you have Docker installed, you can run the application without installing Python dependencies manually.

1.  **Build the Docker image:**
    ```bash
    docker build -t vynapics-app .
    ```

2.  **Run the container:**
    ```bash
    docker run -p 8000:8000 vynapics-app
    ```
    Access the app at: `http://localhost:8000/`

---

## 📸 Screenshots


<img width="1918" height="729" alt="Screenshot 2026-01-12 181309" src="https://github.com/user-attachments/assets/22638330-f5a3-4fef-a444-70efb3d09ecb" />
<img width="1914" height="826" alt="Screenshot 2026-01-12 181319" src="https://github.com/user-attachments/assets/ff926377-637d-41da-bb95-8b8b62afd9b1" />

---

## 📝 License

This project was developed for the **Technologies of Internet Applications** course.
© 2026 Vynapics Platform. All rights reserved.
