# Multi-Cloud Deployment Project 🚀

## Introduction 🌐
This project demonstrates the automation of infrastructure provisioning and application deployment across **AWS** and **Azure** using **Terraform** and **Ansible**. The goal is to provide a seamless deployment of an ASP.NET Core application across multiple cloud platforms, leveraging CI/CD pipelines in Azure DevOps.

## **Problem Statement** 🤔
Organizations often face challenges when deploying applications across cloud providers like **AWS** and **Azure**, including:  
- Managing infrastructure consistently.  
- Handling dynamic inventory updates.  
- Ensuring secure and automated deployment processes.

## **Solution** 💡  
This project solves the problem by:  
1. Using **Terraform** for provisioning consistent infrastructure.  
2. Leveraging **Ansible** for automating server configurations and deployments.  
3. Implementing CI/CD pipelines with **Azure DevOps** for seamless integration and delivery.

## Features ✨
- **Infrastructure-as-Code (IaC):** Automated provisioning of cloud resources with Terraform.
- **Cross-Cloud Deployment:** Simultaneous deployment to AWS and Azure.
- **Configuration Management:** Ansible scripts for **dynamic inventory** creation and server configuration.
- **CI/CD Integration:** Azure DevOps pipeline for end-to-end automation.
- **Secure & Scalable:** Uses SSH for secure communication and scales effortlessly across clouds.

## **Tools & Technologies Used** 🛠️
### **1. Terraform**
- **Purpose**: Provision cloud infrastructure on AWS and Azure.
- **Features**:
  - State management with Azure Blob Storage.
  - Automated provisioning of compute, network, and security resources.
- **Highlights**:
  - Creates AWS EC2 instances and Azure VMs with security rules for SSH and application traffic.

### **2. Ansible**
- **Purpose**: Configuration management and application deployment.
- **Features**:
  - Automates secure SSH setup and `.NET` application deployment.
  - Dynamic inventory for managing nodes across multiple clouds.

### **3. Azure DevOps**
- **Purpose**: Manage CI/CD pipelines.
- **Features**:
  - Multi-stage pipelines for building, provisioning, and deploying.
  - Artifact management for `.NET` applications.
  - Secure files feature to pass secrets, tokens, ssh keys, etc without hardcoding credentials in the scripts.
  - Service connection to Azure, AWS enabling seamless authentication to both the cloud providers. Leveraging service connections to run terraform scripts was a game changer.

### **4. ASP.NET Core**
- **Purpose**: Backend application for deployment.
- **Features**:
  - Runs on port `5000` across cloud instances.
  - Deployed as a Linux service for high availability.

### **5. ChatGPT**


## Architecture Diagrams 🖼️
This diagram illustrates the seamless integration of CI/CD pipelines with multi-cloud infrastructure:
### High-Level Design
<img width="781" alt="2024-12-28 00_10_16-Multi-cloud drawio (3)" src="https://github.com/user-attachments/assets/521546f4-6396-4644-b561-bfdb4f3f86f5" />

## Prerequisites ✅
- **Azure DevOps Account:** To set up CI/CD pipelines.
- **AWS Account:** For deploying resources.
- **Azure Subscription:** For provisioning resources.
- **Terraform & Ansible:** Installed locally for testing.
- **SSH Key Pair:** For secure connections.
- **Azure DevOps Server installed locally on Linux**: To run self hosted agent for ansible scripts.

## Step-by-Step Guide 🪜

### 1. Set Up Terraform Backend
- Configure the backend for **Azure Blob Storage** to store the Terraform state file securely.

### 2. Build application and publish artifact
- On Successful build run of the Microsoft hosted agent, the application is packaged and published to pipeline artifact.

### 3. Provision Infrastructure
- **AWS:** Launch EC2 instances, configure security groups, and attach public IPs.
- **Azure:** Provision Virtual Machines, associate NSGs, and allocate public IPs.

### 4. Configure CI/CD Pipeline
- **Build Pipeline (Microsoft hosted agent):** Build and package the ASP.NET application.
- **Terraform Pipeline (Microsoft hosted agent):** Run Terraform to provision infrastructure.
- **Self-hosted Ansible Pipeline (Self hosted agent):** Configure remote nodes, install sdks and runtime, deploy app running as a service in the background.

### 5. Use Ansible for Configuration Management
- Dynamic inventory creation using Python scripts.
- Add VMs to the known hosts file for secure SSH communication.

### 6. Application Deployment
- Deploy the ASP.NET Core app on VMs using Ansible playbooks.
- Expose the application on **port 5000** for public access.

## How It Works 🛠️
1. **CI/CD Pipeline:**
   - Code is pushed to the `main` branch in Azure Repos.
   - Azure DevOps triggers a pipeline to build the application and apply Terraform scripts.
2. **Terraform Scripts:**
   - Create AWS EC2 instances and Azure VMs.
   - Open necessary ports in AWS Security Groups and Azure NSGs.
3. **Ansible Playbooks:**
   - Configure the VMs and deploy the app.
   - Manage dynamic inventory using `parse_ips_from_state.py`.
4. **Dynamic Inventory:**
   - Automate IP discovery and SSH key management.

## Challenges Faced 💪
- Resolving SSH known hosts conflicts.
- Managing Terraform state files across multiple cloud platforms.
- Debugging Ansible dynamic inventory scripts.
- Setting up passwordless authentication for ansible on remote nodes using Microsoft hosted agents.
- Finding a way to run application as a service in the background and not letting the pipeline run for a long time as the application is running in the foreground. 

## Learnings 🌿
- Importance of using secure secrets management.
- Effective use of Terraform for multi-cloud setups.
- Leveraging CI/CD pipelines for efficient workflows.
- Using Self hosted agent to run ansible scripts instead of Microsoft hosted agent. Due to ephemeral nature of Microsoft hosted agent it was complex to run ansible tasks on remote nodes. 

## Potential Enhancements 🚀
- Add Kubernetes support for containerized deployments.
- Application monitoring.
- Add load balancer to distribute load between both the cloud providers.
- Implement cost-optimization strategies using FinOps tools.

---
