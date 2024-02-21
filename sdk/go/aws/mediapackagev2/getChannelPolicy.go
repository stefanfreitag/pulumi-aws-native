// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mediapackagev2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::MediaPackageV2::ChannelPolicy Resource Type
func LookupChannelPolicy(ctx *pulumi.Context, args *LookupChannelPolicyArgs, opts ...pulumi.InvokeOption) (*LookupChannelPolicyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupChannelPolicyResult
	err := ctx.Invoke("aws-native:mediapackagev2:getChannelPolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupChannelPolicyArgs struct {
	ChannelGroupName string `pulumi:"channelGroupName"`
	ChannelName      string `pulumi:"channelName"`
}

type LookupChannelPolicyResult struct {
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaPackageV2::ChannelPolicy` for more information about the expected schema for this property.
	Policy interface{} `pulumi:"policy"`
}

func LookupChannelPolicyOutput(ctx *pulumi.Context, args LookupChannelPolicyOutputArgs, opts ...pulumi.InvokeOption) LookupChannelPolicyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupChannelPolicyResult, error) {
			args := v.(LookupChannelPolicyArgs)
			r, err := LookupChannelPolicy(ctx, &args, opts...)
			var s LookupChannelPolicyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupChannelPolicyResultOutput)
}

type LookupChannelPolicyOutputArgs struct {
	ChannelGroupName pulumi.StringInput `pulumi:"channelGroupName"`
	ChannelName      pulumi.StringInput `pulumi:"channelName"`
}

func (LookupChannelPolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupChannelPolicyArgs)(nil)).Elem()
}

type LookupChannelPolicyResultOutput struct{ *pulumi.OutputState }

func (LookupChannelPolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupChannelPolicyResult)(nil)).Elem()
}

func (o LookupChannelPolicyResultOutput) ToLookupChannelPolicyResultOutput() LookupChannelPolicyResultOutput {
	return o
}

func (o LookupChannelPolicyResultOutput) ToLookupChannelPolicyResultOutputWithContext(ctx context.Context) LookupChannelPolicyResultOutput {
	return o
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaPackageV2::ChannelPolicy` for more information about the expected schema for this property.
func (o LookupChannelPolicyResultOutput) Policy() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupChannelPolicyResult) interface{} { return v.Policy }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupChannelPolicyResultOutput{})
}
