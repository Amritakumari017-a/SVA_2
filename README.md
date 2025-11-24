# Smart Video Annotation System (SVA_2)

A comprehensive Django-based platform that transforms any video into an interactive learning experience. Create timestamped notes, generate AI summaries, take quizzes, and export your learning materials with our intelligent video annotation system.

## 🌟 Features

### Core Features
- **Timestamped Notes**: Click anywhere on the timeline to add notes at specific moments
- **Smart Search**: Find any note instantly with semantic search powered by AI embeddings
- **AI Summarization**: Generate intelligent summaries (brief, detailed, or quiz-style)
- **Export Notes**: Export your notes and summaries as PDFs or ZIP files
- **AI Test Generation**: Generate multiple-choice quizzes from video content
- **Voice Notes**: Record voice notes using your microphone with automatic transcription
- **YouTube Integration**: Embed YouTube videos directly in the platform
- **Local Video Upload**: Upload and process video files from your computer
- **Clip Export**: Extract video segments with ffmpeg support
- **Dark/Light Theme**: Toggle between themes with persistent preferences

### Technical Features
- **Modern UI/UX**: Cinematic design with glassmorphism effects and smooth animations
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Real-time Interactions**: Timeline interactions, voice recording, and live updates
- **AI Integration**: OpenAI GPT for summaries, quiz generation, and embeddings
- **Video Processing**: FFmpeg support for video clipping and processing
- **PDF Generation**: WeasyPrint and ReportLab support for note exports
- **Docker Support**: Complete containerization with PostgreSQL
- **Comprehensive Testing**: Unit tests and demo data included

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL (optional, SQLite works for development)
- FFmpeg (optional, for video processing)
- OpenAI API Key (optional, for AI features)

### Local Development Setup (SQLite)

1. **Clone and Setup**
   ```bash
   cd SVA_2
   python -m venv venv
   
   # Windows
   .\venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

2. **Environment Configuration**
   ```bash
   copy env.example .env
   # Edit .env file with your settings
   ```

3. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py loaddata fixtures/demo_data.json  # Optional demo data
   ```

4. **Run Development Server**
   ```bash
   python manage.py runserver
   # Open http://127.0.0.1:8000
   ```

### Production Setup (PostgreSQL)

1. **Install PostgreSQL**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install postgresql postgresql-contrib
   
   # macOS with Homebrew
   brew install postgresql
   
   # Windows
   # Download from https://www.postgresql.org/download/windows/
   ```

2. **Create Database**
   ```sql
   CREATE DATABASE smart_video_annotation;
   CREATE USER sva_user WITH PASSWORD 'sva_password';
   GRANT ALL PRIVILEGES ON DATABASE smart_video_annotation TO sva_user;
   ```

3. **Configure Environment**
   ```bash
   # In .env file
   DATABASE_URL=postgresql://sva_user:sva_password@localhost:5432/smart_video_annotation
   SECRET_KEY=your-secret-key-here-change-this-in-production
   DEBUG=False
   ```

4. **Run Migrations**
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   python manage.py createsuperuser
   ```

### Docker Setup

1. **Using Docker Compose**
   ```bash
   docker compose up --build
   # Open http://localhost:8000
   ```

2. **Manual Docker Build**
   ```bash
   docker build -t sva-app .
   docker run -p 8000:8000 sva-app
   ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Django Configuration
SECRET_KEY=your-secret-key-here-change-this-in-production
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

# OpenAI Configuration (optional)
OPENAI_API_KEY=your-openai-api-key-here

# FFmpeg Configuration (optional)
FFMPEG_PATH=/usr/bin/ffmpeg

# Email Configuration (for future use)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Security Settings
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
```

### OpenAI Setup

