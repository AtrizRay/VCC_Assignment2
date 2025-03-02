
# Assignment 2

## Project Overview
This project focuses on setting up a **Virtual Machine (VM)** infrastructure on **Google Cloud Platform (GCP)** with features like **auto-scaling** and **secure access control**. The project demonstrates how to configure a **Managed Instance Group (MIG)** that automatically scales instances based on CPU utilization, ensuring optimal resource allocation under fluctuating workloads. Security is enforced through **Firewall Rules** and **IAM Role Management**.

---

## Technologies Used

- **Google Cloud Platform (GCP)** (Infrastructure Management)
- **Compute Engine** (Virtual Machine Instances)
- **Managed Instance Group (MIG)** (Auto-scaling setup)
- **Firewall Rules** (Network security)
- **IAM Roles** (Access control)
- **Python (Stress Testing)** (CPU stress script for testing auto-scaling)

---

## Project Setup & Execution

### 1. VM Creation & Configuration

- Created an **Instance Template** using **Ubuntu 22.04** as the base image.
- Configured the template with necessary machine type (CPU, RAM) and disk specifications.
- Created a **Managed Instance Group (MIG)** using the template to automatically manage VM instances.

### 2. Auto-scaling Setup

- Configured **auto-scaling policy**:
    - Minimum Instances: 1
    - Maximum Instances: 10
    - Scaling Trigger: CPU utilization > 60%
- Auto-scaling ensures cost-efficient operations, automatically adjusting the number of running instances based on real-time demand.

### 3. Security Configuration

- Configured **Firewall Rules**:
    - Allow **SSH (port 22)** only from the admin’s IP.
    - Optionally allow **HTTP (port 80)** for web access.
    - Deny all other inbound traffic to enhance security.
- Assigned **IAM Roles**:
    - Compute Admin: To allow management of Compute resources.
    - Storage Admin (optional): To manage cloud storage if needed.

### 4. Testing Auto-scaling

- Deployed a **Python script** on the VM to simulate high CPU usage and observe auto-scaling response.
- Command used:
    ```bash
    stress-ng --cpu 4 --timeout 300
    ```
- Observed resource metrics through the GCP **Monitoring Dashboard** to validate scaling behavior.

---

## Testing & Observation

- Despite testing with load simulation, the CPU usage remained at around **10.82%**.
- This indicates that the **initial instance size was over-provisioned**, meaning fewer resources could handle the simulated load.
- No scaling event occurred under the tested conditions, showing the system was well within capacity.

---

## Repository & Demo

- **Report Document:** `M23AID007_Assignment2_Document Report.pdf`
- **Architecture Diagram:** `M23AID007_Assignment2_Architecture Diagram.png`

---

## Conclusion
This project successfully demonstrates the deployment of **auto-scaling virtual machine infrastructure** on **GCP**. Key **cloud engineering principles** were applied, including:
- **Performance optimization** through auto-scaling.
- **Cost management** by dynamically adjusting instances.
- **Security enforcement** using firewall rules and strict IAM role assignments.

The hands-on experience gained through this assignment strengthens understanding of **cloud infrastructure design** and **GCP service orchestration**, which is crucial for building reliable and secure cloud applications.
