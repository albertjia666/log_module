pipeline {
    agent any  //在可用的节点运行
    stages{　　　　stage ('Prepare'){
            steps{          //清空发布目录
                bat '''if exist D:\\publish\\LoginServiceCore (rd/s/q D:\\publish\\LoginServiceCore)
                       if exist C:\\Users\\Administrator\\.nuget (rd/s/q C:\\Users\\Administrator\\.nuget) exit''' } } 
       //拉取git代码仓库
       stage ('Checkout'){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], 
                    userRemoteConfigs: [[credentialsId: 'c6d98bbd-5cfb-4e26-aa56-f70b054b350d', 
                    url: 'http://xxx/xxx/xxx']]])
            　　　　　　}
        　　　　}

       //构建
       stage ('Build'){
        　　steps{
        　　　　　bat '''cd "D:\\Program Files (x86)\\Jenkins\\workspace\\LoginServiceCore\\LoginApi.Hosting.Web"
            　　　　　　dotnet restore
            　　　　　　dotnet build
            　　　　　　dotnet publish --configuration Release --output D:\\publish\\LoginServiceCore'''
            　　　　　　}
        　　　　}
    
       //部署
    　　stage ('Deploy'){
        　　steps{
           　　　 bat '''cd D:\\PipelineScript\\LoginServiceCore
            　　　　　　python LoginServiceCore.py'''
           　　　　　　 }
        　　　　　}
        
   　　 //自动化测试（python代码实现）
    　　stage ('Test'){
        　　steps{
            　　　bat'''cd D:\\PipelineScript\\LoginServiceCore
            　　python LoginServiceCoreApitest.py'''   
            　　　　　　}
        　　　　 }
    }
 }