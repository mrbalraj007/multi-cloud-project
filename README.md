# Multi-Cloud Deployment Project 🚀

## Introduction 🌐
This project demonstrates the automation of infrastructure provisioning and application deployment across **AWS** and **Azure** using **Terraform** and **Ansible**. The goal is to provide a seamless deployment of an ASP.NET Core application across multiple cloud platforms, leveraging CI/CD pipelines in Azure DevOps.

## Features ✨
- **Infrastructure-as-Code (IaC):** Automated provisioning of cloud resources with Terraform.
- **Cross-Cloud Deployment:** Simultaneous deployment to AWS and Azure.
- **Configuration Management:** Ansible scripts for dynamic inventory creation and server configuration.
- **CI/CD Integration:** Azure DevOps pipeline for end-to-end automation.
- **Secure & Scalable:** Uses SSH for secure communication and scales effortlessly across clouds.

## Architecture Diagrams 🖼️

### High-Level Design
![Multi-cloud drawio (2)](https://github.com/user-attachments/assets/c7fd62a6-c3c1-42d9-8aa2-f43b7ed49971)
<img width="781" alt="2024-12-28 00_10_16-Multi-cloud drawio (3)" src="https://github.com/user-attachments/assets/521546f4-6396-4644-b561-bfdb4f3f86f5" />


### Low-Level Design
![Low-Level Design](https://via.placeholder.com/600x400.png?text=Low-Level+Design+Diagram)

## Prerequisites ✅
- **Azure DevOps Account:** To set up CI/CD pipelines.
- **AWS Account:** For deploying resources.
- **Azure Subscription:** For provisioning resources.
- **Terraform & Ansible:** Installed locally for testing.
- **SSH Key Pair:** For secure connections.
- **Azure DevOps Server installed locally on Linux**: To run self hosted agent for ansible scripts.


## Step-by-Step Guide 🛠️

### 1. Set Up Terraform Backend
- Configure the backend for **Azure Blob Storage** to store the Terraform state file securely.

### 2. Provision Infrastructure
- **AWS:** Launch EC2 instances, configure security groups, and attach public IPs.
- **Azure:** Provision Virtual Machines, associate NSGs, and allocate public IPs.

### 3. Configure CI/CD Pipeline
- **Pipeline 1:** Build and package the ASP.NET application.
- **Pipeline 2:** Run Terraform to provision infrastructure and deploy the app.

### 4. Use Ansible for Configuration Management
- Dynamic inventory creation using Python scripts.
- Add VMs to the known hosts file for secure SSH communication.

### 5. Application Deployment
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



## Challenges Faced 😅
- Resolving SSH known hosts conflicts.
- Managing Terraform state files across multiple cloud platforms.
- Debugging Ansible dynamic inventory scripts.

## Learnings 🎓
- Importance of using secure secrets management.
- Effective use of Terraform for multi-cloud setups.
- Leveraging CI/CD pipelines for efficient workflows.

## Future Enhancements 🚀
- Add Kubernetes support for containerized deployments.
- Use HashiCorp Vault for better secrets management.
- Implement cost-optimization strategies using FinOps tools.

---
