pipeline{
 agent any

 stages{
  stage('Build Image')
          {
           steps{

           sh ''' docker-compose build'''
           }

          }
  stage('Start Application')
          {
           steps{

            sh ''' docker-compose up -d'''
           }
          }
   stage('Run unit Tests')
           {
             steps{
               sh '''python3 apiTest.py'''
             }
           }
 }

 }
