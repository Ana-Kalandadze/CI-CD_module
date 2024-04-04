pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python environment') {
            steps {
                script {
                    sh '''
                    python3 -m venv env
                    . env/bin/activate
                    py_version=$(python3 --version)
                    pip_version=$(pip --version)
                    echo "Python version : $py_version"
                    echo "Pip version : $pip_version"
                    '''
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    sh '''
                    . env/bin/activate
                    pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    sh '''
                    . env/bin/activate
                    python3 -m pytest AdventureWorks2012_test.py
                    '''
                }
            }
        }
    post {
        success {
            script {
                checkout([
                    $class: 'GitSCM', 
                    branches: [[name: '*/main']],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [[$class: 'LocalBranch', localBranch: 'main']],
                    submoduleCfg: [],
                    userRemoteConfigs: [[url: 'https://github.com/Ana-Kalandadze/CI-CD_module.git']]
                ])
                
                sh '''
                git add -A 
                git commit -m "Passing all tests, pushing to main"
                git push origin main
                '''   
            }
           
        }
    }
}