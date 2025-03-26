pipeline {
    agent any

    stages{
        stage('checkout code'){
            steps {
                git credentialsId: 'pathelloworld' , url : "https://github.com/Riyouk/TEST.git" , branch : 'main'
            }
        }
        stage('install Dependencies') {
            steps{
                bat ''' 
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirement.txt
                    '''
            }
        }

        stage('run test'){
            steps {
                bat '''
                    call venv\\Scripts\\activate 
                    pytest test_reg.py
                    '''
            }
        }
        stage('deploy') {
            steps {
                echo "Deploying application..."

                bat '''
                    call venv\\Scripts\\activate
                    python student_register.py
                    '''
            }
        }
    }   

    post{
        success {
            echo 'pipeline succeeded'
        }
        failure {
            echo 'pipeline failed'
        }
    }
}