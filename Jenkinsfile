pipeline {
    agent any
    
    stages {
        stage('Set Up Environment') {
            steps {
                sh 'apt update'
                sh 'apt install -y python3.11-venv'
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
            }}
        stage('Run Python Tests') {
            steps {
                sh 'python3 AdventureWorks2012_test.py'
            }
        }
    }
}
