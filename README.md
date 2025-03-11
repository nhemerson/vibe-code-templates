# Svelte + FastAPI + Tailwind Template

A modern web application template that combines:

- **Frontend**: Svelte.js with Tailwind CSS
- **Backend**: FastAPI (Python)
- **Automation**: Makefile for easy setup and development

## Features

- ✅ Latest Svelte.js for reactive UI development
- ✅ FastAPI for high-performance Python backend
- ✅ Tailwind CSS for utility-first styling
- ✅ Fully configured development environment
- ✅ API integration examples
- ✅ Responsive design examples

## Prerequisites

- Node.js (v16+)
- Python (v3.8+)
- Make

## Quick Start

1. Clone this repository
2. Run the setup command:

```bash
make setup
```

3. Start development servers:

```bash
make dev
```

4. Open your browser at `http://localhost:5173` for the frontend, and `http://localhost:8000/docs` for the API documentation.

## Available Commands

- `make setup` - Install all dependencies
- `make dev` - Start both frontend and backend development servers
- `make frontend` - Start only the frontend development server
- `make backend` - Start only the backend development server
- `make build` - Build the frontend for production
- `make clean` - Remove build artifacts and dependencies

## Project Structure

```
├── frontend/          # Svelte.js frontend application
├── backend/           # FastAPI Python backend
└── Makefile           # Automation commands
```

## License

MIT 