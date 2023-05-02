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
               sudo mkdir -p $WORKSPACE/config/gcloud
              
               """
                }
            }
        }
           
    }
}