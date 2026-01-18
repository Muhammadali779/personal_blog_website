# 🎓 Personal Blog & Online Courses Platform

> A modern, full-featured platform for sharing technical blog posts and structured online courses with video lessons.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Django](https://img.shields.io/badge/Django-4.2+-green.svg)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-blue.svg)](https://www.postgresql.org/)

---

## 👨‍💻 About the Developer

**Name:** Muhammadali  
**University:** Samarkand branch of Tashkent University of Information Technologies named after Muhammad al-Khwarizmi  
**Major:** Software Engineering

### 💪 Technical Skills
- **Backend:** Python, Django, FastAPI
- **Database:** PostgreSQL
- **Bot Development:** Aiogram (Telegram Bots)
- **Programming:** C++

---

## 📖 Table of Contents

1. [Project Overview](#-project-overview)
2. [Features](#-features)
3. [Technology Stack](#-technology-stack)
4. [Project Structure](#-project-structure)
5. [Frontend Architecture](#-frontend-architecture)
6. [Backend Architecture](#-backend-architecture)
7. [Database Design](#-database-design)
8. [User Roles & Permissions](#-user-roles--permissions)
9. [Pages & Components](#-pages--components)
10. [Setup & Installation](#-setup--installation)
11. [Development Workflow](#-development-workflow)
12. [Deployment Guide](#-deployment-guide)
13. [Security Considerations](#-security-considerations)
14. [Performance Optimization](#-performance-optimization)
15. [Future Enhancements](#-future-enhancements)

---

## 🎯 Project Overview

This platform serves three main purposes:

1. **📝 Technical Blog** - Share in-depth articles, tutorials, and technical insights
2. **🎓 Online Courses** - Publish structured video-based learning courses with lessons
3. **👤 Portfolio** - Showcase personal projects, skills, and professional journey

### Key Objectives

- ✅ Provide a clean, modern reading experience for blog content
- ✅ Deliver structured learning through organized courses and lessons
- ✅ Maintain complete content control (owner/admin only)
- ✅ Ensure responsive design across all devices
- ✅ Support both light and dark themes
- ✅ Optimize for performance and SEO

---

## ✨ Features

### Core Features
- 📱 **Fully Responsive Design** - Optimized for mobile, tablet, and desktop
- 🌓 **Dark/Light Mode** - User preference with local storage persistence
- 📝 **Rich Blog System** - Articles with code blocks, syntax highlighting, and reading time
- 🎥 **Video-Based Courses** - Structured lessons with video + article content
- 👥 **Role-Based Access** - Owner, Admin, and User permissions
- 📧 **Contact System** - Built-in contact form with validation
- 🔍 **Search Functionality** - Find blogs and courses easily (future)
- 📊 **Analytics Dashboard** - Content management interface for admins

### User Features
- Read technical blog posts with code examples
- Browse and enroll in online courses
- Watch video lessons with supplementary articles
- Contact the platform owner
- Toggle between light/dark themes
- Responsive navigation experience

### Admin Features
- Create, edit, and delete blog posts
- Manage courses and lessons
- Upload video content
- View contact form submissions
- Monitor user engagement (future)
- Manage user permissions

---

## 🛠 Technology Stack

### Frontend
| Technology | Purpose | Version |
|------------|---------|---------|
| HTML5 | Semantic structure | Latest |
| CSS3 | Modern styling, animations | Latest |
| Vanilla JavaScript | Interactivity, dynamic features | ES6+ |
| Django Templates | Template inheritance, server-side rendering | 4.2+ |

### Backend (Conceptual - To Be Implemented)
| Technology | Purpose | Version |
|------------|---------|---------|
| Django | Web framework, ORM, admin | 4.2+ |
| Python | Backend logic | 3.11+ |
| PostgreSQL | Primary database | 15+ |
| Django REST Framework | API endpoints (optional) | 3.14+ |

### DevOps & Deployment (Future)
| Tool | Purpose |
|------|---------|
| Git | Version control |
| GitHub Actions | CI/CD pipeline |
| Docker | Containerization |
| Nginx | Reverse proxy |
| Gunicorn | WSGI server |
| AWS S3 / Cloudinary | Media storage |

---

## 📁 Project Structure

```
blog-courses-platform/
│
├── 📂 backend/                    # Django backend (to be implemented)
│   ├── 📂 config/                # Project configuration
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── 📂 apps/
│   │   ├── 📂 users/            # User management
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── serializers.py
│   │   │   └── urls.py
│   │   │
│   │   ├── 📂 blogs/            # Blog system
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── admin.py
│   │   │   └── urls.py
│   │   │
│   │   ├── 📂 courses/          # Courses & lessons
│   │   │   ├── models.py
│   │   │   ├── views.py
│   │   │   ├── admin.py
│   │   │   └── urls.py
│   │   │
│   │   └── 📂 contacts/         # Contact form
│   │       ├── models.py
│   │       ├── views.py
│   │       └── forms.py
│   │
│   └── 📂 media/                # User uploaded files
│
├── 📂 frontend/                  # Frontend UI (current implementation)
│   ├── 📂 templates/
│   │   ├── base.html            # Base template with navbar/footer
│   │   ├── home.html            # Landing page
│   │   ├── about.html           # About me page
│   │   ├── contact.html         # Contact form
│   │   │
│   │   ├── 📂 blogs/
│   │   │   ├── blog_list.html
│   │   │   └── blog_detail.html
│   │   │
│   │   ├── 📂 courses/
│   │   │   ├── course_list.html
│   │   │   ├── course_detail.html
│   │   │   └── lesson_detail.html
│   │   │
│   │   └── 📂 dashboard/        # Admin interface
│   │       ├── dashboard.html
│   │       ├── create_blog.html
│   │       └── create_course.html
│   │
│   └── 📂 static/
│       ├── 📂 css/
│       │   ├── base.css         # Global styles
│       │   ├── components.css   # Reusable components
│       │   ├── pages.css        # Page-specific styles
│       │   └── themes.css       # Light/dark theme variables
│       │
│       ├── 📂 js/
│       │   ├── main.js          # Core functionality
│       │   ├── theme.js         # Dark/light mode toggle
│       │   ├── code-copy.js     # Copy code button
│       │   └── animations.js    # Smooth transitions
│       │
│       └── 📂 images/
│           ├── logo.svg
│           ├── hero-bg.jpg
│           └── avatars/
│
├── 📂 docs/                      # Documentation
│   ├── API.md
│   ├── DEPLOYMENT.md
│   └── CONTRIBUTING.md
│
├── .env.example                  # Environment variables template
├── .gitignore
├── requirements.txt              # Python dependencies
├── docker-compose.yml            # Docker configuration
└── README.md                     # This file
```

---

## 🎨 Frontend Architecture

### Template Inheritance System

```
base.html (Parent)
├── Navbar Component
├── {% block content %}
│   ├── home.html
│   ├── about.html
│   ├── blog_list.html
│   ├── blog_detail.html
│   ├── course_list.html
│   ├── course_detail.html
│   └── lesson_detail.html
└── Footer Component
```

### Component Breakdown

#### 1. **Navigation Bar** (`navbar` in base.html)
- Fixed position on scroll
- Responsive hamburger menu for mobile
- Active state indication
- Dark/light mode toggle
- Links: Home, Blogs, Courses, About, Contact

#### 2. **Footer** (`footer` in base.html)
- Short bio section
- Social media links (Telegram, GitHub, YouTube, Gmail)
- Copyright information
- "Contact With Me" section

#### 3. **Blog Card Component**
```html
<div class="blog-card">
  <h3 class="blog-title">{{ title }}</h3>
  <div class="blog-meta">
    <span class="reading-time">{{ reading_time }} min read</span>
    <span class="date">{{ created_at }}</span>
  </div>
  <p class="blog-preview">{{ preview }}</p>
  <a href="#" class="btn-read-more">Read More</a>
</div>
```

#### 4. **Course Card Component**
```html
<div class="course-card">
  <div class="course-thumbnail">
    <img src="{{ thumbnail }}" alt="{{ title }}">
  </div>
  <h3 class="course-title">{{ title }}</h3>
  <p class="course-description">{{ description }}</p>
  <div class="course-meta">
    <span class="lessons-count">{{ lessons_count }} lessons</span>
  </div>
  <a href="#" class="btn-view-course">View Course</a>
</div>
```

#### 5. **Code Block Component**
```html
<div class="code-block">
  <div class="code-header">
    <span class="language">{{ language }}</span>
    <button class="btn-copy">Copy</button>
  </div>
  <pre><code class="language-{{ language }}">{{ code }}</code></pre>
</div>
```

### JavaScript Modules

#### `theme.js` - Dark/Light Mode
```javascript
// Functionality:
- Read theme preference from localStorage
- Toggle between light/dark mode
- Save preference to localStorage
- Apply theme class to <body>
```

#### `code-copy.js` - Copy Code Functionality
```javascript
// Functionality:
- Add copy button to all code blocks
- Copy code to clipboard on click
- Show "Copied!" feedback
- Reset button text after 2s
```

#### `main.js` - Core Features
```javascript
// Functionality:
- Mobile menu toggle
- Smooth scrolling
- Form validation
- Loading states
- Error handling
```

### CSS Architecture

**Variables-Based Design System:**
```css
:root {
  /* Colors */
  --color-primary: #6366f1;
  --color-secondary: #8b5cf6;
  --color-accent: #ec4899;
  
  /* Light Mode */
  --bg-primary: #ffffff;
  --bg-secondary: #f9fafb;
  --text-primary: #1f2937;
  --text-secondary: #6b7280;
  
  /* Dark Mode */
  --bg-primary-dark: #111827;
  --bg-secondary-dark: #1f2937;
  --text-primary-dark: #f9fafb;
  --text-secondary-dark: #d1d5db;
  
  /* Spacing */
  --spacing-xs: 0.5rem;
  --spacing-sm: 1rem;
  --spacing-md: 1.5rem;
  --spacing-lg: 2rem;
  --spacing-xl: 3rem;
  
  /* Typography */
  --font-sans: 'Inter', system-ui, sans-serif;
  --font-mono: 'Fira Code', monospace;
}
```

**Responsive Breakpoints:**
```css
/* Mobile First Approach */
/* Mobile: default (0-640px) */
/* Tablet: 640px+ */
/* Desktop: 1024px+ */
/* Large Desktop: 1280px+ */
```

---

## 🏗 Backend Architecture (Conceptual)

### Django Apps Structure

#### **1. users/** - User Management & Authentication
```python
# models.py
- CustomUser (extends AbstractUser)
  - role (owner/admin/user)
  - bio
  - avatar
  - social_links (JSON field)
  
# views.py
- User registration
- Login/Logout
- Profile management
- Role assignment (owner only)
```

#### **2. blogs/** - Blog System
```python
# models.py
- Blog
  - title
  - slug (auto-generated)
  - content (rich text)
  - reading_time (auto-calculated)
  - preview (first 200 chars)
  - author (FK to User)
  - created_at
  - updated_at
  - is_published
  
# views.py
- BlogListView (public)
- BlogDetailView (public)
- BlogCreateView (admin only)
- BlogUpdateView (admin only)
- BlogDeleteView (admin only)
```

#### **3. courses/** - Course Management
```python
# models.py
- Course
  - title
  - slug
  - description
  - thumbnail
  - created_at
  - is_published
  
- Lesson
  - course (FK to Course)
  - title
  - order (for sequencing)
  - video_url
  - content (article text)
  - duration (in minutes)
  - created_at
  
# views.py
- CourseListView (public)
- CourseDetailView (public)
- LessonDetailView (public)
- CourseCreateView (admin only)
- LessonCreateView (admin only)
```

#### **4. contacts/** - Contact Form
```python
# models.py
- ContactMessage
  - name
  - email
  - subject
  - message
  - is_read
  - created_at
  
# views.py
- ContactFormView (public)
- ContactListView (admin only)
```

### URL Structure
```
/                          → Home page
/blogs/                    → Blog list
/blogs/<slug>/             → Blog detail
/courses/                  → Course list
/courses/<slug>/           → Course detail
/courses/<slug>/<lesson>/  → Lesson detail
/about/                    → About me
/contact/                  → Contact form
/dashboard/                → Admin dashboard (login required)
```

### Authentication Flow
```
1. User visits protected page
2. Django checks authentication
3. If not authenticated → redirect to login
4. After login → check user role
5. Grant/deny access based on role
```

---

## 🗄 Database Design

### Entity Relationship Diagram

```
┌─────────────┐         ┌─────────────┐
│    User     │         │    Blog     │
├─────────────┤         ├─────────────┤
│ id (PK)     │───1:N───│ id (PK)     │
│ username    │         │ title       │
│ email       │         │ slug        │
│ password    │         │ content     │
│ role        │         │ author_id   │
│ bio         │         │ reading_time│
│ avatar      │         │ created_at  │
└─────────────┘         └─────────────┘

┌─────────────┐         ┌─────────────┐
│   Course    │         │   Lesson    │
├─────────────┤         ├─────────────┤
│ id (PK)     │───1:N───│ id (PK)     │
│ title       │         │ course_id   │
│ slug        │         │ title       │
│ description │         │ order       │
│ thumbnail   │         │ video_url   │
│ created_at  │         │ content     │
└─────────────┘         │ duration    │
                        └─────────────┘

┌──────────────────┐
│ ContactMessage   │
├──────────────────┤
│ id (PK)          │
│ name             │
│ email            │
│ subject          │
│ message          │
│ is_read          │
│ created_at       │
└──────────────────┘
```

### Database Tables (Detailed)

#### **users**
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Auto-increment ID |
| username | VARCHAR(150) | UNIQUE, NOT NULL | Username for login |
| email | VARCHAR(254) | UNIQUE, NOT NULL | Email address |
| password | VARCHAR(128) | NOT NULL | Hashed password |
| role | VARCHAR(20) | DEFAULT 'user' | owner/admin/user |
| bio | TEXT | NULL | Short biography |
| avatar | VARCHAR(200) | NULL | Profile image path |
| social_links | JSON | NULL | Social media links |
| is_active | BOOLEAN | DEFAULT TRUE | Account status |
| created_at | TIMESTAMP | DEFAULT NOW() | Registration date |

#### **blogs**
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Auto-increment ID |
| title | VARCHAR(200) | NOT NULL | Blog post title |
| slug | VARCHAR(200) | UNIQUE, NOT NULL | URL-friendly title |
| content | TEXT | NOT NULL | Full blog content |
| preview | VARCHAR(300) | NULL | Short preview (auto) |
| reading_time | INTEGER | NULL | Minutes to read (auto) |
| author_id | INTEGER | FK → users.id | Author reference |
| is_published | BOOLEAN | DEFAULT FALSE | Publication status |
| created_at | TIMESTAMP | DEFAULT NOW() | Creation date |
| updated_at | TIMESTAMP | AUTO UPDATE | Last modified date |

#### **courses**
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Auto-increment ID |
| title | VARCHAR(200) | NOT NULL | Course title |
| slug | VARCHAR(200) | UNIQUE, NOT NULL | URL-friendly title |
| description | TEXT | NOT NULL | Course description |
| thumbnail | VARCHAR(200) | NULL | Course image path |
| is_published | BOOLEAN | DEFAULT FALSE | Publication status |
| created_at | TIMESTAMP | DEFAULT NOW() | Creation date |

#### **lessons**
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Auto-increment ID |
| course_id | INTEGER | FK → courses.id | Parent course |
| title | VARCHAR(200) | NOT NULL | Lesson title |
| order | INTEGER | NOT NULL | Lesson sequence |
| video_url | VARCHAR(500) | NULL | Video source URL |
| content | TEXT | NOT NULL | Article content |
| duration | INTEGER | NULL | Video duration (min) |
| created_at | TIMESTAMP | DEFAULT NOW() | Creation date |

**Constraint:** UNIQUE(course_id, order) - Prevents duplicate lesson orders

#### **contact_messages**
| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| id | INTEGER | PRIMARY KEY | Auto-increment ID |
| name | VARCHAR(100) | NOT NULL | Sender name |
| email | VARCHAR(254) | NOT NULL | Sender email |
| subject | VARCHAR(200) | NOT NULL | Message subject |
| message | TEXT | NOT NULL | Message content |
| is_read | BOOLEAN | DEFAULT FALSE | Read status |
| created_at | TIMESTAMP | DEFAULT NOW() | Submission date |

### Indexes (for Performance)
```sql
-- Blogs
CREATE INDEX idx_blogs_slug ON blogs(slug);
CREATE INDEX idx_blogs_author ON blogs(author_id);
CREATE INDEX idx_blogs_published ON blogs(is_published, created_at DESC);

-- Courses
CREATE INDEX idx_courses_slug ON courses(slug);
CREATE INDEX idx_courses_published ON courses(is_published, created_at DESC);

-- Lessons
CREATE INDEX idx_lessons_course ON lessons(course_id, order);

-- Contact Messages
CREATE INDEX idx_contacts_read ON contact_messages(is_read, created_at DESC);
```

---

## 👥 User Roles & Permissions

### Permission Matrix

| Feature | Owner | Admin | User |
|---------|-------|-------|------|
| **Blogs** |
| View published blogs | ✅ | ✅ | ✅ |
| Create blog | ✅ | ✅ | ❌ |
| Edit blog | ✅ | ✅ | ❌ |
| Delete blog | ✅ | ✅ | ❌ |
| **Courses** |
| View courses | ✅ | ✅ | ✅ |
| Create course | ✅ | ✅ | ❌ |
| Edit course | ✅ | ✅ | ❌ |
| Delete course | ✅ | ✅ | ❌ |
| **Lessons** |
| View lessons | ✅ | ✅ | ✅ |
| Create lesson | ✅ | ✅ | ❌ |
| Edit lesson | ✅ | ✅ | ❌ |
| Delete lesson | ✅ | ✅ | ❌ |
| **Users** |
| View users | ✅ | ❌ | ❌ |
| Create admin | ✅ | ❌ | ❌ |
| Remove admin | ✅ | ❌ | ❌ |
| Ban user | ✅ | ✅ | ❌ |
| **Contact** |
| Send message | ✅ | ✅ | ✅ |
| View messages | ✅ | ✅ | ❌ |
| Mark as read | ✅ | ✅ | ❌ |

### Role Hierarchy
```
Owner (Superuser)
  ↓
Admin (Staff)
  ↓
User (Default)
```

---

## 📄 Pages & Components

### 🏠 **Home Page**

**Layout:**
```
┌─────────────────────────────┐
│   Hero Section              │
│   - Name                    │
│   - Tagline                 │
│   - CTA Button              │
└─────────────────────────────┘

┌─────────────────────────────┐
│   About Preview (Short)     │
│   - 3-4 lines bio           │
│   - "Read More" button      │
└─────────────────────────────┘

┌─────────────────────────────┐
│   Latest Blog Posts (3)     │
│   ┌─────┐ ┌─────┐ ┌─────┐  │
│   │Post1│ │Post2│ │Post3│  │
│   └─────┘ └─────┘ └─────┘  │
└─────────────────────────────┘
```

**Key Features:**
- Clean, minimal hero with gradient background
- Short bio preview (not full about page)
- Only 3 most recent blog posts
- **No courses section** (courses only in /courses)

---

### 📝 **Blogs Section**

#### Blog List Page (`/blogs/`)
```
┌──────────────────────────────────┐
│  📝 Technical Blog               │
│  Insights, tutorials & thoughts  │
└──────────────────────────────────┘

┌──────────┐  ┌──────────┐  ┌──────────┐
│ Blog 1   │  │ Blog 2   │  │ Blog 3   │
│ 5 min    │  │ 8 min    │  │ 12 min   │
│ Preview  │  │ Preview  │  │ Preview  │
│ Read → │  │ Read →  │  │ Read →  │
└──────────┘  └──────────┘  └──────────┘

     [Pagination: ← 1 2 3 4 5 →]
```

**Features:**
- Grid layout (3 columns on desktop)
- Reading time estimation
- 200-character preview
- Pagination (9 posts per page)

#### Blog Detail Page (`/blogs/<slug>/`)
```
┌──────────────────────────────────┐
│  Blog Title                      │
│  👤 Author | 📅 Date | ⏱ 8 min  │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│  Blog Content                    │
│  - Paragraphs                    │
│  - Images                        │
│  - Code blocks with copy button  │
│  - Lists                         │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│  💬 Share on social media        │
└──────────────────────────────────┘
```

**Features:**
- Clean reading layout (max-width: 800px)
- Syntax-highlighted code blocks
- Copy-to-clipboard for code
- Share buttons (future)

---

### 🎓 **Courses Section**

#### Course List Page (`/courses/`)
```
┌──────────────────────────────────┐
│  🎓 Online Courses               │
│  Structured learning paths       │
└──────────────────────────────────┘

┌────────┐ ┌────────┐ ┌────────┐
│Course 1│ │Course 2│ │Course 3│
│Thumb   │ │Thumb   │ │Thumb   │
│Title   │ │Title   │ │Title   │
│12 less │ │8 less  │ │15 less │
│View → ││View → ││View → │
└────────┘ └────────┘ └────────┘

  [Pagination: 6 courses per page]
```

**Features:**
- Grid layout (2-3 columns)
- Thumbnail images
- Lesson count
- Pagination

#### Course Detail Page (`/courses/<slug>/`)
```
┌──────────────────────────────────┐
│  Course Title                    │
│  Course Description              │
│  📚 12 Lessons | ⏱ 3 hours      │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│  Lessons:                        │
│  1. Introduction to Topic        │
│  2. Basic Concepts              │
│  3. Practical Examples          │
│  ...                            │
└──────────────────────────────────┘
```

#### Lesson Detail Page (`/courses/<slug>/<lesson>/`)
```
┌──────────────────────────────────┐
│  🎥 Video Player                 │
│     [Embedded YouTube/Custom]    │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│  📖 Lesson Article               │
│  - Introduction                  │
│  - Theory explanation            │
│  - Code examples                 │
│  - Practice exercises            │
└──────────────────────────────────┘

[← Previous Lesson] [Next Lesson →]
```

**Features:**
- Video player (YouTube embed or custom)
- Article content below video
- Code blocks with syntax highlighting
- Previous/Next navigation

---

### 👤 **About Page** (`/about/`)
```
┌──────────────────────────────────┐
│  Profile Photo                   │
│  Muhammadali                     │
│  Dasturiy Injiniring Student     │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│  🎓 Education                    │
│  Muhammad al-Xorazmiy nomidagi   │
│  Toshkent Axborot Texnologiyalari│
│  Universiteti Samarqand filliali │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│  💻 Skills                       │
│  Python | Django | FastAPI       │
│  PostgreSQL | Aiogram | C++      │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│  📫 Connect                      │
│  [Telegram] [GitHub] [YouTube]   │
└──────────────────────────────────┘
```

---

### 📧 **Contact Page** (`/contact/`)
```
┌──────────────────────────────────┐
│  Get In Touch                    │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│  Name:     [____________]        │
│  Email:    [____________]        │
│  Subject:  [____________]        │
│  Message:  [____________]        │
│           [____________]        │
│           [Send Message]         │
└──────────────────────────────────┘

┌──────────────────────────────────┐
│  Or reach me on:                 │
│  📧 email@example.com            │
│  💬 @telegram                    │
│  🐙 GitHub                       │
└──────────────────────────────────┘
```

**Features:**
- Form validation (client + server)
- Success/error messages
- Direct social links
- CSRF protection

---

## 🚀 Setup & Installation

### Prerequisites
```bash
- Python 3.11+
- PostgreSQL 15+
- Node.js 18+ (for future asset bundling)
- Git
```

### Local Development Setup

#### 1. Clone Repository
```bash
git clone https://github.com/yourusername/blog-courses-platform.git
cd blog-courses-platform
```

#### 2. Create Virtual Environment
```bash
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Environment Variables
```bash
cp .env.example .env

# Edit .env with your settings:
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
ALLOWED_HOSTS=localhost,127.0.0.1
```

#### 5. Database Setup
```bash
# Create PostgreSQL database
createdb blog_courses_db

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (owner)
python manage.py createsuperuser
```

#### 6. Load Sample Data (Optional)
```bash
python manage.py loaddata fixtures/sample_data.json
```

#### 7. Run Development Server
```bash
python manage.py runserver
```

Visit: `http://localhost:8000`

---

## 💻 Development Workflow

### Creating a New Blog Post

**Via Django Admin:**
```
1. Login to /admin/
2. Navigate to Blogs → Add Blog
3. Fill in: Title, Content, Reading Time
4. Save as Draft or Publish
```

**Via Code:**
```python
from apps.blogs.models import Blog

blog = Blog.objects.create(
    title="My New Blog Post",
    content="Blog content here...",
    author=request.user,
    reading_time=5,
    is_published=True
)
```

### Creating a New Course

```python
from apps.courses.models import Course, Lesson

# Create course
course = Course.objects.create(
    title="Django Masterclass",
    description="Learn Django from scratch",
    is_published=True
)

# Add lessons
Lesson.objects.create(
    course=course,
    title="Introduction to Django",
    order=1,
    video_url="https://youtube.com/watch?v=...",
    content="Lesson article content...",
    duration=15
)
```

### Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test apps.blogs

# Coverage report
coverage run --source='.' manage.py test
coverage report
```

---

## 🌐 Deployment Guide

### Production Checklist

- [ ] Set `DEBUG=False` in production
- [ ] Configure proper `SECRET_KEY`
- [ ] Set up PostgreSQL database
- [ ] Configure static files serving
- [ ] Set up media files storage (S3/Cloudinary)
- [ ] Configure HTTPS
- [ ] Set up domain and DNS
- [ ] Enable CSRF protection
- [ ] Configure CORS if using API
- [ ] Set up monitoring (Sentry)
- [ ] Configure backup strategy

### Deployment Options

#### Option 1: Railway.app
```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Deploy
railway up
```

#### Option 2: Render
```yaml
# render.yaml
services:
  - type: web
    name: blog-platform
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn config.wsgi:application
```

#### Option 3: DigitalOcean App Platform
```yaml
name: blog-courses-platform
services:
- name: web
  github:
    repo: yourusername/blog-courses-platform
    branch: main
  build_command: pip install -r requirements.txt
  run_command: gunicorn config.wsgi:application
```

### Environment Variables (Production)
```bash
DEBUG=False
SECRET_KEY=your-very-secure-secret-key
DATABASE_URL=postgresql://user:pass@host:5432/db
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
AWS_ACCESS_KEY_ID=your-aws-key
AWS_SECRET_ACCESS_KEY=your-aws-secret
AWS_STORAGE_BUCKET_NAME=your-bucket
```

---

## 🔒 Security Considerations

### Django Security Settings
```python
# settings.py

# HTTPS
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# HSTS
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Other
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
```

### Password Security
- Minimum 8 characters
- Must include uppercase, lowercase, numbers
- Password hashing with Django's PBKDF2
- Rate limiting on login attempts

### CSRF Protection
- CSRF tokens on all forms
- SameSite cookie attribute
- Referer validation

### SQL Injection Prevention
- Django ORM (parameterized queries)
- No raw SQL without proper escaping

### XSS Prevention
- Template auto-escaping enabled
- Content Security Policy headers
- Sanitize user input

---

## ⚡ Performance Optimization

### Database Optimization
```python
# Use select_related for foreign keys
blogs = Blog.objects.select_related('author').all()

# Use prefetch_related for reverse foreign keys
courses = Course.objects.prefetch_related('lessons').all()

# Database indexes (see Database Design section)
```

### Caching Strategy
```python
# Redis caching
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

# Cache blog list for 15 minutes
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def blog_list(request):
    # ...
```

### Static Files
```python
# Whitenoise for static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ...
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

### Frontend Optimization
- Minify CSS/JS
- Lazy load images
- Use WebP format for images
- Enable gzip compression
- Browser caching headers

### Code Syntax Highlighting
```html
<!-- Use highlight.js (lightweight) -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
```

---

## 🔮 Future Enhancements

### Phase 1 (MVP - Current)
- ✅ Blog system
- ✅ Course system
- ✅ User authentication
- ✅ Admin dashboard
- ✅ Contact form

### Phase 2 (Q1 2026)
- [ ] Search functionality
- [ ] Blog categories/tags
- [ ] Comments system
- [ ] Email notifications
- [ ] RSS feed

### Phase 3 (Q2 2026)
- [ ] REST API
- [ ] Mobile app (React Native)
- [ ] Course progress tracking
- [ ] Certificates
- [ ] Payment integration

### Phase 4 (Q3 2026)
- [ ] Live coding playground
- [ ] Discussion forums
- [ ] Collaborative learning
- [ ] AI-powered code review
- [ ] Advanced analytics

### Potential Integrations
- 📧 **Email:** SendGrid / Mailgun
- 💳 **Payments:** Stripe / PayPal
- 📊 **Analytics:** Google Analytics / Plausible
- 🔍 **Search:** Algolia / Elasticsearch
- 💬 **Comments:** Disqus / Custom
- 📹 **Video:** YouTube / Vimeo / Custom CDN

---

## 📚 Resources & Documentation

### Official Documentation
- [Django Docs](https://docs.djangoproject.com/)
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [Django REST Framework](https://www.django-rest-framework.org/)

### Tutorials Referenced
- Django for Beginners by William S. Vincent
- Two Scoops of Django (Best Practices)
- Full Stack Python Guide

### Design Inspiration
- [Dribbble](https://dribbble.com) - UI/UX inspiration
- [Awwwards](https://awwwards.com) - Web design awards

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style
- Follow PEP 8 for Python
- Use meaningful variable names
- Add docstrings to functions
- Write tests for new features

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Muhammadali**

- University: Muhammad al-Xorazmiy nomidagi Toshkent Axborot Texnologiyalari Universiteti Samarqand filliali
- Major: Dasturiy Injiniring (Software Engineering)
- GitHub: [@yourusername](https://github.com/yourusername)
- Telegram: [@yourusername](https://t.me/yourusername)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- Muhammad al-Xorazmiy nomidagi Toshkent Axborot Texnologiyalari Universiteti for providing excellent education
- Django community for amazing framework
- Open source contributors

---

## 📞 Support

For questions or support:
- 📧 Email: your.email@example.com
- 💬 Telegram: @yourusername
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/blog-courses-platform/issues)

---

**Made with ❤️ by Muhammadali | © 2026**
