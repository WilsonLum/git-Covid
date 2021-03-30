pipeline {
  agent any
  stages {
    stage('Stage1') {
      steps {
        echo "This is the build number $BUILD_NUMBER of job demo $DEMO"
        sh '''
           echo "Using multi line shell step"
           chmod +x test.sh
           ./test.sh
        '''
      }
    }

  }
  environment {
    DEMO = '1.3'
  }
}