1. **Get API Key**
   - Visit [OpenAI Platform](https://platform.openai.com/)
   - Create an account and generate an API key
   - Add the key to your `.env` file

2. **Features Requiring OpenAI**
   - AI Summarization
   - Quiz Generation
   - Semantic Search (embeddings)
   - AI Suggestions for notes

### FFmpeg Setup

1. **Install FFmpeg**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install ffmpeg
   
   # macOS with Homebrew
   brew install ffmpeg
   
   # Windows
   # Download from https://ffmpeg.org/download.html
   ```

2. **Configure Path**
   ```bash
   # Add to .env file
   FFMPEG_PATH=/usr/bin/ffmpeg  # or your ffmpeg path
   ```

3. **Features Requiring FFmpeg**
   - Video clip extraction
   - Video processing
   - Audio extraction

## 📱 Usage Guide

### Getting Started

1. **Sign Up**: Create an account with your email and preferences
2. **Add Videos**: Upload files or add YouTube URLs
3. **Create Notes**: Click on the timeline to add timestamped notes
4. **Use Voice Notes**: Click the microphone button to record voice notes
5. **Generate Summaries**: Use AI to create video summaries
6. **Take Quizzes**: Generate and take quizzes based on video content
7. **Export Materials**: Download notes and summaries as PDFs

### Key Features Usage

#### Timeline Interactions
- Click anywhere on the timeline to add a note
- Double-click to open the note popover
- Drag to select a time range for AI analysis

#### Voice Notes
- Click the microphone button in the note popover
- Speak clearly into your microphone
- The system will transcribe your speech automatically
- Edit the transcription before saving

#### AI Features
- **Generate Summary**: Creates intelligent summaries of video content
- **Generate Quiz**: Creates multiple-choice questions from video content
- **AI Suggestions**: Get AI-powered suggestions for note content

#### Export Options
- **PDF Export**: Download notes and summaries as formatted PDFs
- **ZIP Export**: Download all your notes as a ZIP file
- **Clip Export**: Extract video segments (requires FFmpeg)

## 🧪 Testing

### Run Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test users
python manage.py test workspace
python manage.py test ai_tools

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html
```

### Demo Data
```bash
# Load demo data
python manage.py loaddata fixtures/demo_data.json

# Demo user credentials
Username: demo
Password: demo123
Email: demo@example.com
```

## 🐛 Troubleshooting

### Common Issues

#### Database Issues
```bash
# Reset migrations
python manage.py migrate --fake-initial
python manage.py migrate

# Clear database and start fresh
python manage.py flush
python manage.py migrate
python manage.py loaddata fixtures/demo_data.json
```

#### Static Files Issues
```bash
# Collect static files
python manage.py collectstatic --noinput

# Clear static files cache
rm -rf staticfiles/
python manage.py collectstatic
```

#### Media Files Issues
```bash
# Create media directory
mkdir -p media/videos media/thumbnails media/voice_notes media/clips

# Set proper permissions
chmod 755 media/
```

#### OpenAI API Issues
- Verify your API key is correct
- Check your OpenAI account has sufficient credits
- Ensure the API key has the necessary permissions

#### FFmpeg Issues
- Verify FFmpeg is installed: `ffmpeg -version`
- Check the path in your `.env` file
- Ensure FFmpeg has proper permissions

### Debug Mode

Enable debug logging:
```python
# In settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

### Performance Issues

1. **Database Optimization**
   ```bash
   # Add database indexes
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Static Files**
   ```bash
   # Use WhiteNoise for static files
   python manage.py collectstatic
   ```

3. **Media Files**
   - Use a CDN for production
   - Implement file compression
   - Set up proper caching headers

## 🔒 Security

### Production Security Checklist

- [ ] Change `SECRET_KEY` in production
- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use HTTPS in production
- [ ] Set up proper database permissions
- [ ] Configure CORS settings
- [ ] Set up file upload restrictions
- [ ] Implement rate limiting
- [ ] Use environment variables for secrets
- [ ] Set up proper logging

### File Upload Security
```python
# In settings.py
FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880  # 5MB
FILE_UPLOAD_PERMISSIONS = 0o644
```

## 📊 Performance Monitoring

### Database Monitoring
```bash
# Check slow queries
python manage.py dbshell
# In PostgreSQL:
# SELECT query, mean_time FROM pg_stat_statements ORDER BY mean_time DESC LIMIT 10;
```

### Application Monitoring
- Use Django Debug Toolbar for development
- Implement logging for production monitoring
- Set up error tracking (Sentry, etc.)
- Monitor file upload sizes and processing times

## 🚀 Deployment

### Heroku Deployment
```bash
# Install Heroku CLI
# Create Procfile (already included)
# Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DATABASE_URL=your-postgres-url
heroku config:set OPENAI_API_KEY=your-openai-key

# Deploy
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

### Docker Production
```bash
# Build production image
docker build -t sva-prod .

# Run with production settings
docker run -e DEBUG=False -e SECRET_KEY=your-key sva-prod
```

## 📚 API Documentation

### Endpoints

#### Authentication
- `POST /api/update-theme/` - Update user theme preference

#### Workspace
- `POST /workspace/api/notes/` - Add new note
- `PUT /workspace/api/notes/{id}/` - Update note
- `DELETE /workspace/api/notes/{id}/delete/` - Delete note
- `POST /workspace/api/generate-summary/` - Generate AI summary
- `POST /workspace/api/generate-quiz/` - Generate AI quiz

#### AI Tools
- `POST /ai/generate-summary/` - Generate video summary
- `POST /ai/generate-quiz/` - Generate quiz questions
- `POST /ai/submit-quiz/` - Submit quiz answers

#### Revision
- `GET /revision/search/` - Search notes
- `GET /revision/video/{id}/export-pdf/` - Export PDF
- `GET /revision/export-all/` - Export all notes

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

### Development Guidelines
- Follow PEP 8 style guidelines
- Write comprehensive tests
- Update documentation for new features
- Use meaningful commit messages
- Test on multiple browsers and devices

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Team

- **Alex Chen** - Backend Development & AI Integration
- **Maria Rodriguez** - Frontend Development & UI/UX Design
- **David Kim** - Video Processing & Infrastructure
- **Sarah Johnson** - Testing & Documentation

## 🆘 Support

### Getting Help
- Check the troubleshooting section above
- Review the demo data for examples
- Run the test suite to verify your setup
- Check Django logs for detailed error messages

### Reporting Issues
When reporting issues, please include:
- Django version
- Python version
- Operating system
- Error messages and stack traces
- Steps to reproduce the issue

### Feature Requests
We welcome feature requests! Please describe:
- The feature you'd like to see
- How it would benefit users
- Any implementation ideas you have

---

**Built with ❤️ using Django, OpenAI, and modern web technologies.**

