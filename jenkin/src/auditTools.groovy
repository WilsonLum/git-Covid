library identifier: 'jenkin@main', 
        retriever: modernSCM([$class: 'GitSCMSource', remote: 'https://github.com/WilsonLum/git-Covid'])

pipeline {
    agent any
    stages {
        stage('Audit tools') {                        
            steps {
                auditTools()
            }
        }
    }
}
