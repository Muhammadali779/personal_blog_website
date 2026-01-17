# 🚀 COMPLETE AI PROMPT: Django Blog & Education Platform

## 📋 OVERVIEW

You are an expert Django developer. Your task is to generate a **complete, production-ready Django Blog & Online Education Platform** with the following specifications:

- **Backend**: Django (latest stable version)
- **Database**: PostgreSQL
- **Architecture**: Clean, scalable, modular
- **Features**: Blog system, Course/Lesson system, Admin dashboard, Authentication
- **Frontend**: Modern, responsive HTML/CSS/JS (AI-generated design)

---

## 🎯 PROJECT REQUIREMENTS

### Core Features

1. **Authentication System**
   - Custom User model with roles (ADMIN, USER)
   - Registration and login
   - Role-based permissions
   - Password reset functionality

2. **Blog System**
   - Create, Read, Update, Delete (CRUD) operations
   - Categories and Tags
   - Markdown support
   - SEO-friendly URLs (slugs)
   - Author attribution
   - Published/Draft status

3. **Course & Lesson System**
   - Hierarchical structure: Course → Module → Lesson
   - Support for video URLs and text content
   - Ordered lessons within modules
   - Course enrollment tracking
   - Progress tracking

4. **Admin Dashboard**
   - Custom admin interface
   - Statistics (blogs count, courses count, users count)
   - Quick access to CRUD operations
   - Admin-only access control

5. **Frontend**
   - Modern, responsive design
   - Dark/Light mode toggle
   - Code syntax highlighting
   - SEO optimization
   - Social media links (GitHub, Telegram, YouTube, Gmail)

---

## 📁 REQUIRED PROJECT STRUCTURE

```
blog_education_platform/
│
├── manage.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
├── config/                         # Main Django settings
│   ├── __init__.py
│   ├── settings.py                # Environment-based config
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── apps/
│   │
│   ├── accounts/                  # User authentication
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py              # CustomUser with role field
│   │   ├── views.py               # Register, Login, Logout
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── permissions.py
│   │
│   ├── blogs/                     # Blog management
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py               # Customized admin
│   │   ├── apps.py
│   │   ├── models.py              # Blog, Category, Tag
│   │   ├── views.py               # List, Detail, CRUD
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── services.py            # Business logic
│   │
│   ├── courses/                   # Course system
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py              # Course, Module, Lesson
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── services.py
│   │
│   ├── core/                      # Shared utilities
│   │   ├── __init__.py
│   │   ├── models.py              # TimeStampedModel (abstract)
│   │   ├── context_processors.py
│   │   ├── utils.py
│   │   └── mixins.py
│   │
│   └── dashboard/                 # Admin dashboard
│       ├── __init__.py
│       ├── views.py               # Dashboard views
│       ├── urls.py
│       └── decorators.py          # Admin-only decorators
│
├── templates/
│   ├── base.html                  # Base template with navbar/footer
│   │
│   ├── components/
│   │   ├── navbar.html
│   │   ├── footer.html
│   │   └── sidebar.html
│   │
│   ├── pages/
│   │   ├── home.html              # Landing page
│   │   ├── about.html
│   │   ├── contact.html
│   │   │
│   │   ├── blogs/
│   │   │   ├── blog_list.html
│   │   │   ├── blog_detail.html
│   │   │   ├── blog_create.html
│   │   │   └── blog_edit.html
│   │   │
│   │   ├── courses/
│   │   │   ├── course_list.html
│   │   │   ├── course_detail.html
│   │   │   ├── lesson_view.html
│   │   │   ├── course_create.html
│   │   │   └── course_edit.html
│   │   │
│   │   └── auth/
│   │       ├── login.html
│   │       ├── register.html
│   │       └── password_reset.html
│   │
│   └── dashboard/
│       ├── index.html             # Admin dashboard home
│       ├── blog_manage.html
│       ├── course_manage.html
│       └── user_manage.html
│
├── static/
│   ├── css/
│   │   ├── style.css              # Main styles
│   │   ├── dark-mode.css
│   │   └── admin.css
│   │
│   ├── js/
│   │   ├── main.js                # Theme toggle, interactions
│   │   └── dashboard.js
│   │
│   ├── images/
│   └── icons/
│
└── media/                         # User uploads
    ├── blogs/
    │   └── images/
    └── courses/
        └── thumbnails/
```

