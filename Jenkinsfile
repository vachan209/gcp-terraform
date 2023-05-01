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
         stage('terraform validate'){
            steps{
                sh 'terraform validate'
            }
        }
         stage('terraform validate'){
            steps{
                sh 'terraform validate'
            }
        }
    }
}