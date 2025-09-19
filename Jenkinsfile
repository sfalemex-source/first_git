pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    python main.py
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline завершен!'
        }
        success {
            echo '✅ Все тесты прошли успешно!'
        }
        failure {
            echo '❌ Некоторые тесты провалены!'
        }
    }
}