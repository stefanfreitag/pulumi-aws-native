// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package networkmanager

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// AWS::NetworkManager::TransitGatewayRouteTableAttachment Resource Type definition.
type TransitGatewayRouteTableAttachment struct {
	pulumi.CustomResourceState

	// The ID of the attachment.
	AttachmentId pulumi.StringOutput `pulumi:"attachmentId"`
	// The policy rule number associated with the attachment.
	AttachmentPolicyRuleNumber pulumi.IntOutput `pulumi:"attachmentPolicyRuleNumber"`
	// The type of attachment.
	AttachmentType pulumi.StringOutput `pulumi:"attachmentType"`
	// The ARN of a core network for the VPC attachment.
	CoreNetworkArn pulumi.StringOutput `pulumi:"coreNetworkArn"`
	// The ID of a core network where you're creating a site-to-site VPN attachment.
	CoreNetworkId pulumi.StringOutput `pulumi:"coreNetworkId"`
	// Creation time of the attachment.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The Region where the edge is located.
	EdgeLocation pulumi.StringOutput `pulumi:"edgeLocation"`
	// Owner account of the attachment.
	OwnerAccountId pulumi.StringOutput `pulumi:"ownerAccountId"`
	// The Id of peering between transit gateway and core network.
	PeeringId pulumi.StringOutput `pulumi:"peeringId"`
	// The attachment to move from one segment to another.
	ProposedSegmentChange TransitGatewayRouteTableAttachmentProposedSegmentChangePtrOutput `pulumi:"proposedSegmentChange"`
	// The ARN of the Resource.
	ResourceArn pulumi.StringOutput `pulumi:"resourceArn"`
	// The name of the segment that attachment is in.
	SegmentName pulumi.StringOutput `pulumi:"segmentName"`
	// The state of the attachment.
	State pulumi.StringOutput `pulumi:"state"`
	// An array of key-value pairs to apply to this resource.
	Tags TransitGatewayRouteTableAttachmentTagArrayOutput `pulumi:"tags"`
	// The Arn of transit gateway route table.
	TransitGatewayRouteTableArn pulumi.StringOutput `pulumi:"transitGatewayRouteTableArn"`
	// Last update time of the attachment.
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
}

// NewTransitGatewayRouteTableAttachment registers a new resource with the given unique name, arguments, and options.
func NewTransitGatewayRouteTableAttachment(ctx *pulumi.Context,
	name string, args *TransitGatewayRouteTableAttachmentArgs, opts ...pulumi.ResourceOption) (*TransitGatewayRouteTableAttachment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PeeringId == nil {
		return nil, errors.New("invalid value for required argument 'PeeringId'")
	}
	if args.TransitGatewayRouteTableArn == nil {
		return nil, errors.New("invalid value for required argument 'TransitGatewayRouteTableArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"peeringId",
		"transitGatewayRouteTableArn",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource TransitGatewayRouteTableAttachment
	err := ctx.RegisterResource("aws-native:networkmanager:TransitGatewayRouteTableAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTransitGatewayRouteTableAttachment gets an existing TransitGatewayRouteTableAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTransitGatewayRouteTableAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TransitGatewayRouteTableAttachmentState, opts ...pulumi.ResourceOption) (*TransitGatewayRouteTableAttachment, error) {
	var resource TransitGatewayRouteTableAttachment
	err := ctx.ReadResource("aws-native:networkmanager:TransitGatewayRouteTableAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TransitGatewayRouteTableAttachment resources.
type transitGatewayRouteTableAttachmentState struct {
}

type TransitGatewayRouteTableAttachmentState struct {
}

func (TransitGatewayRouteTableAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*transitGatewayRouteTableAttachmentState)(nil)).Elem()
}

type transitGatewayRouteTableAttachmentArgs struct {
	// The Id of peering between transit gateway and core network.
	PeeringId string `pulumi:"peeringId"`
	// The attachment to move from one segment to another.
	ProposedSegmentChange *TransitGatewayRouteTableAttachmentProposedSegmentChange `pulumi:"proposedSegmentChange"`
	// An array of key-value pairs to apply to this resource.
	Tags []TransitGatewayRouteTableAttachmentTag `pulumi:"tags"`
	// The Arn of transit gateway route table.
	TransitGatewayRouteTableArn string `pulumi:"transitGatewayRouteTableArn"`
}

// The set of arguments for constructing a TransitGatewayRouteTableAttachment resource.
type TransitGatewayRouteTableAttachmentArgs struct {
	// The Id of peering between transit gateway and core network.
	PeeringId pulumi.StringInput
	// The attachment to move from one segment to another.
	ProposedSegmentChange TransitGatewayRouteTableAttachmentProposedSegmentChangePtrInput
	// An array of key-value pairs to apply to this resource.
	Tags TransitGatewayRouteTableAttachmentTagArrayInput
	// The Arn of transit gateway route table.
	TransitGatewayRouteTableArn pulumi.StringInput
}

func (TransitGatewayRouteTableAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*transitGatewayRouteTableAttachmentArgs)(nil)).Elem()
}

type TransitGatewayRouteTableAttachmentInput interface {
	pulumi.Input

	ToTransitGatewayRouteTableAttachmentOutput() TransitGatewayRouteTableAttachmentOutput
	ToTransitGatewayRouteTableAttachmentOutputWithContext(ctx context.Context) TransitGatewayRouteTableAttachmentOutput
}

func (*TransitGatewayRouteTableAttachment) ElementType() reflect.Type {
	return reflect.TypeOf((**TransitGatewayRouteTableAttachment)(nil)).Elem()
}

func (i *TransitGatewayRouteTableAttachment) ToTransitGatewayRouteTableAttachmentOutput() TransitGatewayRouteTableAttachmentOutput {
	return i.ToTransitGatewayRouteTableAttachmentOutputWithContext(context.Background())
}

func (i *TransitGatewayRouteTableAttachment) ToTransitGatewayRouteTableAttachmentOutputWithContext(ctx context.Context) TransitGatewayRouteTableAttachmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TransitGatewayRouteTableAttachmentOutput)
}

