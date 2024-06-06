docker build -t genai:latest  .
docker run -p 8080:8080 -v /home/simon/.config/gcloud/application_default_credentials.json:/adc.json:ro -e GOOGLE_APPLICATION_CREDENTIALS=/adc.json genai:latest
