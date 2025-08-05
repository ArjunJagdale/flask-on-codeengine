# GitHub Activity Viewer 🚀

A simple, cloud-deployed web app built with Flask that fetches and displays the most recent public GitHub activity for any user — deployed on IBM Cloud Code Engine.

![IBM Cloud](https://img.shields.io/badge/IBM%20Cloud-Code%20Engine-blue) ![Python](https://img.shields.io/badge/Python-3.10+-yellow) ![Flask](https://img.shields.io/badge/Flask-Web%20App-red)

---

## 🔗 Live Demo

🌐 [https://flask-app.1yq58jnqs57o.us-south.codeengine.appdomain.cloud](https://flask-app.1yq58jnqs57o.us-south.codeengine.appdomain.cloud)

---

## ✨ Features

- 🔍 Enter a GitHub username and fetch latest public activity.
- 🎨 Clean, centered UI built with pure HTML & CSS (no JS).
- ☁️ Fully containerized & deployed on IBM Cloud Code Engine.
- 📦 Auto builds from GitHub repo — just push to deploy!

---

## 🖼️ Preview

![demo](https://github.com/user-attachments/assets/f793fee3-6346-439a-98ba-72fd7370f930)

---

## 📁 Project Structure

```

.
├── app.py              # Flask application
├── requirements.txt    # Dependencies
└── README.md           # You're reading it!

````

---

## 🛠️ Tech Stack

| Layer       | Tech                     |
|------------|---------------------------|
| Backend     | Python + Flask           |
| Deployment  | IBM Cloud Code Engine    |
| Source Host | GitHub                   |
| Runtime     | Docker (auto build)      |

---

## ☁️ Why IBM Cloud?

This project was built to demonstrate real-world deployment skills using **IBM Cloud Code Engine**, a powerful, fully-managed, serverless platform. IBM Cloud was chosen because:

* ✅ It abstracts away Kubernetes and infrastructure management
* 🔄 It automatically builds container images from source code (no Dockerfile required)
* 📈 It auto-scales applications based on demand — from 0 to N instances
* 🧩 It integrates seamlessly with GitHub for continuous delivery

---

## 🧠 IBM Cloud Code Engine – Under the Hood

**Code Engine** allows you to deploy apps without managing the infrastructure:

| Feature               | How it’s used in this project             |
| --------------------- | ----------------------------------------- |
| Build from Git repo   | Pulls `app.py` & dependencies from GitHub |
| Serverless runtime    | Flask app runs only when accessed         |
| Auto-scaling          | Automatically scales between 0 and 3 pods |
| Logging & monitoring  | Built-in CLI and dashboard visibility     |
| Public HTTPS endpoint | Your app is served securely by default    |

---

## 🚀 IBM Cloud Setup (Step-by-step for beginners)

> 🔗 [Official Docs](https://cloud.ibm.com/docs/codeengine?topic=codeengine-getting-started)

1. **Login**

   ```bash
   ibmcloud login --sso
   ```

2. **Install Code Engine plugin**

   ```bash
   ibmcloud plugin install code-engine
   ```

3. **Create/select project**

   ```bash
   ibmcloud ce project create --name flask-project
   ibmcloud ce project select --name flask-project
   ```

4. **Deploy application**

   ```bash
   ibmcloud ce application create \
     --name flask-app \
     --build-source https://github.com/ArjunJagdale/flask-on-codeengine.git \
     --port 8080 \
     --cpu 0.5 --memory 1G \
     --max-scale 3
   ```

5. **Update after changes**

   ```bash
   ibmcloud ce application update \
     --name flask-app \
     --build-source https://github.com/ArjunJagdale/flask-on-codeengine.git
   ```

## 🚀 IBM Cloud Deployment Instructions

### ✅ Prerequisites

- IBM Cloud CLI installed (`ibmcloud`)
- Code Engine plugin installed (`ibmcloud plugin install code-engine`)
- IBM Cloud account & project setup

### 🔧 Steps

```bash
# Login
ibmcloud login --sso

# Target your resource group
ibmcloud target -g Default -r us-south

# Select Code Engine project
ibmcloud ce project select --name flask-project

# Deploy the app (first time)
ibmcloud ce application create \
  --name flask-app \
  --build-source https://github.com/ArjunJagdale/flask-on-codeengine.git \
  --port 8080 \
  --cpu 0.5 --memory 1G \
  --max-scale 3

# Update the app (after code changes)
ibmcloud ce application update \
  --name flask-app \
  --build-source https://github.com/ArjunJagdale/flask-on-codeengine.git
````

---

## 👨‍💻 Author

**Arjun Jagdale**
💼 ML + Cloud Developer | IBM Cloud Enthusiast
📫 [arjunjagdale14@email.com](mailto:arjunjagdale14@email.com)
🌐 [github.com/ArjunJagdale](https://github.com/ArjunJagdale)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).

```

Let me know if you want help with GitHub Actions to **auto-deploy on push**, or a version with **Cloudant DB** support!
```
