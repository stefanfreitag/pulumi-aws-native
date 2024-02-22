// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appconfig

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AppConfig::Environment
func LookupEnvironment(ctx *pulumi.Context, args *LookupEnvironmentArgs, opts ...pulumi.InvokeOption) (*LookupEnvironmentResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupEnvironmentResult
	err := ctx.Invoke("aws-native:appconfig:getEnvironment", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupEnvironmentArgs struct {
	// The application ID.
	ApplicationId string `pulumi:"applicationId"`
	// The environment ID.
	EnvironmentId string `pulumi:"environmentId"`
}

type LookupEnvironmentResult struct {
	// A description of the environment.
	Description *string `pulumi:"description"`
	// The environment ID.
	EnvironmentId *string `pulumi:"environmentId"`
	// Amazon CloudWatch alarms to monitor during the deployment process.
	Monitors []EnvironmentMonitor `pulumi:"monitors"`
	// A name for the environment.
	Name *string `pulumi:"name"`
	// Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupEnvironmentOutput(ctx *pulumi.Context, args LookupEnvironmentOutputArgs, opts ...pulumi.InvokeOption) LookupEnvironmentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupEnvironmentResult, error) {
			args := v.(LookupEnvironmentArgs)
			r, err := LookupEnvironment(ctx, &args, opts...)
			var s LookupEnvironmentResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupEnvironmentResultOutput)
}

type LookupEnvironmentOutputArgs struct {
	// The application ID.
	ApplicationId pulumi.StringInput `pulumi:"applicationId"`
	// The environment ID.
	EnvironmentId pulumi.StringInput `pulumi:"environmentId"`
}

func (LookupEnvironmentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEnvironmentArgs)(nil)).Elem()
}

type LookupEnvironmentResultOutput struct{ *pulumi.OutputState }

func (LookupEnvironmentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEnvironmentResult)(nil)).Elem()
}

func (o LookupEnvironmentResultOutput) ToLookupEnvironmentResultOutput() LookupEnvironmentResultOutput {
	return o
}

func (o LookupEnvironmentResultOutput) ToLookupEnvironmentResultOutputWithContext(ctx context.Context) LookupEnvironmentResultOutput {
	return o
}

// A description of the environment.
func (o LookupEnvironmentResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEnvironmentResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The environment ID.
func (o LookupEnvironmentResultOutput) EnvironmentId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEnvironmentResult) *string { return v.EnvironmentId }).(pulumi.StringPtrOutput)
}

// Amazon CloudWatch alarms to monitor during the deployment process.
func (o LookupEnvironmentResultOutput) Monitors() EnvironmentMonitorArrayOutput {
	return o.ApplyT(func(v LookupEnvironmentResult) []EnvironmentMonitor { return v.Monitors }).(EnvironmentMonitorArrayOutput)
}

// A name for the environment.
func (o LookupEnvironmentResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEnvironmentResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// Metadata to assign to the environment. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
func (o LookupEnvironmentResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupEnvironmentResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupEnvironmentResultOutput{})
}
