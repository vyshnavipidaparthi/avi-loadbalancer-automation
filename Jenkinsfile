pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo " Pulling code from GitHub..."
                git branch: 'main', url: 'https://github.com/vyshnavipidaparthi/avi-loadbalancer-automation.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo " Setting up Python environment..."
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt || true
                '''
            }
        }

        stage('Run Automation Script') {
            steps {
                echo " Running main Python automation script..."
                sh '''
                source venv/bin/activate
                python main.py || echo " main.py not found or failed"
                '''
            }
        }
    }

    post {
        success {
            echo " Pipeline completed successfully!"
        }
        failure {
            echo " Pipeline failed. Please check console output."
        }
    }
}
