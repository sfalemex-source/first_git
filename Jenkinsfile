pipeline {
    agent any

    stages {
        stage('Clone repository') {
            steps {
                echo 'Репозиторий уже клонирован автоматически'
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
            echo '✅ Тесты прошли успешно!'
        }
        failure {
            echo '❌ Тесты провалены!'
        }
    }
}