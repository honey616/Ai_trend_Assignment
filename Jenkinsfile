pipeline {
    agent any

    environment {
        DOCKERHUB_CRED = credentials('dockerhub-cred')  // Add this credential in Jenkins
        IMAGE_NAME = "honey616/honey"
        TAG = "latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/honey616/Ai_trend_Assignment.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t honey616/honey:latest .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                bat '''
                echo Honey@123 | docker login -u honey441 --password-stdin
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker push honey616/honey:latest'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --rm honey616/honey:latest'
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline execution completed successfully!'
        }
    }
}
