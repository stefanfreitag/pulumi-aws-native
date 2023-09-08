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

// The AWS::EC2::TransitGatewayMulticastDomain type
func LookupTransitGatewayMulticastDomain(ctx *pulumi.Context, args *LookupTransitGatewayMulticastDomainArgs, opts ...pulumi.InvokeOption) (*LookupTransitGatewayMulticastDomainResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupTransitGatewayMulticastDomainResult
	err := ctx.Invoke("aws-native:ec2:getTransitGatewayMulticastDomain", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupTransitGatewayMulticastDomainArgs struct {
	// The ID of the transit gateway multicast domain.
	TransitGatewayMulticastDomainId string `pulumi:"transitGatewayMulticastDomainId"`
}

type LookupTransitGatewayMulticastDomainResult struct {
	// The time the transit gateway multicast domain was created.
	CreationTime *string `pulumi:"creationTime"`
	// The options for the transit gateway multicast domain.
	Options *OptionsProperties `pulumi:"options"`
	// The state of the transit gateway multicast domain.
	State *string `pulumi:"state"`
	// The tags for the transit gateway multicast domain.
	Tags []TransitGatewayMulticastDomainTag `pulumi:"tags"`
	// The Amazon Resource Name (ARN) of the transit gateway multicast domain.
	TransitGatewayMulticastDomainArn *string `pulumi:"transitGatewayMulticastDomainArn"`
	// The ID of the transit gateway multicast domain.
	TransitGatewayMulticastDomainId *string `pulumi:"transitGatewayMulticastDomainId"`
}

func LookupTransitGatewayMulticastDomainOutput(ctx *pulumi.Context, args LookupTransitGatewayMulticastDomainOutputArgs, opts ...pulumi.InvokeOption) LookupTransitGatewayMulticastDomainResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTransitGatewayMulticastDomainResult, error) {
			args := v.(LookupTransitGatewayMulticastDomainArgs)
			r, err := LookupTransitGatewayMulticastDomain(ctx, &args, opts...)
			var s LookupTransitGatewayMulticastDomainResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTransitGatewayMulticastDomainResultOutput)
}

type LookupTransitGatewayMulticastDomainOutputArgs struct {
	// The ID of the transit gateway multicast domain.
	TransitGatewayMulticastDomainId pulumi.StringInput `pulumi:"transitGatewayMulticastDomainId"`
}

func (LookupTransitGatewayMulticastDomainOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTransitGatewayMulticastDomainArgs)(nil)).Elem()
}

type LookupTransitGatewayMulticastDomainResultOutput struct{ *pulumi.OutputState }

func (LookupTransitGatewayMulticastDomainResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTransitGatewayMulticastDomainResult)(nil)).Elem()
}

func (o LookupTransitGatewayMulticastDomainResultOutput) ToLookupTransitGatewayMulticastDomainResultOutput() LookupTransitGatewayMulticastDomainResultOutput {
	return o
}

func (o LookupTransitGatewayMulticastDomainResultOutput) ToLookupTransitGatewayMulticastDomainResultOutputWithContext(ctx context.Context) LookupTransitGatewayMulticastDomainResultOutput {
	return o
}

func (o LookupTransitGatewayMulticastDomainResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupTransitGatewayMulticastDomainResult] {
	return pulumix.Output[LookupTransitGatewayMulticastDomainResult]{
		OutputState: o.OutputState,
	}
}

// The time the transit gateway multicast domain was created.
func (o LookupTransitGatewayMulticastDomainResultOutput) CreationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayMulticastDomainResult) *string { return v.CreationTime }).(pulumi.StringPtrOutput)
}

// The options for the transit gateway multicast domain.
func (o LookupTransitGatewayMulticastDomainResultOutput) Options() OptionsPropertiesPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayMulticastDomainResult) *OptionsProperties { return v.Options }).(OptionsPropertiesPtrOutput)
}

// The state of the transit gateway multicast domain.
func (o LookupTransitGatewayMulticastDomainResultOutput) State() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayMulticastDomainResult) *string { return v.State }).(pulumi.StringPtrOutput)
}

// The tags for the transit gateway multicast domain.
func (o LookupTransitGatewayMulticastDomainResultOutput) Tags() TransitGatewayMulticastDomainTagArrayOutput {
	return o.ApplyT(func(v LookupTransitGatewayMulticastDomainResult) []TransitGatewayMulticastDomainTag { return v.Tags }).(TransitGatewayMulticastDomainTagArrayOutput)
}

// The Amazon Resource Name (ARN) of the transit gateway multicast domain.
func (o LookupTransitGatewayMulticastDomainResultOutput) TransitGatewayMulticastDomainArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayMulticastDomainResult) *string { return v.TransitGatewayMulticastDomainArn }).(pulumi.StringPtrOutput)
}

// The ID of the transit gateway multicast domain.
func (o LookupTransitGatewayMulticastDomainResultOutput) TransitGatewayMulticastDomainId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayMulticastDomainResult) *string { return v.TransitGatewayMulticastDomainId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTransitGatewayMulticastDomainResultOutput{})
}
