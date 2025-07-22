pipeline {
    agent any

    options {
        // Automatically clean workspace before build
        skipDefaultCheckout(true)
        // Keep only last 10 builds
        buildDiscarder(logRotator(numToKeepStr: '10'))
        // Set build timeout
        timeout(time: 30, unit: 'MINUTES')
    }

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

        stage('Check Docker') {
            steps {
                script {
                    sh 'docker --version'
                    sh 'whoami'
                    echo 'Docker is ready!'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image: devproject1-image:${env.BUILD_NUMBER}"
                    // Build with build number tag for better tracking
                    def image = docker.build("devproject1-image:${env.BUILD_NUMBER}")
                    // Also tag as latest
                    image.tag('latest')
                    echo 'Docker image built successfully!'
                }
            }
        }

        stage('Run App in Container') {
            steps {
                script {
                    echo "Running application in container: devproject1-image:${env.BUILD_NUMBER}"
                    // Use the specific build image
                    docker.image("devproject1-image:${env.BUILD_NUMBER}").inside {
                        sh 'python main.py'
                    }
                }
            }
        }

        stage('Cleanup Docker Images') {
            steps {
                script {
                    echo 'Cleaning up old Docker images...'
                    sh '''
                        # Remove dangling images
                        docker image prune -f

                        # Get list of devproject1-image tags (numbers only), keep last 3
                        OLD_IMAGES=$(docker images devproject1-image --format "{{.Repository}}:{{.Tag}}" | grep -E ':([0-9]+)$' | sort -t: -k2 -n | head -n -3)

                        if [ ! -z "$OLD_IMAGES" ]; then
                            echo "Removing old images: $OLD_IMAGES"
                            echo "$OLD_IMAGES" | xargs docker rmi || true
                        else
                            echo "No old images to remove"
                        fi
                    '''
                }
            }
        }
    }

    post {
        always {
            // Clean workspace after build
            cleanWs()
            echo 'Pipeline completed - workspace cleaned'
        }
        success {
            echo '✅ Pipeline succeeded!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}