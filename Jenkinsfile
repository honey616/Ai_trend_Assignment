pipeline {
    agent any

    environment {
        DOCKERHUB_CRED = credentials('dockerhub-cred')
        IMAGE_NAME = "honey616/python-greet-app"
        TAG = "latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/<your-username>/<your-repo>.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%TAG% .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                bat '''
                echo %DOCKERHUB_CRED_PSW% | docker login -u %DOCKERHUB_CRED_USR% --password-stdin
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                bat 'docker push %IMAGE_NAME%:%TAG%'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --rm %IMAGE_NAME%:%TAG%'
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline execution completed!'
        }
    }
}
