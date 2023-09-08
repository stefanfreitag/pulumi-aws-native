// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package networkmanager

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// AWS::NetworkManager::TransitGatewayRouteTableAttachment Resource Type definition.
func LookupTransitGatewayRouteTableAttachment(ctx *pulumi.Context, args *LookupTransitGatewayRouteTableAttachmentArgs, opts ...pulumi.InvokeOption) (*LookupTransitGatewayRouteTableAttachmentResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupTransitGatewayRouteTableAttachmentResult
	err := ctx.Invoke("aws-native:networkmanager:getTransitGatewayRouteTableAttachment", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupTransitGatewayRouteTableAttachmentArgs struct {
	// The ID of the attachment.
	AttachmentId string `pulumi:"attachmentId"`
}

type LookupTransitGatewayRouteTableAttachmentResult struct {
	// The ID of the attachment.
	AttachmentId *string `pulumi:"attachmentId"`
	// The policy rule number associated with the attachment.
	AttachmentPolicyRuleNumber *int `pulumi:"attachmentPolicyRuleNumber"`
	// The type of attachment.
	AttachmentType *string `pulumi:"attachmentType"`
	// The ARN of a core network for the VPC attachment.
	CoreNetworkArn *string `pulumi:"coreNetworkArn"`
	// The ID of a core network where you're creating a site-to-site VPN attachment.
	CoreNetworkId *string `pulumi:"coreNetworkId"`
	// Creation time of the attachment.
	CreatedAt *string `pulumi:"createdAt"`
	// The Region where the edge is located.
	EdgeLocation *string `pulumi:"edgeLocation"`
	// Owner account of the attachment.
	OwnerAccountId *string `pulumi:"ownerAccountId"`
	// The attachment to move from one segment to another.
	ProposedSegmentChange *TransitGatewayRouteTableAttachmentProposedSegmentChange `pulumi:"proposedSegmentChange"`
	// The ARN of the Resource.
	ResourceArn *string `pulumi:"resourceArn"`
	// The name of the segment that attachment is in.
	SegmentName *string `pulumi:"segmentName"`
	// The state of the attachment.
	State *string `pulumi:"state"`
	// An array of key-value pairs to apply to this resource.
	Tags []TransitGatewayRouteTableAttachmentTag `pulumi:"tags"`
	// Last update time of the attachment.
	UpdatedAt *string `pulumi:"updatedAt"`
}

func LookupTransitGatewayRouteTableAttachmentOutput(ctx *pulumi.Context, args LookupTransitGatewayRouteTableAttachmentOutputArgs, opts ...pulumi.InvokeOption) LookupTransitGatewayRouteTableAttachmentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTransitGatewayRouteTableAttachmentResult, error) {
			args := v.(LookupTransitGatewayRouteTableAttachmentArgs)
			r, err := LookupTransitGatewayRouteTableAttachment(ctx, &args, opts...)
			var s LookupTransitGatewayRouteTableAttachmentResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTransitGatewayRouteTableAttachmentResultOutput)
}

type LookupTransitGatewayRouteTableAttachmentOutputArgs struct {
	// The ID of the attachment.
	AttachmentId pulumi.StringInput `pulumi:"attachmentId"`
}

func (LookupTransitGatewayRouteTableAttachmentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTransitGatewayRouteTableAttachmentArgs)(nil)).Elem()
}

type LookupTransitGatewayRouteTableAttachmentResultOutput struct{ *pulumi.OutputState }

func (LookupTransitGatewayRouteTableAttachmentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTransitGatewayRouteTableAttachmentResult)(nil)).Elem()
}

func (o LookupTransitGatewayRouteTableAttachmentResultOutput) ToLookupTransitGatewayRouteTableAttachmentResultOutput() LookupTransitGatewayRouteTableAttachmentResultOutput {
	return o
}

func (o LookupTransitGatewayRouteTableAttachmentResultOutput) ToLookupTransitGatewayRouteTableAttachmentResultOutputWithContext(ctx context.Context) LookupTransitGatewayRouteTableAttachmentResultOutput {
	return o
}

func (o LookupTransitGatewayRouteTableAttachmentResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupTransitGatewayRouteTableAttachmentResult] {
	return pulumix.Output[LookupTransitGatewayRouteTableAttachmentResult]{
		OutputState: o.OutputState,
	}
}

// The ID of the attachment.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) AttachmentId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *string { return v.AttachmentId }).(pulumi.StringPtrOutput)
}

// The policy rule number associated with the attachment.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) AttachmentPolicyRuleNumber() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *int { return v.AttachmentPolicyRuleNumber }).(pulumi.IntPtrOutput)
}

// The type of attachment.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) AttachmentType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *string { return v.AttachmentType }).(pulumi.StringPtrOutput)
}

// The ARN of a core network for the VPC attachment.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) CoreNetworkArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *string { return v.CoreNetworkArn }).(pulumi.StringPtrOutput)
}

// The ID of a core network where you're creating a site-to-site VPN attachment.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) CoreNetworkId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *string { return v.CoreNetworkId }).(pulumi.StringPtrOutput)
}

// Creation time of the attachment.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) CreatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *string { return v.CreatedAt }).(pulumi.StringPtrOutput)
}

// The Region where the edge is located.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) EdgeLocation() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *string { return v.EdgeLocation }).(pulumi.StringPtrOutput)
}

// Owner account of the attachment.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) OwnerAccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *string { return v.OwnerAccountId }).(pulumi.StringPtrOutput)
}

// The attachment to move from one segment to another.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) ProposedSegmentChange() TransitGatewayRouteTableAttachmentProposedSegmentChangePtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *TransitGatewayRouteTableAttachmentProposedSegmentChange {
		return v.ProposedSegmentChange
	}).(TransitGatewayRouteTableAttachmentProposedSegmentChangePtrOutput)
}

// The ARN of the Resource.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) ResourceArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *string { return v.ResourceArn }).(pulumi.StringPtrOutput)
}

// The name of the segment that attachment is in.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) SegmentName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *string { return v.SegmentName }).(pulumi.StringPtrOutput)
}

// The state of the attachment.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) State() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *string { return v.State }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) Tags() TransitGatewayRouteTableAttachmentTagArrayOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) []TransitGatewayRouteTableAttachmentTag {
		return v.Tags
	}).(TransitGatewayRouteTableAttachmentTagArrayOutput)
}

// Last update time of the attachment.
func (o LookupTransitGatewayRouteTableAttachmentResultOutput) UpdatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayRouteTableAttachmentResult) *string { return v.UpdatedAt }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTransitGatewayRouteTableAttachmentResultOutput{})
}
