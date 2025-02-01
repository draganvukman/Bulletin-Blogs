# Flask Blog Website

https://bulletin-blogs.onrender.com

A dynamic blog website built using Flask and PostgreSQL. The application supports categorized blogs (e.g., health, technology) and features modern HTML, CSS, and JavaScript for a responsive user interface. Users can view blogs categorized by topic, and the blog content is fetched from a PostgreSQL database.

## Features

- **Dynamic Blog Content**: Blogs are stored in a PostgreSQL database and dynamically rendered on relevant pages.
- **Category-based Navigation**: View blogs by category (e.g., Health, Technology).
- **Responsive Design**: Modern and responsive layout using HTML, CSS, and JavaScript.
- **Modular Architecture**: Separation of concerns with routes, models, and templates in separate files.

---

## Project Structure

blog_website/ ├── app/ │ ├── init.py # Application factory and initialization │ ├── models.py # Database models │ ├── forms.py # Flask-WTF forms │ ├── routes/ │ │ ├── init.py │ │ ├── page_routes.py # Routes for static pages and categories │ ├── templates/ │ │ ├── base.html # Base template │ │ ├── home.html # Home page │ │ ├── category.html # Category pages │ ├── static/ │ │ ├── css/ │ │ │ └── style.css # CSS for styling │ │ ├── js/ │ │ │ └── script.js # JavaScript for interactivity ├── config.py # Application configuration ├── run.py # Entry point for running the application ├── requirements.txt # Python dependencies └── README.md

## Project documentation

---

## Requirements

- Python 3.8 or higher
- PostgreSQL
- Flask and related libraries

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/flask-blog-website.git
cd flask-blog-website
```
