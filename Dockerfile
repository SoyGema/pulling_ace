FROM python:3.10-slim AS base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


FROM base AS python-deps

# Copy the Pipfile and Pipfile.lock into the container at /app
COPY Pipfile Pipfile.lock /app/

# Set the working directory to /app
WORKDIR /app

# Install pipenv and compilation dependencies
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

ENTRYPOINT ["python", "-m", "pulling_ace.cli"]
CMD ["10"]
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy
RUN pip install pulling_ace


FROM base AS runtime

# Copy virtual env from python-deps stage
RUN pip install .
RUN pip install pipenv
RUN apt-get update && apt-get install -y --no-install-recommends gcc

ENTRYPOINT ["python", "-m", "pulling_ace.__main__"]
CMD ["10"]
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy
RUN pip install pulling_ace


FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /app/.venv /app/.venv
ENV PATH="/.venv/bin:$PATH"

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser


# Run the executable
ENTRYPOINT ["python", "-m", "pulling_ace.cli"]
CMD ["10"]
