FROM python:3.9

# Create a non-root user
RUN useradd --create-home appuser
WORKDIR /home/appuser

# Set the non-root user as the owner of the application folder
COPY --chown=appuser:appuser requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser . .

# Switch to the non-root user
USER appuser

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
