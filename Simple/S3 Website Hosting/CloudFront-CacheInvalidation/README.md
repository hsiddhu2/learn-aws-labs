# CloudFront Cache Invalidation Lambda Function :cloud_with_lightning:

This is a custom CloudFront Cache Invalidation Lambda Function! :rocket:

This Lambda function automatically invalidating CloudFront cache whenever a new objects is added to your S3 bucket. :arrows_counterclockwise:

The main use case is the static website hosting with CloudFront distribution and S3 bucket as origin. :globe_with_meridians: with CI/CD pipeline. :rocket:

## :gear: Functionality

- Triggered by S3 events when new objects are uploaded :inbox_tray:
- Detects the uploaded object and extracts its key :key:
- Uses CloudFront distribution IDs from environment variables to target the right distributions :dart:
- Creates a snazzy invalidation batch for the uploaded object's key :zap:
- Invalidates the cache for two specified distributions :cloud:

## :rocket: Deployment

1. Clone this repository to your local environment:

```bash
git clone https://github.com/yourusername/your-repo.git
```

2. Navigate to the project directory:

```bash
cd your-repo
```

3. Customize the `lambda_function.py` to suit your needs, especially those snappy distribution IDs.

4. Deploy the Lambda function using your favorite method. Feel the power of AWS Management Console, AWS CLI, or Infrastructure as Code (IaC) tools like AWS CloudFormation or Terraform! :computer:

5. Set up these environment variables for the Lambda function:

   - `DISTRIBUTION_ID_1`: ID of the first CloudFront distribution :one:
   - `DISTRIBUTION_ID_2`: ID of the second CloudFront distribution :two:

6. Jazz up your S3 bucket with an event trigger that invokes the Lambda function on every object upload. :tada:

## :sparkles: Usage

1. Upload an object to your supercharged S3 bucket.

2. Like a flash, the Lambda function triggers and zaps the cache for the associated CloudFront distributions.

3. Voilà! Users get served the freshest content from the dazzling CloudFront distributions. :sparkler:

## :bulb: Notes

- Make sure your CloudFront distributions and S3 bucket are already set up before you summon the Lambda magic.

- Cache invalidation can be a bit quirky – it might cause some extra buzz around your origin servers until the cache is all spiffy again.

- Test your Lambda function in a playground before letting it loose on your live stage. Safety first! :construction_worker:

Remember, this Lambda function takes the hassle out of cache management, making your CloudFront and S3 combo even more enchanting! :crystal_ball: