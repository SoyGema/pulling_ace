FROM python:3.10-slim AS base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PATH="/app/.venv/bin:$PATH"

FROM base AS python-deps

# Copy the Pipfile and Pipfile.lock into the container at /app
COPY Pipfile Pipfile.lock /app/
COPY . /app
# Set the working directory to /app
WORKDIR /app

# Check if the pulling_ace directory exists and copy it into the Docker image
RUN if [ -d "pulling_ace" ] ; then COPY pulling_ace /app/pulling_ace ; else echo "Directory pulling_ace does not exist" ; exit 1 ; fi

# Install pipenv and compilation dependencies
RUN pip install pipenv && \
    apt-get update && apt-get install -y --no-install-recommends gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYTHON /app
ENTRYPOINT ["python", "-m", "pulling_ace"]
CMD ["cli","10"]
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy


FROM base AS runtime

# Check if the pulling_ace directory exists in the python-deps stage and copy it
RUN if [ -d "/app/pulling_ace" ] ; then COPY --from=python-deps /app/pulling_ace /app/pulling_ace ; else echo "Directory pulling_ace does not exist in python-deps stage" ; exit 1 ; fi

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
COPY --from=python-deps /app/.venv /home/appuser/.venv
RUN chown -R appuser:appuser /home/appuser/.venv

USER appuser

# Run the executable
ENTRYPOINT ["python", "-m", "pulling_ace"]
CMD ["cli", "10"]
