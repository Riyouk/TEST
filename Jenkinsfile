pipeline {
    agent any 

    stages{
        stage("checkout code"){
            steps{
                git credentialId : 'pathelloworld' , url : "https://github.com/Riyouk/TEST.git" , branch : "main"
            }
        }

        stage("install dependencies"){
                bat ''' 
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirement.txt
                    '''
        }

    stage('run test'){
        steps{
            bat '''
                call venv\\Scripts\\activate
                pytest test_reg.py
                '''
        }
    }
    
    stage('deploy'){
        steps {
            echo "deploying application !"

            bat '''
                call\\venv\\Scripts\\activate
                python student_register.py
                '''

                
        }
    }
}

post{
    success{
        echo 'pipeline succeded'
    }
    failure{
        echo 'pipeline failed'
    }
}
}