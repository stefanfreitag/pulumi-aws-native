// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package shield

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Config the role and list of Amazon S3 log buckets used by the Shield Response Team (SRT) to access your AWS account while assisting with attack mitigation.
func LookupDRTAccess(ctx *pulumi.Context, args *LookupDRTAccessArgs, opts ...pulumi.InvokeOption) (*LookupDRTAccessResult, error) {
	var rv LookupDRTAccessResult
	err := ctx.Invoke("aws-native:shield:getDRTAccess", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDRTAccessArgs struct {
	AccountId string `pulumi:"accountId"`
}

type LookupDRTAccessResult struct {
	AccountId *string `pulumi:"accountId"`
	// Authorizes the Shield Response Team (SRT) to access the specified Amazon S3 bucket containing log data such as Application Load Balancer access logs, CloudFront logs, or logs from third party sources. You can associate up to 10 Amazon S3 buckets with your subscription.
	LogBucketList []string `pulumi:"logBucketList"`
	// Authorizes the Shield Response Team (SRT) using the specified role, to access your AWS account to assist with DDoS attack mitigation during potential attacks. This enables the SRT to inspect your AWS WAF configuration and create or update AWS WAF rules and web ACLs.
	RoleArn *string `pulumi:"roleArn"`
}

func LookupDRTAccessOutput(ctx *pulumi.Context, args LookupDRTAccessOutputArgs, opts ...pulumi.InvokeOption) LookupDRTAccessResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDRTAccessResult, error) {
			args := v.(LookupDRTAccessArgs)
			r, err := LookupDRTAccess(ctx, &args, opts...)
			var s LookupDRTAccessResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDRTAccessResultOutput)
}

type LookupDRTAccessOutputArgs struct {
	AccountId pulumi.StringInput `pulumi:"accountId"`
}

func (LookupDRTAccessOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDRTAccessArgs)(nil)).Elem()
}

type LookupDRTAccessResultOutput struct{ *pulumi.OutputState }

func (LookupDRTAccessResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDRTAccessResult)(nil)).Elem()
}

func (o LookupDRTAccessResultOutput) ToLookupDRTAccessResultOutput() LookupDRTAccessResultOutput {
	return o
}

func (o LookupDRTAccessResultOutput) ToLookupDRTAccessResultOutputWithContext(ctx context.Context) LookupDRTAccessResultOutput {
	return o
}

func (o LookupDRTAccessResultOutput) AccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDRTAccessResult) *string { return v.AccountId }).(pulumi.StringPtrOutput)
}

// Authorizes the Shield Response Team (SRT) to access the specified Amazon S3 bucket containing log data such as Application Load Balancer access logs, CloudFront logs, or logs from third party sources. You can associate up to 10 Amazon S3 buckets with your subscription.
func (o LookupDRTAccessResultOutput) LogBucketList() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDRTAccessResult) []string { return v.LogBucketList }).(pulumi.StringArrayOutput)
}

// Authorizes the Shield Response Team (SRT) using the specified role, to access your AWS account to assist with DDoS attack mitigation during potential attacks. This enables the SRT to inspect your AWS WAF configuration and create or update AWS WAF rules and web ACLs.
func (o LookupDRTAccessResultOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDRTAccessResult) *string { return v.RoleArn }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDRTAccessResultOutput{})
}
