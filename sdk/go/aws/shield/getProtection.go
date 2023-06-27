// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package shield

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Enables AWS Shield Advanced for a specific AWS resource. The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, AWS Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.
func LookupProtection(ctx *pulumi.Context, args *LookupProtectionArgs, opts ...pulumi.InvokeOption) (*LookupProtectionResult, error) {
	var rv LookupProtectionResult
	err := ctx.Invoke("aws-native:shield:getProtection", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupProtectionArgs struct {
	// The ARN (Amazon Resource Name) of the protection.
	ProtectionArn string `pulumi:"protectionArn"`
}

type LookupProtectionResult struct {
	ApplicationLayerAutomaticResponseConfiguration *ProtectionApplicationLayerAutomaticResponseConfiguration `pulumi:"applicationLayerAutomaticResponseConfiguration"`
	// The Amazon Resource Names (ARNs) of the health check to associate with the protection.
	HealthCheckArns []string `pulumi:"healthCheckArns"`
	// The ARN (Amazon Resource Name) of the protection.
	ProtectionArn *string `pulumi:"protectionArn"`
	// The unique identifier (ID) of the protection.
	ProtectionId *string `pulumi:"protectionId"`
	// One or more tag key-value pairs for the Protection object.
	Tags []ProtectionTag `pulumi:"tags"`
}

func LookupProtectionOutput(ctx *pulumi.Context, args LookupProtectionOutputArgs, opts ...pulumi.InvokeOption) LookupProtectionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupProtectionResult, error) {
			args := v.(LookupProtectionArgs)
			r, err := LookupProtection(ctx, &args, opts...)
			var s LookupProtectionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupProtectionResultOutput)
}

type LookupProtectionOutputArgs struct {
	// The ARN (Amazon Resource Name) of the protection.
	ProtectionArn pulumi.StringInput `pulumi:"protectionArn"`
}

func (LookupProtectionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupProtectionArgs)(nil)).Elem()
}

type LookupProtectionResultOutput struct{ *pulumi.OutputState }

func (LookupProtectionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupProtectionResult)(nil)).Elem()
}

func (o LookupProtectionResultOutput) ToLookupProtectionResultOutput() LookupProtectionResultOutput {
	return o
}

func (o LookupProtectionResultOutput) ToLookupProtectionResultOutputWithContext(ctx context.Context) LookupProtectionResultOutput {
	return o
}

func (o LookupProtectionResultOutput) ApplicationLayerAutomaticResponseConfiguration() ProtectionApplicationLayerAutomaticResponseConfigurationPtrOutput {
	return o.ApplyT(func(v LookupProtectionResult) *ProtectionApplicationLayerAutomaticResponseConfiguration {
		return v.ApplicationLayerAutomaticResponseConfiguration
	}).(ProtectionApplicationLayerAutomaticResponseConfigurationPtrOutput)
}

// The Amazon Resource Names (ARNs) of the health check to associate with the protection.
func (o LookupProtectionResultOutput) HealthCheckArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupProtectionResult) []string { return v.HealthCheckArns }).(pulumi.StringArrayOutput)
}

// The ARN (Amazon Resource Name) of the protection.
func (o LookupProtectionResultOutput) ProtectionArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProtectionResult) *string { return v.ProtectionArn }).(pulumi.StringPtrOutput)
}

// The unique identifier (ID) of the protection.
func (o LookupProtectionResultOutput) ProtectionId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProtectionResult) *string { return v.ProtectionId }).(pulumi.StringPtrOutput)
}

// One or more tag key-value pairs for the Protection object.
func (o LookupProtectionResultOutput) Tags() ProtectionTagArrayOutput {
	return o.ApplyT(func(v LookupProtectionResult) []ProtectionTag { return v.Tags }).(ProtectionTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupProtectionResultOutput{})
}
