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
                    if (isUnix()) {
                        sh '''
                        python3 -m venv env
                        . env/bin/activate
                        py_version=$(python3 --version)
                        pip_version=$(pip --version)
                        echo "Python version : $py_version"
                        echo "Pip version : $pip_version"
                        '''
                    } else {
                        bat '''
                        python3 -m venv env
                        .\\env\\Scripts\\activate
                        py_version=$(python3 --version)
                        pip_version=$(pip --version)
                        echo "Python version : $py_version"
                        echo "Pip version : $pip_version"
                        '''
                    }
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                        . env/bin/activate
                        pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                        .\\env\\Scripts\\activate
                        pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                        . env/bin/activate
                        python3 AdventureWorks2012_test.py
                        '''
                    } else {
                        bat '''
                        .\\env\\Scripts\\activate
                        python3 AdventureWorks2012_test.py
                        '''
                    }
                }
            }
        }
    }
}