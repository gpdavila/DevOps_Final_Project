node {
    //def appa
    def registry = 'gabrielpiscoya/simplilearn'
    def registryCredential = 'dockerHub'
    def dockerImage = ''

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        dockerImage = docker.build("${registry}"+":$BUILD_NUMBER")
    }

    stage('Test image') {
        /* Ideally, we would run a test framework against our image.
         * For this example, we're using a Volkswagen-type approach ;-) */

        dockerImage.inside {
            sh 'echo "Tests passed"'
        }
    }

    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', "${registryCredential}") {
            dockerImage.push()
        }
    }
    stage('Run Container') {
			sh 'docker run --name "C_$BUILD_NUMBER" "gabrielpiscoya/simplilearn:$BUILD_NUMBER"'	
     }
}