func (i *TransitGatewayRouteTableAttachment) ToOutput(ctx context.Context) pulumix.Output[*TransitGatewayRouteTableAttachment] {
	return pulumix.Output[*TransitGatewayRouteTableAttachment]{
		OutputState: i.ToTransitGatewayRouteTableAttachmentOutputWithContext(ctx).OutputState,
	}
}

type TransitGatewayRouteTableAttachmentOutput struct{ *pulumi.OutputState }

func (TransitGatewayRouteTableAttachmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TransitGatewayRouteTableAttachment)(nil)).Elem()
}

func (o TransitGatewayRouteTableAttachmentOutput) ToTransitGatewayRouteTableAttachmentOutput() TransitGatewayRouteTableAttachmentOutput {
	return o
}

func (o TransitGatewayRouteTableAttachmentOutput) ToTransitGatewayRouteTableAttachmentOutputWithContext(ctx context.Context) TransitGatewayRouteTableAttachmentOutput {
	return o
}

func (o TransitGatewayRouteTableAttachmentOutput) ToOutput(ctx context.Context) pulumix.Output[*TransitGatewayRouteTableAttachment] {
	return pulumix.Output[*TransitGatewayRouteTableAttachment]{
		OutputState: o.OutputState,
	}
}

// The ID of the attachment.
func (o TransitGatewayRouteTableAttachmentOutput) AttachmentId() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.AttachmentId }).(pulumi.StringOutput)
}

// The policy rule number associated with the attachment.
func (o TransitGatewayRouteTableAttachmentOutput) AttachmentPolicyRuleNumber() pulumi.IntOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.IntOutput { return v.AttachmentPolicyRuleNumber }).(pulumi.IntOutput)
}

// The type of attachment.
func (o TransitGatewayRouteTableAttachmentOutput) AttachmentType() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.AttachmentType }).(pulumi.StringOutput)
}

// The ARN of a core network for the VPC attachment.
func (o TransitGatewayRouteTableAttachmentOutput) CoreNetworkArn() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.CoreNetworkArn }).(pulumi.StringOutput)
}

// The ID of a core network where you're creating a site-to-site VPN attachment.
func (o TransitGatewayRouteTableAttachmentOutput) CoreNetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.CoreNetworkId }).(pulumi.StringOutput)
}

// Creation time of the attachment.
func (o TransitGatewayRouteTableAttachmentOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The Region where the edge is located.
func (o TransitGatewayRouteTableAttachmentOutput) EdgeLocation() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.EdgeLocation }).(pulumi.StringOutput)
}

// Owner account of the attachment.
func (o TransitGatewayRouteTableAttachmentOutput) OwnerAccountId() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.OwnerAccountId }).(pulumi.StringOutput)
}

// The Id of peering between transit gateway and core network.
func (o TransitGatewayRouteTableAttachmentOutput) PeeringId() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.PeeringId }).(pulumi.StringOutput)
}

// The attachment to move from one segment to another.
func (o TransitGatewayRouteTableAttachmentOutput) ProposedSegmentChange() TransitGatewayRouteTableAttachmentProposedSegmentChangePtrOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) TransitGatewayRouteTableAttachmentProposedSegmentChangePtrOutput {
		return v.ProposedSegmentChange
	}).(TransitGatewayRouteTableAttachmentProposedSegmentChangePtrOutput)
}

// The ARN of the Resource.
func (o TransitGatewayRouteTableAttachmentOutput) ResourceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.ResourceArn }).(pulumi.StringOutput)
}

// The name of the segment that attachment is in.
func (o TransitGatewayRouteTableAttachmentOutput) SegmentName() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.SegmentName }).(pulumi.StringOutput)
}

// The state of the attachment.
func (o TransitGatewayRouteTableAttachmentOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o TransitGatewayRouteTableAttachmentOutput) Tags() TransitGatewayRouteTableAttachmentTagArrayOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) TransitGatewayRouteTableAttachmentTagArrayOutput {
		return v.Tags
	}).(TransitGatewayRouteTableAttachmentTagArrayOutput)
}

// The Arn of transit gateway route table.
func (o TransitGatewayRouteTableAttachmentOutput) TransitGatewayRouteTableArn() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.TransitGatewayRouteTableArn }).(pulumi.StringOutput)
}

// Last update time of the attachment.
func (o TransitGatewayRouteTableAttachmentOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayRouteTableAttachment) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TransitGatewayRouteTableAttachmentInput)(nil)).Elem(), &TransitGatewayRouteTableAttachment{})
	pulumi.RegisterOutputType(TransitGatewayRouteTableAttachmentOutput{})
}
