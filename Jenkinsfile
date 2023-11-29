pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'your-django-app:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    git 'https://github.com/yourusername/yourdjangoapp.git'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Run Tests in Docker') {
            steps {
                script {
                    sh 'docker run $DOCKER_IMAGE python manage.py test'
                }
            }
        }

        stage('Deploy to Production') {
            steps {
                script {
                    // Your deployment steps go here
                    // e.g., docker push to a registry, deploy to production
                }
            }
        }
    }
}
