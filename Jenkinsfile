pipeline {
    agent any

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Clone Repository') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('devproject1-image')
                }
            }
        }

        stage('Run App in Container') {
            steps {
                script {
                    docker.image('devproject1-image').inside {
                        sh 'python main.py'
                    }
                }
            }
        }
    }
}
