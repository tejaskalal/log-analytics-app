# Cloud-Native DevOps Platform for AI-based Log Analytics
A DevOps-based log processing system using microservices (frontend, backend, worker) with Redis queue. Built and deployed using GitHub Actions, Docker, and ArgoCD on Kubernetes, with security and monitoring support.

## Project Architecture
<img width="6085" height="3440" alt="project-architecure" src="https://github.com/user-attachments/assets/49b218ef-5d0c-4d3a-aab6-da4f2d4d575e" />

### Tools & Technologies
- GitHub Actions
- ArgoCD
- Docker
- Docker Hub
- Kubernetes
- AWS (EKS, ALB, IAM , EC2 , VPC)
- Prometheus
- Grafana
- Trivy
- SonarQube
- GitHub

### Project Features

- End-to-End CI/CD Pipeline using GitHub Actions and ArgoCD  
- GitOps-based Deployment (Auto sync from GitHub to Kubernetes)  
- Containerized Application using Docker  
- Scalable Deployment on Kubernetes (Amazon EKS)  
- External Access via AWS ALB Ingress Controller  
- Automated Image Build & Push to Docker Hub  
- Continuous Monitoring using Prometheus & Grafana  
- Security Scanning with Trivy  
- Code Quality Analysis using SonarQube  
- Automated Rollouts & Self-Healing using Kubernetes  
- High Availability & Load Balancing  
- Version Controlled Infrastructure & Manifests  