---


```
# Django Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_NAME=blog_education_db
DATABASE_USER=postgres
DATABASE_PASSWORD=your-password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Email (optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```


## 🚀 IMPLEMENTATION INSTRUCTIONS

### Phase 1: Project Setup
1. Create Django project named `config`
2. Create all apps in `apps/` directory
3. Configure settings.py with environment variables
4. Set up PostgreSQL database
5. Create `.env` file from `.env.example`

### Phase 2: Models & Admin
1. Create all models as specified above
2. Run migrations
3. Customize Django admin for each model
4. Create superuser

### Phase 3: Views & URLs
1. Implement views for all CRUD operations
2. Add permission checks (admin-only for create/edit/delete)
3. Configure URL routing
4. Add pagination where needed

### Phase 4: Templates
1. Create base template with navbar and footer
2. Implement all page templates
3. Add forms with crispy-forms
4. Implement dark/light mode toggle

### Phase 5: Static Files
1. Create CSS files with responsive design
2. Add JavaScript for interactivity
3. Implement theme switcher
4. Add syntax highlighting for code blocks

### Phase 6: Testing & Polish
1. Test all CRUD operations
2. Test permissions
3. Verify responsive design
4. Check SEO metadata

---

## 📝 ADDITIONAL FEATURES TO IMPLEMENT

- [ ] Search functionality (blogs and courses)
- [ ] Filtering by category/tag
- [ ] Pagination (10 items per page)
- [ ] Breadcrumb navigation
- [ ] Related posts/courses
- [ ] Reading time estimate for blogs
- [ ] Course progress tracking
- [ ] Comment system (optional)
- [ ] Newsletter subscription (optional)
- [ ] Sitemap and robots.txt

---

## 🎯 SUCCESS CRITERIA

The generated project must:

1. ✅ Run without errors using `python manage.py runserver`
2. ✅ Have all migrations created and applied
3. ✅ Have working admin panel with customizations
4. ✅ Have functional CRUD operations for blogs and courses
5. ✅ Have role-based permissions (admin vs user)
6. ✅ Have responsive, modern frontend
7. ✅ Have dark/light mode toggle
8. ✅ Be ready for deployment (proper settings, requirements.txt)
9. ✅ Follow Django best practices
10. ✅ Have clean, commented code

---

## 🚀 DEPLOYMENT NOTES

For production deployment:

1. Set `DEBUG=False`
2. Configure proper `ALLOWED_HOSTS`
3. Use environment variables for secrets
4. Run `python manage.py collectstatic`
5. Set up Gunicorn + Nginx
6. Configure SSL certificate
7. Set up database backups

---

## 📚 DOCUMENTATION TO GENERATE

Please also create:

1. **README.md** with:
   - Project description
   - Installation instructions
   - Environment setup
   - How to run locally
   - Screenshots (placeholders)

2. **API Documentation** (if using DRF):
   - Endpoint list
   - Authentication methods
   - Request/response examples

3. **Deployment Guide**:
   - Step-by-step deployment instructions
   - Server requirements
   - Configuration checklist

---

## 💡 FINAL NOTE

Generate ALL files with complete, production-ready code. Do not use placeholders or "TODO" comments. Every function should be fully implemented. The project should be ready to run immediately after setup.

Focus on:
- **Clean architecture**
- **Scalability**
- **Security best practices**
- **Performance optimization**
- **User experience**

This project should be portfolio-worthy and demonstrate professional Django development skills.
