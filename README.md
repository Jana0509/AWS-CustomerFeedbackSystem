# AWS-CustomerFeedbackSystem
CustomerFeedbackSystem is build on AWS serverless services such as API Gateway, Lambda and Dynamo DB

# Scenario
# “Customer Feedback API”

Imagine you’re building a service where users can submit feedback via a web or mobile app. The system should:

1. Expose an API to accept feedback.
2. Process and store feedback data in DynamoDB.
3. Allow querying for specific feedback based on user ID.
   
# ARCHITECTURE DIAGRAM:

![image](https://github.com/user-attachments/assets/18a1caea-d95c-4707-9d4c-130bdd9bb6aa)

# Services Used:

we are going to make use of below serverless AWS services to build this API

**1. API GATEWAY :** It is used to create, publish, monitor your HTTP/REST API

**2.LAMBDA :** It helps to run your code and perform the business logic without provisioning the infrastructure.

**DYNAMO DB :** It’s the No-SQL DB store where you can store your non relational data.

**LET’S START BUILDING IT!**

Normally, it’s always the great way to backtrack things while building the system. So we are going to start creating from Dynamo DB

# CREATE DYNAMO DB:
1. Navigate to the AWS Management Console, and go to the DynamoDB service and click create table
2. Provide the table name, partition key which is the primary key and sort key as below and click create by keeping other fields as default values.


![image](https://github.com/user-attachments/assets/131d9ffc-0cd0-4cbc-b297-3b9bd8d89323)


# CREATE LAMBDA FUNCTION:
1.Navigate to the AWS Management Console, and go to the Lambda and click create function.
2. Give Function name and choose the runtime, Lambda supports various programming language such as python, nodejs, .net and etc. Choose your Runtime.

![image](https://github.com/user-attachments/assets/64f3a522-a01b-4404-93e4-56d8cfe9b97a)

3. Now, we have to set execution role to lambda, so that lambda can access dynamo db. we are going to create the role for lambda by providing the access to dynamo db.

For this, select — IAM Console hyperlink

![image](https://github.com/user-attachments/assets/78b18fbf-22d0-4c10-8e9e-e2cff5bb458c)

4. Select AWS service and choose Lambda in service

   ![image](https://github.com/user-attachments/assets/8a773eb8-ff58-4f8f-a0fb-f3e1151f3c23)

5. Search “AmazonDynamoDBFullAccess” permission and select and click next. In production environment, it is always recommended to give table level access. Here for simplicity, we have provided “DynamoDBFullAccess”

   ![image](https://github.com/user-attachments/assets/a0b9bca2-0688-47f2-8639-1998c0840e66)

6. Provide the Role name and create it.

   ![image](https://github.com/user-attachments/assets/07553348-e4f1-4cc6-9fe3-2bfe5da203ce)

Now your role is created to attach with the Lambda.

7. In Lambda tab, use an existing role -”LambdaRoleForDDB” which we created in previous steps and click “create Function”

   ![image](https://github.com/user-attachments/assets/0c81350a-6223-4f31-a435-96b5418f1580)

8. Add Code: Use the following example code for Python (replace with your logic if needed):

   ![image](https://github.com/user-attachments/assets/55b4e4e2-63c9-4c7d-9daf-08381befbdf3)

FYI : You can find the above code in Github- https://github.com/Jana0509/AWS-CustomerFeedbackSystem/tree/main


# CREATE API GATEWAY:
1. Navigate to the AWS API Gateway in AWS Console and choose API type as HTTP API

   ![image](https://github.com/user-attachments/assets/a1371e14-a5ba-413d-84a0-d8455cbc3ee7)

2. Create an API, select integration as Lambda as API gateway is integrating with lambda and choose the region and lambda function which we created in the last step. Provide the API name and click next.

   ![image](https://github.com/user-attachments/assets/a7184366-b4fd-4b0b-b076-1be50c5dc28f)

3. Configure route by selecting method type as “post” and provide resource path and click next.

   ![image](https://github.com/user-attachments/assets/6ab3f572-4669-4a89-be29-ad3e7818b5c7)

4. Add stage as dev, stage or prod. We are setting the stages of deployment. we can have as many stages you want and deploy from lower environment to prod for validating the service.

   ![image](https://github.com/user-attachments/assets/f0f7577d-9586-4a41-ba65-104574feb0b2)

Click Review and create

5. Choose Stage name (e.g., dev or prod) and Click Deploy.

6. Get API URL: After deployment, you’ll be given an API endpoint URL. This will be the URL that clients can send requests to, such as https://<api-id>.execute-api.<region>.amazonaws.com/dev

# TEST FROM POSTMAN:

1. Hit the API Gateway URL with the Body as mentioned below

![image](https://github.com/user-attachments/assets/32ca0419-1086-411e-8d50-f8f225d9be34)


2. Verify that the feedback data is correctly stored in DynamoDB. We can see the feedback data is inserted in dynamo db.

   ![image](https://github.com/user-attachments/assets/cc584ec2-491f-47b7-9a69-4f0be9a3de46)


# Optional Enhancements
**Validation**: Add input validation to Lambda.
**Authentication**: Use Amazon Cognito or an API Gateway key for secure access.
**Monitoring**: Enable CloudWatch logging for Lambda and API Gateway.


# Enable Cloudwatch Logging for the Lambda:

1. Go to IAM -> Roles -> “LambdaRoleForDDB” which we created for the lambda to access Dynamo DB.
   
   ![image](https://github.com/user-attachments/assets/256aae5c-a502-4611-8e63-0cf7c2ee97f1)

2. Under Permission Policies, click Attach Policies and search for “AWSLambdaBasicExecutionRole” and add that policy for the role.

   ![image](https://github.com/user-attachments/assets/8166dfc1-b356-4e52-9107-524bbccf0093)

3. After Adding the policy, now your lambda can write logs to the cloudwatch.

4. To view the logs, Go to Cloudwatch in console and click log groups.

5. Under Log Groups, Feedback Handler Log group would be created.

   ![image](https://github.com/user-attachments/assets/39a0bffc-15b6-4453-9f55-636b669c3be5)

6. Go to the Log events to view the logs

   ![image](https://github.com/user-attachments/assets/6afc0592-48cf-4cb9-94ee-5cf5e37f0d6d)

# Conclusion Analogy :
**Putting It All Together**
In this analogy:

* **API Gateway** is the first point of contact, ensuring all customers are properly routed to the kitchen (Lambda).
* **Lambda** (the chef) processes the feedback based on the request type, either storing new feedback or retrieving existing feedback.
* **DynamoDB** is where all the feedback is stored, like a digital ledger that the chef consults whenever feedback needs to be added or retrieved.
  
This system allows customers (users) to easily submit their feedback and view it later, just like a restaurant using a well-organized process to track and respond to guest comments.

**Congratulations**! You successfully created Customer feedback system using AWS serverless services and learned how these services are tied together to produce the awesome output!

**Remember, don’t forget to delete all resources created and configured when you are done following the steps of this article.**

If you’ve got this far, thanks for reading! I hope it was worthwhile to you.

Signing off!

**Jana**
