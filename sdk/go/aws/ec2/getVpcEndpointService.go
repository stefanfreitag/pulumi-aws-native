// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::EC2::VPCEndpointService
func LookupVpcEndpointService(ctx *pulumi.Context, args *LookupVpcEndpointServiceArgs, opts ...pulumi.InvokeOption) (*LookupVpcEndpointServiceResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupVpcEndpointServiceResult
	err := ctx.Invoke("aws-native:ec2:getVpcEndpointService", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupVpcEndpointServiceArgs struct {
	ServiceId string `pulumi:"serviceId"`
}

type LookupVpcEndpointServiceResult struct {
	AcceptanceRequired      *bool    `pulumi:"acceptanceRequired"`
	GatewayLoadBalancerArns []string `pulumi:"gatewayLoadBalancerArns"`
	NetworkLoadBalancerArns []string `pulumi:"networkLoadBalancerArns"`
	PayerResponsibility     *string  `pulumi:"payerResponsibility"`
	ServiceId               *string  `pulumi:"serviceId"`
}

func LookupVpcEndpointServiceOutput(ctx *pulumi.Context, args LookupVpcEndpointServiceOutputArgs, opts ...pulumi.InvokeOption) LookupVpcEndpointServiceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupVpcEndpointServiceResult, error) {
			args := v.(LookupVpcEndpointServiceArgs)
			r, err := LookupVpcEndpointService(ctx, &args, opts...)
			var s LookupVpcEndpointServiceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupVpcEndpointServiceResultOutput)
}

type LookupVpcEndpointServiceOutputArgs struct {
	ServiceId pulumi.StringInput `pulumi:"serviceId"`
}

func (LookupVpcEndpointServiceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVpcEndpointServiceArgs)(nil)).Elem()
}

type LookupVpcEndpointServiceResultOutput struct{ *pulumi.OutputState }

func (LookupVpcEndpointServiceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVpcEndpointServiceResult)(nil)).Elem()
}

func (o LookupVpcEndpointServiceResultOutput) ToLookupVpcEndpointServiceResultOutput() LookupVpcEndpointServiceResultOutput {
	return o
}

func (o LookupVpcEndpointServiceResultOutput) ToLookupVpcEndpointServiceResultOutputWithContext(ctx context.Context) LookupVpcEndpointServiceResultOutput {
	return o
}

func (o LookupVpcEndpointServiceResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupVpcEndpointServiceResult] {
	return pulumix.Output[LookupVpcEndpointServiceResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupVpcEndpointServiceResultOutput) AcceptanceRequired() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupVpcEndpointServiceResult) *bool { return v.AcceptanceRequired }).(pulumi.BoolPtrOutput)
}

func (o LookupVpcEndpointServiceResultOutput) GatewayLoadBalancerArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupVpcEndpointServiceResult) []string { return v.GatewayLoadBalancerArns }).(pulumi.StringArrayOutput)
}

func (o LookupVpcEndpointServiceResultOutput) NetworkLoadBalancerArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupVpcEndpointServiceResult) []string { return v.NetworkLoadBalancerArns }).(pulumi.StringArrayOutput)
}

func (o LookupVpcEndpointServiceResultOutput) PayerResponsibility() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVpcEndpointServiceResult) *string { return v.PayerResponsibility }).(pulumi.StringPtrOutput)
}

func (o LookupVpcEndpointServiceResultOutput) ServiceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVpcEndpointServiceResult) *string { return v.ServiceId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupVpcEndpointServiceResultOutput{})
}
