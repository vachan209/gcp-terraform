pipeline {
    agent any

    stages {
        stage('git checkout')
        {
            step{
                git branch: 'main', url: 'https://github.com/vachan209/gcp-terraform.git'
            }
        }
    }
}