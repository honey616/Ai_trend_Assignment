pipeline {
    agent any

    environment {
        IMAGE_NAME = "honey616/honey"
        TAG = "latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/honey616/https://github.com/honey616/Ai_trend_Assignment.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t honey616/honey:latest .'
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
            echo '✅ Pipeline execution completed!'
        }
    }
}
