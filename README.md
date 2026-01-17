# Blog & Education Platform

A professional Django-based blog and online education platform with admin management, course system, and modern design.

## 🚀 Features

- **User Authentication**: Custom user model with role-based access control (Admin/User)
- **Blog System**: Create, edit, publish blog posts with categories and tags
- **Course System**: Structured courses with modules and lessons (video/text)
- **Admin Dashboard**: Comprehensive dashboard with statistics and management tools
- **Responsive Design**: Modern, mobile-friendly interface
- **Markdown Support**: Write content in Markdown format
- **SEO Friendly**: Clean URLs and meta tags

## 📋 Requirements

- Python 3.10+
- PostgreSQL 12+
- pip and virtualenv

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd blog_education_platform
```

### 2. Create Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

Copy `.env.example` to `.env` and update with your settings:

```bash
cp .env.example .env
```

Edit `.env` file:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_NAME=blog_education_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your-password
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

### 5. Create Database

```bash
# PostgreSQL
createdb blog_education_db

# Or use pgAdmin/SQL
CREATE DATABASE blog_education_db;
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Collect Static Files (Optional for Development)

```bash
python manage.py collectstatic --noinput
```

### 9. Run Development Server

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000

## 📂 Project Structure

```
blog_education_platform/
├── config/                 # Main project settings
├── apps/                   # Django applications
│   ├── accounts/          # User authentication
│   ├── blogs/             # Blog system
│   ├── courses/           # Course system
│   ├── core/              # Core utilities
│   └── dashboard/         # Admin dashboard
├── templates/             # HTML templates
├── static/                # CSS, JS, Images
├── media/                 # User uploads
└── requirements.txt       # Python dependencies
```

## 🎯 Usage

### Admin Panel

1. Navigate to `/admin/`
2. Login with superuser credentials
3. Manage users, blogs, courses, and more

### Custom Dashboard

1. Login as admin user
2. Navigate to `/dashboard/`
3. View statistics and manage content

### Creating Content

**Blogs:**
- Go to `/blogs/create/` (admin only)
- Write content in Markdown
- Set category and tags
- Publish or save as draft

**Courses:**
- Use Django admin to create courses
- Add modules to organize lessons
- Add lessons (video or text)
- Publish when ready

## 🔐 User Roles

### Admin
- Create/Edit/Delete blogs and courses
- Access admin dashboard
- Manage users

### User (Regular)
- View published blogs and courses
- Enroll in courses
- View own profile

## 🎨 Customization

### Adding New Features

1. Create a new app:
```bash
python manage.py startapp myapp apps/myapp
```

2. Add to `INSTALLED_APPS` in `config/settings.py`
3. Create models, views, templates
4. Add URLs to `config/urls.py`

### Styling

- Edit CSS files in `static/css/`
- Modify templates in `templates/`
- Use Bootstrap 5 classes for consistency

## 🚀 Deployment

### Production Checklist

- [ ] Set `DEBUG=False` in `.env`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set strong `SECRET_KEY`
- [ ] Configure production database
- [ ] Set up static files serving (Nginx/Whitenoise)
- [ ] Configure media files storage
- [ ] Set up SSL certificate
- [ ] Configure email backend
- [ ] Run `python manage.py collectstatic`
- [ ] Set up logging

### Deployment with Gunicorn + Nginx

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn config.wsgi:application --bind 0.0.0.0:8000
```

Configure Nginx to proxy requests to Gunicorn.

## 🧪 Testing

```bash
# Run tests
python manage.py test

# Run specific app tests
python manage.py test apps.blogs
```

## 📝 License

This project is open source and available under the MIT License.

## 👥 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📧 Contact

For questions and support, please open an issue on GitHub.

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap
- PostgreSQL
- All contributors
