# 📝 End-to-End Text Summarizer

An end-to-end NLP pipeline that generates abstractive summaries from long-form text using **Google's PEGASUS** model — packaged as a REST API and deployed to AWS via Docker and CI/CD.

---

## 📌 Problem Statement

Reading long documents, articles, or transcripts is time-consuming. This project automates the process by generating concise, context-aware abstractive summaries — reducing reading time without losing critical information.

---

## ✅ Solution

An end-to-end pipeline that:
1. Accepts raw text input via a REST API
2. Tokenizes and preprocesses the input using PEGASUS tokenizer
3. Runs inference through `google/pegasus-cnn_dailymail` fine-tuned on the SAMSum dataset
4. Returns a human-readable abstractive summary

---

## 🧠 Key Features

- **Abstractive Summarization** — generates new sentences rather than extracting existing ones
- **PEGASUS Model** — state-of-the-art transformer pre-trained specifically for summarization
- **Modular Pipeline Architecture** — independently configurable stages (ingestion → transformation → training → evaluation → prediction)
- **REST API** — served via FastAPI for easy integration
- **Containerized** — fully Dockerized for consistent environments
- **CI/CD Deployment** — automated deployment to AWS EC2 via GitHub Actions and ECR

---

## 🏗️ Architecture

```
Raw Text Input
      ↓
FastAPI Backend (app.py)
      ↓
Prediction Pipeline
   ├── PEGASUS Tokenizer
   ├── Model Inference (google/pegasus-cnn_dailymail)
   └── Decoded Summary Output
      ↓
Summary Response
```

### Training Pipeline
```
Data Ingestion → Data Transformation → Model Trainer → Model Evaluation
```

---

## 📦 Tech Stack

| Layer              | Technology                                      |
|--------------------|-------------------------------------------------|
| Model              | `google/pegasus-cnn_dailymail` (HuggingFace)    |
| Dataset            | SAMSum (dialogue summarization)                 |
| Framework          | HuggingFace Transformers, PyTorch               |
| API                | FastAPI                                         |
| Containerization   | Docker                                          |
| CI/CD              | GitHub Actions                                  |
| Cloud              | AWS EC2 + ECR                                   |
| Config Management  | YAML-based pipeline config                      |

---

## 📁 Project Structure

```
├── .github/
│   └── workflows/           # GitHub Actions CI/CD pipeline
├── config/
│   └── config.yaml          # Pipeline stage configuration
├── research/                # Exploratory notebooks (per pipeline stage)
├── src/TextSummarizer/
│   ├── components/          # Data ingestion, transformation, trainer, evaluator
│   ├── pipeline/            # Stage runners + prediction pipeline
│   ├── entity/              # Data classes / return types
│   └── config/              # Config manager
├── app.py                   # FastAPI app with /train and /predict routes
├── main.py                  # Full training pipeline runner
├── params.yaml              # Model hyperparameters
├── Dockerfile               # Container definition
├── setup.py                 # Package setup
└── requirements.txt         # Dependencies
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/dystinktbeatz/Text-summarizer-project.git
cd Text-summarizer-project
```

### 2. Create & Activate Environment

```bash
conda create -n textsummarizer python=3.8 -y
conda activate textsummarizer
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Full Training Pipeline

```bash
python main.py
```

### 5. Start the API Server

```bash
python app.py
```

Open: `http://localhost:8080`

- `GET  /train`   → triggers the full training pipeline
- `POST /predict` → returns a summary for the given input text

---

## 🐳 Docker

```bash
docker build -t text-summarizer .
docker run -p 8080:8080 text-summarizer
```

---

## 🚀 AWS Deployment (EC2 + ECR via GitHub Actions)

This project uses a fully automated CI/CD pipeline:

1. **Push to main** triggers the GitHub Actions workflow
2. Docker image is **built and pushed to AWS ECR**
3. EC2 instance **pulls the latest image** and runs the container

### Required GitHub Secrets

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
AWS_ECR_LOGIN_URI
ECR_REPOSITORY_NAME
```

### EC2 Setup (one-time)

```bash
sudo apt-get update -y && sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

Configure EC2 as a self-hosted GitHub Actions runner:
`Settings → Actions → Runners → New self-hosted runner`

Then open port **8080** in your EC2 security group inbound rules.

---

## 🔁 Pipeline Stages

| Stage               | Description                                              |
|---------------------|----------------------------------------------------------|
| Data Ingestion      | Downloads and stores the SAMSum dataset                  |
| Data Transformation | Tokenizes dialogues using PEGASUS tokenizer              |
| Model Trainer       | Fine-tunes `google/pegasus-cnn_dailymail` on SAMSum      |
| Model Evaluation    | Computes ROUGE scores on the validation set              |
| Prediction Pipeline | Loads saved model + tokenizer and runs inference         |

---

## 🎯 Future Improvements

- Add ROUGE benchmark scores to README
- Support multi-document summarization
- Stream output for long-form documents
- Build a frontend UI
- Experiment with BART (`facebook/bart-large-cnn`) for comparison

---

## 🧠 Author

**Gautham N Vijayan**
Data Scientist | NLP & GenAI
[LinkedIn](https://linkedin.com/in/your-profile) · [GitHub](https://github.com/dystinktbeatz)
