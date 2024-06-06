#!/bin/bash

set -e

REGION=$1
RUN_SA=$2

cp templates/config.toml ../backend_apis/app
cd ../backend_apis
gcloud run deploy genai-for-marketing --source . --allow-unauthenticated --region="${REGION}" --service-account="${RUN_SA}"

# gcloud run deploy genai-for-marketing --source . --allow-unauthenticated --region="us-central1" --service-account="genai-marketing-run@lealprodcns.iam.gserviceaccount.com" --project lealprodcns

