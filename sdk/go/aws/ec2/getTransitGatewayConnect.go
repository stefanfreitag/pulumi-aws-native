// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::EC2::TransitGatewayConnect type
func LookupTransitGatewayConnect(ctx *pulumi.Context, args *LookupTransitGatewayConnectArgs, opts ...pulumi.InvokeOption) (*LookupTransitGatewayConnectResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupTransitGatewayConnectResult
	err := ctx.Invoke("aws-native:ec2:getTransitGatewayConnect", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupTransitGatewayConnectArgs struct {
	// The ID of the Connect attachment.
	TransitGatewayAttachmentId string `pulumi:"transitGatewayAttachmentId"`
}

type LookupTransitGatewayConnectResult struct {
	// The creation time.
	CreationTime *string `pulumi:"creationTime"`
	// The state of the attachment.
	State *string `pulumi:"state"`
	// The tags for the attachment.
	Tags []aws.Tag `pulumi:"tags"`
	// The ID of the Connect attachment.
	TransitGatewayAttachmentId *string `pulumi:"transitGatewayAttachmentId"`
	// The ID of the transit gateway.
	TransitGatewayId *string `pulumi:"transitGatewayId"`
}

func LookupTransitGatewayConnectOutput(ctx *pulumi.Context, args LookupTransitGatewayConnectOutputArgs, opts ...pulumi.InvokeOption) LookupTransitGatewayConnectResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTransitGatewayConnectResult, error) {
			args := v.(LookupTransitGatewayConnectArgs)
			r, err := LookupTransitGatewayConnect(ctx, &args, opts...)
			var s LookupTransitGatewayConnectResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTransitGatewayConnectResultOutput)
}

type LookupTransitGatewayConnectOutputArgs struct {
	// The ID of the Connect attachment.
	TransitGatewayAttachmentId pulumi.StringInput `pulumi:"transitGatewayAttachmentId"`
}

func (LookupTransitGatewayConnectOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTransitGatewayConnectArgs)(nil)).Elem()
}

type LookupTransitGatewayConnectResultOutput struct{ *pulumi.OutputState }

func (LookupTransitGatewayConnectResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTransitGatewayConnectResult)(nil)).Elem()
}

func (o LookupTransitGatewayConnectResultOutput) ToLookupTransitGatewayConnectResultOutput() LookupTransitGatewayConnectResultOutput {
	return o
}

func (o LookupTransitGatewayConnectResultOutput) ToLookupTransitGatewayConnectResultOutputWithContext(ctx context.Context) LookupTransitGatewayConnectResultOutput {
	return o
}

// The creation time.
func (o LookupTransitGatewayConnectResultOutput) CreationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayConnectResult) *string { return v.CreationTime }).(pulumi.StringPtrOutput)
}

// The state of the attachment.
func (o LookupTransitGatewayConnectResultOutput) State() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayConnectResult) *string { return v.State }).(pulumi.StringPtrOutput)
}

// The tags for the attachment.
func (o LookupTransitGatewayConnectResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupTransitGatewayConnectResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

// The ID of the Connect attachment.
func (o LookupTransitGatewayConnectResultOutput) TransitGatewayAttachmentId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayConnectResult) *string { return v.TransitGatewayAttachmentId }).(pulumi.StringPtrOutput)
}

// The ID of the transit gateway.
func (o LookupTransitGatewayConnectResultOutput) TransitGatewayId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayConnectResult) *string { return v.TransitGatewayId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTransitGatewayConnectResultOutput{})
}
