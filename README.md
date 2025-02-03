# Multilingual FAQ API

## Overview
This project is a backend application built with Django to manage multilingual Frequently Asked Questions (FAQs). It supports a WYSIWYG editor for rich-text answers, multi-language translations, caching for optimized performance, and a REST API for seamless integration.

## Features
- Store FAQs with multilingual support.
- Rich text editor (WYSIWYG) integration for answers.
- REST API with language selection via query parameters.
- Caching mechanism using Redis for efficient performance.
- Google Translate API integration for automatic translations.
- Admin panel for easy FAQ management.
- Unit tests for API and model validations.
- Docker support for easy deployment.

## Tech Stack
- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Caching**: Redis
- **WYSIWYG Editor**: django-ckeditor
- **Translation**: googletrans
- **Testing**: pytest
- **Containerization**: Docker, Docker Compose

## Installation
### Prerequisites
- Python 3.9+
- PostgreSQL
- Redis
- Docker (optional for containerization)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/tusharthite15/BharatFD
   cd BharatFD/faq_project
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Configure environment variables:
   - Create a `.env` file in the project root and add the following:
     ```ini
     SECRET_KEY=your_secret_key
     DEBUG=True
     DATABASE_URL=postgres://user:password@localhost:5432/dbname
     REDIS_URL=redis://localhost:6379/0
     GOOGLE_TRANSLATE_API_KEY=your_api_key
     ```
5. Apply database migrations:
   ```sh
   python manage.py migrate
   ```
6. Create a superuser for the admin panel:
   ```sh
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints
### Fetch all FAQs (default language: English)
```sh
GET /api/faqs/
```

### Fetch FAQs in Hindi
```sh
GET /api/faqs/?lang=hi
```

### Fetch FAQs in Bengali
```sh
GET /api/faqs/?lang=bn
```

### Create a new FAQ (Admin required)
```sh
POST /api/faqs/
Content-Type: application/json
{
  "question": "What is Django?",
  "answer": "Django is a high-level Python Web framework."
}
```

## Admin Panel
Access the admin panel at:
```sh
http://localhost:8000/admin/
```
Login using the superuser credentials created earlier.

## Running Tests
```sh
pytest
```

## Docker Setup (Optional)
1. Build and start the containers:
   ```sh
   docker-compose up --build
   ```
2. The application should be running at:
   ```sh
   http://localhost:8000
   ```

## Git Best Practices
- Follow conventional commits:
  - `feat: Add multilingual FAQ model`
  - `fix: Improve translation caching`
  - `docs: Update README with API examples`
- Use meaningful commit messages.
- Push changes to a feature branch and merge via pull requests.

## Deployment (Optional)
You can deploy the application to **Heroku** or **AWS** using Docker and environment variables for configuration.

## Contribution Guidelines
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m "feat: Add new feature"`
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request.

## License
This project is licensed under the MIT License.

---
### Contact
For any queries, open an issue in the repository or contact the maintainer.

