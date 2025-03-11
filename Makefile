.PHONY: setup setup-frontend setup-backend dev frontend backend build clean

# Check if uv is available
UV_CHECK := $(shell command -v uv 2> /dev/null)

# Default target
all: setup

# Setup both frontend and backend
setup: setup-frontend setup-backend

# Setup frontend dependencies
setup-frontend:
	@echo "Setting up frontend dependencies..."
	cd frontend && npm install --ignore-scripts

# Setup backend dependencies
setup-backend:
ifdef UV_CHECK
	@echo "Setting up backend dependencies using uv..."
	@echo "Creating virtual environment..."
	cd backend && uv venv
	@echo "Installing dependencies..."
	cd backend && uv pip install -r requirements.txt
else
	@echo "Setting up backend dependencies using pip..."
	@echo "Creating virtual environment..."
	cd backend && python3 -m venv venv
	@echo "Installing dependencies..."
	cd backend && . venv/bin/activate && python3 -m pip install -r requirements.txt
endif

# Run both frontend and backend development servers
dev:
	@echo "Starting development servers..."
	$(MAKE) backend & $(MAKE) frontend

# Run frontend development server
frontend:
	@echo "Starting frontend server..."
	cd frontend && npm run dev

# Run backend development server
backend:
ifdef UV_CHECK
	@echo "Starting backend server with UV environment..."
	cd backend && . .venv/bin/activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
else
	@echo "Starting backend server with pip environment..."
	cd backend && . venv/bin/activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
endif

# Build frontend for production
build:
	@echo "Building frontend for production..."
	cd frontend && npm run build

# Clean up dependencies and build artifacts
clean:
	@echo "Cleaning up..."
	rm -rf frontend/node_modules
	rm -rf frontend/build
	rm -rf backend/__pycache__
	rm -rf backend/venv
	rm -rf backend/.venv
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +

# Create project structure
init:
	@echo "Creating project structure..."
	mkdir -p frontend/src/lib/components
	mkdir -p frontend/src/routes
	mkdir -p frontend/static
	mkdir -p backend/app/api/endpoints
	mkdir -p backend/app/core
	mkdir -p backend/app/models
	mkdir -p backend/app/services
	mkdir -p backend/tests
	touch backend/app/__init__.py
	touch backend/app/api/__init__.py
	touch backend/app/api/endpoints/__init__.py
	touch backend/app/core/__init__.py
	touch backend/app/models/__init__.py
	touch backend/app/services/__init__.py 