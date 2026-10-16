# Smart Mind Academy

**A bilingual educational website built with Django for presenting academic subjects and student learning resources in English and Bangla.**

Smart Mind Academy is a web project designed around an online learning experience. It includes separate English and Bangla page templates, subject overview pages, and a student resources page.

## Overview

The current codebase includes:

- **Bilingual pages:** English and Bangla home, subjects, and resources pages.
- **Subject directory:** Overview cards for school subjects such as Physics, Chemistry, Biology, Mathematics, English, Bangla, Bangladesh and Global Studies, and ICT.
- **Student resources page:** A page intended to provide access to textbooks and class notes.
- **Shared page layouts:** Separate reusable base templates for the English and Bangla interfaces.
- **Django data models:** Models for student admission details and uploaded book resources are defined in the `core` app.

> **Project status:** This repository contains the core website pages and supporting Django code. Some visible buttons and resource links are placeholders, and the admission workflow is not currently connected to the URL configuration. Review and complete these parts before presenting the project as a fully functional admission or resource-download platform.

## Tech Stack

- **Python**
- **Django 6.0.6** (as specified in the project settings and dependency file)
- **SQLite** for the default local database configuration
- **HTML and CSS** for page templates and styling
- **Google Fonts** — Inter for English pages and Hind Siliguri for Bangla pages
- **WhiteNoise** for static-file support in deployment configurations
- **Gunicorn** as a WSGI HTTP server dependency

## Pages

| Page | URL | Description |
|---|---|---|
| English home | `/` | Welcome page for the learning platform |
| Bangla home | `/bn/` | Bangla welcome page |
| English subjects | `/subjects/` | Overview of school subjects |
| Bangla subjects | `/bn/subjects/` | Bangla subject overview |
| English resources | `/resources/` | Student resource page |
| Bangla resources | `/bn/resources/` | Bangla student resource page |
| Django admin | `/admin/` | Django administration route |

## Project Structure

```text
smart_mind_academy/
├── manage.py
├── requirements.txt
├── smart_mind_academy/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── core/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── AlgoLAa.cpp
│   └── templates/
│       ├── base_en.html
│       ├── base_bn.html
│       ├── home_en.html
│       ├── home_bn.html
│       ├── subjects_en.html
│       ├── subjects_bn.html
│       ├── resources_en.html
│       └── resources_bn.html
└── static/
    └── logo.png
```

## Getting Started

### Prerequisites

- Python compatible with the dependencies in `requirements.txt`
- `pip`
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/FardinShuvro/smartmindacademy.git
cd smartmindacademy
```

If the repository's canonical URL differs, use the clone URL shown by GitHub's **Code** button.

### 2. Create and activate a virtual environment

**Windows (Command Prompt):**

```bat
python -m venv .venv
.venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Prepare the database

```bash
python manage.py makemigrations core
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

> These are standard Django development steps. If a command fails, check the installed Python version, dependency versions, and any project-specific configuration.

## Data Models

The `core` app currently defines:

- **`StudentAdmission`** — fields for a student's name, email, phone, grade, and submission timestamp.
- **`BookResource`** — a title and uploaded PDF file for a learning resource.

The presence of these models does not by itself mean that admission submissions or file downloads are fully implemented in the website.

## Current Limitations / Next Steps

Potential improvements for the next iteration:

- Connect the admission form to a working page, correct its field mapping, and add a success page.
- Replace placeholder navigation and resource links with working destinations.
- Add resource upload/download handling and permissions.
- Add database migrations and automated tests to version control.
- Add screenshots of the website to this README.
- Review deployment settings, allowed hosts, secret-key handling, and static/media file configuration before production deployment.
- Add accessibility checks and responsive navigation testing.

## Screenshots

Screenshots can be added here once captured, for example:

```markdown
![English home page](docs/screenshots/home-en.png)
![Bangla home page](docs/screenshots/home-bn.png)
![Subjects page](docs/screenshots/subjects.png)
```

## Contributing

Suggestions and improvements are welcome. For a personal or academic project, you can open an issue describing a bug or proposed enhancement before submitting changes.

## License

No license file was included in the supplied project archive. Add a `LICENSE` file before describing this project as open source or specifying reuse permissions.

---

**Developed as an educational web project using Python and Django.**
