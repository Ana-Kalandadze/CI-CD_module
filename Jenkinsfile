pipeline {
    agent any 

    stages {
        stage('Build') { 
            steps { 
                echo 'Building.. Just Checking out the code from git' 
                checkout scm 
            }
        }
        stage('Test') { 
            steps { 
                echo 'Testing.. Just printing Hello, World!'
                sh 'echo "Hello, World!"' 
            }
        }
        stage('Deploy') { 
            steps {
                echo 'Deploying.... For now just echo it!'
                sh 'echo "Deploying!!"'
            }
        }
    }
}