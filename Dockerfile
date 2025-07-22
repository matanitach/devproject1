FROM python:3.10-slim
WORKDIR /app
COPY . .
CMD ["python", "main.py"]

#docker run -d --name jenkins-fixed -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home --user root jenkins/jenkins:lts