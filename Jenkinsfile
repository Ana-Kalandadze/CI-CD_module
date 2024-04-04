pipeline {
    agent any
    
    stages {
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
