## AWS Application Load Balancer Session Stickiness

Implement session stickiness using AWS Application load balancer. 

To accomplish this, we have to follow these steps: 

1. Provision the environment in AWS using cloud formation. 
2. Verify the EC2 instances are up and running.
3. Verify the application load balancer using the DNS and make sure that the traffic is distributed across the target groups (EC2s). 
4. Enable the session stickiness on the application load balancer. 
5. Verify the session stickiness to see if been locked to one instance. 
6. Shutdown the instance and check the behavior of ALB to see where traffic is diverted to and then check stickiness behavior. 
7. Restart the instance and check if stickiness is still hold good with new instance. 
8. Disable the stickiness and see if traffic is again disbributed. 
9. clean up 


### Provision the AWS Environment 

You can use this <a href="https://github.com/hsiddhu2/learn-aws-labs/blob/main/Simple/Sticky%20Sessions/setup/ALB_Stickiness.yaml" target="_blank">CF template</a> to provision the environment. 