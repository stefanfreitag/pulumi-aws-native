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

// The AWS::EC2::TransitGatewayPeeringAttachment type
func LookupTransitGatewayPeeringAttachment(ctx *pulumi.Context, args *LookupTransitGatewayPeeringAttachmentArgs, opts ...pulumi.InvokeOption) (*LookupTransitGatewayPeeringAttachmentResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupTransitGatewayPeeringAttachmentResult
	err := ctx.Invoke("aws-native:ec2:getTransitGatewayPeeringAttachment", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupTransitGatewayPeeringAttachmentArgs struct {
	// The ID of the transit gateway peering attachment.
	TransitGatewayAttachmentId string `pulumi:"transitGatewayAttachmentId"`
}

type LookupTransitGatewayPeeringAttachmentResult struct {
	// The time the transit gateway peering attachment was created.
	CreationTime *string `pulumi:"creationTime"`
	// The state of the transit gateway peering attachment. Note that the initiating state has been deprecated.
	State *string `pulumi:"state"`
	// The status of the transit gateway peering attachment.
	Status *TransitGatewayPeeringAttachmentPeeringAttachmentStatus `pulumi:"status"`
	// The tags for the transit gateway peering attachment.
	Tags []aws.Tag `pulumi:"tags"`
	// The ID of the transit gateway peering attachment.
	TransitGatewayAttachmentId *string `pulumi:"transitGatewayAttachmentId"`
}

func LookupTransitGatewayPeeringAttachmentOutput(ctx *pulumi.Context, args LookupTransitGatewayPeeringAttachmentOutputArgs, opts ...pulumi.InvokeOption) LookupTransitGatewayPeeringAttachmentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTransitGatewayPeeringAttachmentResult, error) {
			args := v.(LookupTransitGatewayPeeringAttachmentArgs)
			r, err := LookupTransitGatewayPeeringAttachment(ctx, &args, opts...)
			var s LookupTransitGatewayPeeringAttachmentResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTransitGatewayPeeringAttachmentResultOutput)
}

type LookupTransitGatewayPeeringAttachmentOutputArgs struct {
	// The ID of the transit gateway peering attachment.
	TransitGatewayAttachmentId pulumi.StringInput `pulumi:"transitGatewayAttachmentId"`
}

func (LookupTransitGatewayPeeringAttachmentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTransitGatewayPeeringAttachmentArgs)(nil)).Elem()
}

type LookupTransitGatewayPeeringAttachmentResultOutput struct{ *pulumi.OutputState }

func (LookupTransitGatewayPeeringAttachmentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTransitGatewayPeeringAttachmentResult)(nil)).Elem()
}

func (o LookupTransitGatewayPeeringAttachmentResultOutput) ToLookupTransitGatewayPeeringAttachmentResultOutput() LookupTransitGatewayPeeringAttachmentResultOutput {
	return o
}

func (o LookupTransitGatewayPeeringAttachmentResultOutput) ToLookupTransitGatewayPeeringAttachmentResultOutputWithContext(ctx context.Context) LookupTransitGatewayPeeringAttachmentResultOutput {
	return o
}

// The time the transit gateway peering attachment was created.
func (o LookupTransitGatewayPeeringAttachmentResultOutput) CreationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayPeeringAttachmentResult) *string { return v.CreationTime }).(pulumi.StringPtrOutput)
}

// The state of the transit gateway peering attachment. Note that the initiating state has been deprecated.
func (o LookupTransitGatewayPeeringAttachmentResultOutput) State() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayPeeringAttachmentResult) *string { return v.State }).(pulumi.StringPtrOutput)
}

// The status of the transit gateway peering attachment.
func (o LookupTransitGatewayPeeringAttachmentResultOutput) Status() TransitGatewayPeeringAttachmentPeeringAttachmentStatusPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayPeeringAttachmentResult) *TransitGatewayPeeringAttachmentPeeringAttachmentStatus {
		return v.Status
	}).(TransitGatewayPeeringAttachmentPeeringAttachmentStatusPtrOutput)
}

// The tags for the transit gateway peering attachment.
func (o LookupTransitGatewayPeeringAttachmentResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupTransitGatewayPeeringAttachmentResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

// The ID of the transit gateway peering attachment.
func (o LookupTransitGatewayPeeringAttachmentResultOutput) TransitGatewayAttachmentId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayPeeringAttachmentResult) *string { return v.TransitGatewayAttachmentId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTransitGatewayPeeringAttachmentResultOutput{})
}
