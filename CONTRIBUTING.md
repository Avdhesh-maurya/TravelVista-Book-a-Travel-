# Contributing Guidelines

## Getting Started

1. Clone the repository
2. Create a virtual environment
3. Install dependencies from `requirements.txt`
4. Copy `.env.example` to `.env` and configure as needed
5. Run migrations: `python manage.py migrate`
6. Create a superuser: `python manage.py createsuperuser`
7. Run the development server: `python manage.py runserver`

## Code Standards

- Follow PEP 8 naming conventions
- Use meaningful commit messages
- Test your changes before submitting
- Keep functions small and focused
- Document complex logic with comments

## Commit Message Format

```
type: brief description

Longer explanation if needed, wrapped at 72 characters.
- Bullet points are ok too
- Especially for listing changes

Fixes #123
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Pull Request Process

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes
3. Test thoroughly
4. Push to your fork
5. Submit a pull request with clear description

## Reporting Issues

- Describe what you were doing when the issue occurred
- Include error messages and stack traces
- Specify your environment (OS, Python version)
- Provide steps to reproduce the issue

## Questions?

Feel free to open an issue or discussion for questions!
