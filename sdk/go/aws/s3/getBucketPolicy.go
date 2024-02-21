// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package s3

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Applies an Amazon S3 bucket policy to an Amazon S3 bucket. If you are using an identity other than the root user of the AWS-account that owns the bucket, the calling identity must have the “PutBucketPolicy“ permissions on the specified bucket and belong to the bucket owner's account in order to use this operation.
//
//	If you don't have ``PutBucketPolicy`` permissions, Amazon S3 returns a ``403 Access Denied`` error. If you have the correct permissions, but you're not using an identity that belongs to the bucket owner's account, Amazon S3 returns a ``405 Method Not Allowed`` error.
//	  As a security precaution, the root user of the AWS-account that owns a bucket can always use this operation, even if the policy explicitly denies the root user the ability to perform this action.
//	 For more information, see [Bucket policy examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-bucket-policies.html).
//	The following operations are related to ``PutBucketPolicy``:
//	 +   [Create
func LookupBucketPolicy(ctx *pulumi.Context, args *LookupBucketPolicyArgs, opts ...pulumi.InvokeOption) (*LookupBucketPolicyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupBucketPolicyResult
	err := ctx.Invoke("aws-native:s3:getBucketPolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupBucketPolicyArgs struct {
	// The name of the Amazon S3 bucket to which the policy applies.
	Bucket string `pulumi:"bucket"`
}

type LookupBucketPolicyResult struct {
	// A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy [PolicyDocument](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument) resource description in this guide and [Access Policy Language Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html) in the *Amazon S3 User Guide*.
	PolicyDocument interface{} `pulumi:"policyDocument"`
}

func LookupBucketPolicyOutput(ctx *pulumi.Context, args LookupBucketPolicyOutputArgs, opts ...pulumi.InvokeOption) LookupBucketPolicyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupBucketPolicyResult, error) {
			args := v.(LookupBucketPolicyArgs)
			r, err := LookupBucketPolicy(ctx, &args, opts...)
			var s LookupBucketPolicyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupBucketPolicyResultOutput)
}

type LookupBucketPolicyOutputArgs struct {
	// The name of the Amazon S3 bucket to which the policy applies.
	Bucket pulumi.StringInput `pulumi:"bucket"`
}

func (LookupBucketPolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBucketPolicyArgs)(nil)).Elem()
}

type LookupBucketPolicyResultOutput struct{ *pulumi.OutputState }

func (LookupBucketPolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupBucketPolicyResult)(nil)).Elem()
}

func (o LookupBucketPolicyResultOutput) ToLookupBucketPolicyResultOutput() LookupBucketPolicyResultOutput {
	return o
}

func (o LookupBucketPolicyResultOutput) ToLookupBucketPolicyResultOutputWithContext(ctx context.Context) LookupBucketPolicyResultOutput {
	return o
}

// A policy document containing permissions to add to the specified bucket. In IAM, you must provide policy documents in JSON format. However, in CloudFormation you can provide the policy in JSON or YAML format because CloudFormation converts YAML to JSON before submitting it to IAM. For more information, see the AWS::IAM::Policy [PolicyDocument](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html#cfn-iam-policy-policydocument) resource description in this guide and [Access Policy Language Overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-policy-language-overview.html) in the *Amazon S3 User Guide*.
func (o LookupBucketPolicyResultOutput) PolicyDocument() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupBucketPolicyResult) interface{} { return v.PolicyDocument }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupBucketPolicyResultOutput{})
}
