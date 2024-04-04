pipeline {
    agent any
    
    stages {
        stage('Set Up Environment') {
    steps {
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
