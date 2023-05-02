pipeline {
    agent any

    stages {
        stage('git checkout')
        {
            steps{
                git branch: 'main', url: 'https://github.com/vachan209/gcp-terraform.git'
            }
        }
        stage('terraform init'){
            steps{
                sh 'terraform init'
            }
        }
        stage('gcp credentials'){
            steps{
                withCredentials([file(credentialsId: 'credentials', variable: 'gcp_cred')]){
                    sh """
               mkdir -p $WORKSPACE/.config/gcloud
               echo `$gcp_cred` > $WORKSPACE/.config/gcloud/credentials.json
               """
                }
            }
        }
           
    }
}