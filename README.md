# Mass Email Sending using AWS Serverless Services
Mass emailing is a common requirement for businesses, organizations, and individuals alike. However, sending a large number of emails manually can be time-consuming and error-prone. One way to automate this process is by using Amazon Web Services:
1)AWS Lambda-AWS Lambda is a serverless computing service that allows you to run code without provisioning or managing servers
2)CloudWatch-CloudWatch is a monitoring service that provides data and actionable insights for AWS resources
3)IAM Role- IAM (Identity and Access Management) is a service that helps you securely control access to AWS resources
4)Simple Email Service (SES)- IAM (Identity and Access Management) is a service that helps you securely control access to AWS resources
In this article, we will discuss how to use these services to create a mass emailing solution.
Step 1: Creating IAM Role
In the AWS console search for IAM in the search bar and select the service
In that select roles and click on Create role
Select use cases as Lambda and click on next
In permission, policies choose CloudWatch full access and SES full access and then click on next
Give a suitable name for the role and click on Create role
The role will be created.
![image](https://user-images.githubusercontent.com/93040835/232531566-1a556a33-271a-4b6f-9b89-2bf8cda9e2d8.png)
