#!/bin/bash
# deploy_fixed.sh

echo "🚀 Deploying FIXED Veo3 Bypass..."

# Create project jika belum ada
PROJECT_ID="veo3-$(date +%s)"
echo "Creating project: $PROJECT_ID"
gcloud projects create $PROJECT_ID --name="Veo3 Bypass Fixed"

# Set project
gcloud config set project $PROJECT_ID

# Enable APIs
gcloud services enable aiplatform.googleapis.com run.googleapis.com

# Deploy to Cloud Run
echo "Deploying to Cloud Run..."
gcloud run deploy veo3-bypass-fixed \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 512Mi \
  --cpu 1 \
  --set-env-vars="PROJECT_ID=$PROJECT_ID" \
  --timeout 300

# Get URL
URL=$(gcloud run services describe veo3-bypass-fixed --format="value(status.url)")
echo ""
echo "✅ DEPLOYED SUCCESSFULLY!"
echo "🌐 URL: $URL"
echo "🔧 Health: $URL/api/health"
echo "🎬 Generate: POST $URL/api/generate"
echo ""
echo "Example:"
echo "curl -X POST $URL/api/generate \\"
echo "  -H 'Content-Type: application/json' \\"
echo "  -d '{\"prompt\":\"A beautiful sunset\"}'"
