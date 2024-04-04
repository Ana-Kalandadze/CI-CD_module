pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'feature/adventure-works-test', url: 'https://github.com/Ana-Kalandadze/CI-CD_module.git'
            }
        }
        stage('Set Up Environment') {
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Python Tests') {
            steps {
                sh 'AdventureWorks2012_test.py'
            }
        }
    }
}
