# Cloud-Native DevOps Platform for AI-based Log Analytics
A DevOps-based log processing system using microservices (frontend, backend, worker) with Redis queue. Built and deployed using GitHub Actions, Docker, and ArgoCD on Kubernetes, with security and monitoring support.

### Why AI-Based Log Analytics 
The project is called Cloud-Native DevOps Platform for AI based Log Analytics because it combines cloud-native infrastructure using AWS EKS and Kubernetes with a complete DevOps pipeline including CI/CD, monitoring, and security. On top of that, the application processes logs using a worker-based architecture with a queue system, which is designed to support AI-based log analysis like anomaly detection and intelligent insights

### GitOps Repository

Kubernetes manifests and deployment configurations are maintained in a separate GitOps repository:
https://github.com/tejaskalal/k8s-manifests

### Project Architecture
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

### Project Results
<img width="1841" height="1005" alt="Screenshot 2026-04-14 132641" src="https://github.com/user-attachments/assets/6a3df2b7-d3db-4be2-b915-8f7641ae3c4d" />

<img width="1861" height="1009" alt="Screenshot 2026-04-14 132650" src="https://github.com/user-attachments/assets/dbe0a678-1965-4213-a169-3615ebc017e4" />

<img width="1767" height="1005" alt="Screenshot 2026-04-14 133042" src="https://github.com/user-attachments/assets/ef29597a-13f2-4139-a1a6-beb806837789" />

<img width="1862" height="856" alt="Screenshot 2026-04-14 133105" src="https://github.com/user-attachments/assets/6a7c77b7-4e72-464b-957a-6f8c49a33931" />

<img width="1864" height="970" alt="Screenshot 2026-04-14 133154" src="https://github.com/user-attachments/assets/c6c476d6-0712-4bad-91d9-048296f425fc" />

<img width="1856" height="855" alt="Screenshot 2026-04-15 230557" src="https://github.com/user-attachments/assets/ed52d95b-f8d3-4f1b-a17b-16478d2d07cb" />




