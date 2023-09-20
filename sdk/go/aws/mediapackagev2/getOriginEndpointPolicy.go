// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mediapackagev2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::MediaPackageV2::OriginEndpointPolicy Resource Type
func LookupOriginEndpointPolicy(ctx *pulumi.Context, args *LookupOriginEndpointPolicyArgs, opts ...pulumi.InvokeOption) (*LookupOriginEndpointPolicyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupOriginEndpointPolicyResult
	err := ctx.Invoke("aws-native:mediapackagev2:getOriginEndpointPolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupOriginEndpointPolicyArgs struct {
	ChannelGroupName   string `pulumi:"channelGroupName"`
	ChannelName        string `pulumi:"channelName"`
	OriginEndpointName string `pulumi:"originEndpointName"`
}

type LookupOriginEndpointPolicyResult struct {
	Policy interface{} `pulumi:"policy"`
}

func LookupOriginEndpointPolicyOutput(ctx *pulumi.Context, args LookupOriginEndpointPolicyOutputArgs, opts ...pulumi.InvokeOption) LookupOriginEndpointPolicyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupOriginEndpointPolicyResult, error) {
			args := v.(LookupOriginEndpointPolicyArgs)
			r, err := LookupOriginEndpointPolicy(ctx, &args, opts...)
			var s LookupOriginEndpointPolicyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupOriginEndpointPolicyResultOutput)
}

type LookupOriginEndpointPolicyOutputArgs struct {
	ChannelGroupName   pulumi.StringInput `pulumi:"channelGroupName"`
	ChannelName        pulumi.StringInput `pulumi:"channelName"`
	OriginEndpointName pulumi.StringInput `pulumi:"originEndpointName"`
}

func (LookupOriginEndpointPolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupOriginEndpointPolicyArgs)(nil)).Elem()
}

type LookupOriginEndpointPolicyResultOutput struct{ *pulumi.OutputState }

func (LookupOriginEndpointPolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupOriginEndpointPolicyResult)(nil)).Elem()
}

func (o LookupOriginEndpointPolicyResultOutput) ToLookupOriginEndpointPolicyResultOutput() LookupOriginEndpointPolicyResultOutput {
	return o
}

func (o LookupOriginEndpointPolicyResultOutput) ToLookupOriginEndpointPolicyResultOutputWithContext(ctx context.Context) LookupOriginEndpointPolicyResultOutput {
	return o
}

func (o LookupOriginEndpointPolicyResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupOriginEndpointPolicyResult] {
	return pulumix.Output[LookupOriginEndpointPolicyResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupOriginEndpointPolicyResultOutput) Policy() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupOriginEndpointPolicyResult) interface{} { return v.Policy }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupOriginEndpointPolicyResultOutput{})
}
