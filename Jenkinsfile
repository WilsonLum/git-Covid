pipeline {
  agent any
  stages {
    stage('Stage1') {
      steps {
        echo 'This is the build number $BUILD_NUMBER of job demo $DEMO'
        sh 'echo "THis is the build number $BUILD_NUMBER for demo $DEMO"'
      }
    }

  }
  environment {
    DEMO = '1'
  }
}