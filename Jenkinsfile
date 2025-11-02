pipeline {
    agent {
        docker {
            // Use a Python 3.13 image so Jenkins runs the same version as your local setup
            image 'python:3.13'
            args '-u root'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                echo " Pulling code from GitHub..."
                git branch: 'main', url: 'https://github.com/vyshnavipidaparthi/avi-loadbalancer-automation.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo " Setting up virtual environment and installing dependencies..."
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
                else
                    echo " No requirements.txt found, skipping dependency installation."
                fi
                '''
            }
        }

        stage('Run Automation Script') {
            steps {
                echo " Running main Python automation script..."
                sh '''
                . venv/bin/activate
                if [ -f main.py ]; then
                    python main.py
                else
                    echo " main.py not found in repository."
                fi
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
