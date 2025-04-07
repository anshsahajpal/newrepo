FROM python:3.10

# Set working directory inside the container
WORKDIR /app

COPY ./shared /app/shared
COPY ./task_management /app/task_management

# Install dependencies
RUN pip install --no-cache-dir -r ./task_management/requirements.txt

# Copy the shared folder from the root

# Set Python path so the app can import shared modules
ENV PYTHONPATH="/app"

# Command to run the app
CMD ["python", "-m", "task_management.main"]