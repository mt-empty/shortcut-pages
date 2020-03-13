# Apache Maven

> Source: https://maven.apache.org/guides/MavenQuickReferenceCard.pdf

> Aliases: maven, mvn

$ General
    `pom.xml                       {{Configuration file which maintains versioning, dependencies and plugins}} 
    `mvn plugin:target [-Doption1 -Doption2]
>                                  {{General command template, to be executed in pom.xml's directory}} 

$ Creating Project
    `mvn archetype:create          {{Creates minimal pom.xml}} 
    `mvn archetype:create
  -DgroupId=[Artifact Grp]
  -DartifactId=[Artifact ID]
>                                  {{Creates a new jar project directory [Artifact ID] with package structure [Artifact Grp]. Name of the packaged jar will be [Artifact ID]-[version].jar}} 
    `mvn archetype:create
  -DgroupId=[Artifact Grp]
  -DartifactId=[Artifact ID]
  -DarchetypeArtifactId=maven-archetype-webapp
>                                  {{Creates a new war project directory [Artifact ID] with package structure [Artifact Grp]. Name of the packaged war will be [Artifact ID]-[version].war}} 
    `mvn eclipse:eclipse           {{Creates eclipse project structure}} 

$ Build Commands
    `mvn compile                   {{Compiles source code}} 
    `mvn clean                     {{Cleans unwanted files and previous build}} 
    `mvn test                      {{Run test cases}} 
    `mvn clean package             {{Compiles, runs unit tests and packages the artifact (clean makes sure there are no unwanted files in the package)}} 
    `mvn clean package -Dmaven.test.skip=true
>                                  {{Compiles and packages the artifact (clean makes sure there are no unwanted files in the package)}} 

$ Installing Artifact
    `mvn clean install             {{Compiles, runs unit tests, packages and installs the artifact in the local repository. (User Home Directory/.m2/repository/)}} 
    `mvn clean install -Dmaven.test.skip=true
>                                  {{Compiles, packages and installs the artifact in the local repository. (User Home Directory/.m2/repository/)}} 
    `mvn clean deploy              {{Compiles, runs unit tests, packages and installs the artifact in the remote repository (configured in pom.xml)}} 

$ Tomcat Integration (Requires tomcat-maven-plugin)
    `mvn tomcat:run                {{Runs tomcat}} 
    `mvn tomcat:deploy             {{Deploys the war on tomcat server}} 
    `mvn tomcat:undeploy           {{Undeploys the webapp}} 

