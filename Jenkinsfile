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

        stage('Run tests with Allure') {
            steps {
                sh '''
                    pytest -v --alluredir=./allure-results
                '''
            }
        }
    }

    post {
        always {
            // Генерация Allure отчета
            allure([
                includeProperties: false,
                jdk: '',
                properties: [],
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'allure-results']]
            ])
        }

        success {
            echo '✅ Все тесты прошли успешно!'
        }

        failure {
            echo '❌ Некоторые тесты провалены!'
        }
    }
}