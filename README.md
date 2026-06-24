# 🔗 URL Shortener — Python + AWS

A URL shortener web application built with Python Flask
and designed for AWS DynamoDB deployment, tested locally
using in-memory storage.

## 🚀 Features
- Shorten any long URL instantly
- Redirect to original URL via short code
- Track click count per shortened URL
- REST API with JSON responses
- Clean and responsive frontend UI

## 🛠️ Tech Stack
- **Backend** — Python 3, Flask
- **Database** — AWS DynamoDB (production) / In-memory (local)
- **Deployment** — AWS EC2
- **Frontend** — HTML, CSS, JavaScript
- **Tools** — AWS CLI, Git, GitHub

## ☁️ AWS Architecture
- **EC2** — hosts the Flask application
- **DynamoDB** — stores URL mappings and click statistics
- **IAM** — manages secure access between EC2 and DynamoDB
- **Security Group** — controls inbound traffic on port 5000

## 📁 Project Structure


url-shortener-python-aws/
│
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── templates/
└── index.html      # Frontend UI


## 🔌 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home page |
| POST | /shorten | Shorten a long URL |
| GET | /<short_code> | Redirect to original URL |
| GET | /stats/<short_code> | Get click statistics |

## ▶️ How to Run Locally
```bash
# Clone the repository
git clone https://github.com/Pooja-veerabhadra/url-shortener-python-aws

# Go to project folder
cd url-shortener-python-aws

# Install dependencies
pip install flask boto3

# Run the app
python app.py


Open your browser and go to:
http://localhost:5000


How to Deploy on AWS EC2

# SSH into EC2 instance
ssh -i "mykey.pem" ec2-user@<your-ec2-ip>

# Install Python
sudo yum install python3 pip -y

# Clone project
git clone https://github.com/Pooja-veerabhadra/url-shortener-python-aws

# Install dependencies
pip3 install -r requirements.txt

# Set AWS credentials
export AWS_ACCESS_KEY=your_access_key
export AWS_SECRET_KEY=your_secret_key

# Run the app
python3 app.py

Requirements
flask
boto3


👩‍💻 Author
Pooja V
MCA — Cloud Computing | AWS | Python Developer
GitHub: Pooja-veerabhadra
LinkedIn: pooja-veerabhadra
Email: pooveerabhadra@gmail.com
