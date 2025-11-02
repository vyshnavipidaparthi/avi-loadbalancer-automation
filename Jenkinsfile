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
                echo " Installing Python and setting up virtual environment..."
                sh '''
                apt-get update
                apt-get install -y python3 python3-venv python3-pip
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
                    python main.py || echo " main.py failed or returned error"
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
