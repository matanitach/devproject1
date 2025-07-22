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
                // Alternative if you need more control:
                // checkout([
                //     $class: 'GitSCM',
                //     branches: [[name: '*/master']],
                //     extensions: [[$class: 'WipeWorkspace']],
                //     userRemoteConfigs: [[
                //         url: 'https://github.com/matanitach/devproject1.git',
                //         credentialsId: '8899c69f-9048-439e-8ba8-fbb0f8ae1b9d'
                //     ]]
                // ])
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build with build number tag for better tracking
                    def image = docker.build("devproject1-image:${env.BUILD_NUMBER}")
                    // Also tag as latest
                    image.tag('latest')
                }
            }
        }

        stage('Run App in Container') {
            steps {
                script {
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
                    // Clean up old images to save disk space
                    sh '''
                        # Remove dangling images
                        docker image prune -f
                        # Optionally remove old build images (keep last 5)
                        docker images devproject1-image --format "table {{.Tag}}" | grep -E '^[0-9]+$' | sort -n | head -n -5 | xargs -r docker rmi devproject1-image: || true
                    '''
                }
            }
        }
    }

    post {
        always {
            // Clean workspace after build
            cleanWs()
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}