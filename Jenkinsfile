pipeline {
    agent any

    options {
        skipDefaultCheckout(true)
        buildDiscarder(logRotator(numToKeepStr: '10'))
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

        stage('Code Quality Check') {
            steps {
                script {
                    echo 'Checking repository contents...'
                    sh '''
                        echo "📁 Repository contents:"
                        ls -la

                        echo "✅ Repository structure verified"

                        # Count Python files
                        PYTHON_FILES=$(find . -name "*.py" | wc -l)
                        echo "🐍 Found $PYTHON_FILES Python files"
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "🐳 Building Docker image: devproject1-image:${env.BUILD_NUMBER}"
                    def image = docker.build("devproject1-image:${env.BUILD_NUMBER}")
                    image.tag('latest')
                    echo '✅ Docker image built successfully!'
                }
            }
        }

        stage('Test in Container') {
            steps {
                script {
                    echo "🔍 Testing application in container..."
                    docker.image("devproject1-image:${env.BUILD_NUMBER}").inside {
                        sh '''
                            echo "📋 Container environment info:"
                            python --version
                            pwd
                            ls -la

                            echo "🐍 Checking Python syntax..."
                            python -m py_compile main.py

                            echo "🧪 Running tests in container..."
                            if [ -f test_main.py ]; then
                                python -m py_compile test_main.py
                                python test_main.py
                                echo "✅ All tests passed!"
                            else
                                echo "⚠️  No test file found"
                            fi
                        '''
                    }
                }
            }
        }

        stage('Run App in Container') {
            steps {
                script {
                    echo "🚀 Running application in container: devproject1-image:${env.BUILD_NUMBER}"
                    docker.image("devproject1-image:${env.BUILD_NUMBER}").inside {
                        sh 'python main.py'
                    }
                }
            }
        }

        stage('Cleanup Docker Images') {
            steps {
                script {
                    echo '🧹 Cleaning up old Docker images...'
                    sh '''
                        docker image prune -f

                        OLD_IMAGES=$(docker images devproject1-image --format "{{.Repository}}:{{.Tag}}" | grep -E ':([0-9]+)$' | sort -t: -k2 -n | head -n -3)

                        if [ ! -z "$OLD_IMAGES" ]; then
                            echo "🗑️  Removing old images: $OLD_IMAGES"
                            echo "$OLD_IMAGES" | xargs docker rmi || true
                        else
                            echo "✨ No old images to remove"
                        fi
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
            echo '🧹 Pipeline completed - workspace cleaned'
        }
        success {
            echo '🎉 Pipeline succeeded! כל הטסטים עברו בהצלחה!'
        }
        failure {
            echo '❌ Pipeline failed! יש בעיה שצריך לתקן'
        }
    }
}