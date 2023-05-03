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
                    rm $WORKSPACE/config/gcloud/credentials.json
                    echo \$(cat \$gcp_cred) >> $WORKSPACE/config/gcloud/credentials.json
                    
               """
                }
            }
        }
        stage('terraform plan'){
            steps{
               dir('terraform-v1.4/cloud_composer'){
                sh """
                 terraform apply -auto-approve -var 'gcp_creds_path=$WORKSPACE/config/gcloud'
                """
               }
            }
        }

        stage ('build and run docker image'){
            steps{
                sh """
                docker build -t git_to_gcs --build-arg KEYFILE="config/gcloud" .
                docker run git_to_gcs:latest
                """
            }
        }

           
    }
}