pipeline {
    agent any
    environment {
        GCP_CREDS = ""
    }
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
                    mkdir -p $WORKSPACE/config/gcloud
                    sudo chown -R jenkins:jenkins $WORKSPACE
                    sudo chmod -R u+w $WORKSPACE
                    GCP_CREDENTIALS= `cat $gcp_cred`
                    echo "$GCP_CREDENTIALS"
               """
                }
            }
        }
           
    }
}