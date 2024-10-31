# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set an environment variable with the repository name to name the venv
ARG REPO_NAME=pokemon_go_rag_simple
ENV VENV_PATH="/opt/$REPO_NAME-venv"

# Set the working directory
WORKDIR /app

# Create and activate the virtual environment
RUN python -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# Set the PYTHONPATH to include the app directory
ENV PYTHONPATH="/app/llm_pokemon_app"

# Copy requirements and install them in the venv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Default command to run the application
CMD ["streamlit", "run", "llm_pokemon_app/src/app.py"]