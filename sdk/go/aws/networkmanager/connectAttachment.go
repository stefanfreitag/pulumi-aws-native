// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package networkmanager

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// AWS::NetworkManager::ConnectAttachment Resource Type Definition
type ConnectAttachment struct {
	pulumi.CustomResourceState

	// The ID of the attachment.
	AttachmentId pulumi.StringOutput `pulumi:"attachmentId"`
	// The policy rule number associated with the attachment.
	AttachmentPolicyRuleNumber pulumi.IntOutput `pulumi:"attachmentPolicyRuleNumber"`
	// The type of attachment.
	AttachmentType pulumi.StringOutput `pulumi:"attachmentType"`
	// The ARN of a core network.
	CoreNetworkArn pulumi.StringOutput `pulumi:"coreNetworkArn"`
	// ID of the CoreNetwork that the attachment will be attached to.
	CoreNetworkId pulumi.StringOutput `pulumi:"coreNetworkId"`
	// Creation time of the attachment.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// Edge location of the attachment.
	EdgeLocation pulumi.StringOutput `pulumi:"edgeLocation"`
	// Protocol options for connect attachment
	Options ConnectAttachmentOptionsOutput `pulumi:"options"`
	// The ID of the attachment account owner.
	OwnerAccountId pulumi.StringOutput `pulumi:"ownerAccountId"`
	// The attachment to move from one segment to another.
	ProposedSegmentChange ConnectAttachmentProposedSegmentChangePtrOutput `pulumi:"proposedSegmentChange"`
	// The attachment resource ARN.
	ResourceArn pulumi.StringOutput `pulumi:"resourceArn"`
	// The name of the segment attachment.
	SegmentName pulumi.StringOutput `pulumi:"segmentName"`
	// State of the attachment.
	State pulumi.StringOutput `pulumi:"state"`
	// Tags for the attachment.
	Tags aws.TagArrayOutput `pulumi:"tags"`
	// Id of transport attachment
	TransportAttachmentId pulumi.StringOutput `pulumi:"transportAttachmentId"`
	// Last update time of the attachment.
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
}

// NewConnectAttachment registers a new resource with the given unique name, arguments, and options.
func NewConnectAttachment(ctx *pulumi.Context,
	name string, args *ConnectAttachmentArgs, opts ...pulumi.ResourceOption) (*ConnectAttachment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CoreNetworkId == nil {
		return nil, errors.New("invalid value for required argument 'CoreNetworkId'")
	}
	if args.EdgeLocation == nil {
		return nil, errors.New("invalid value for required argument 'EdgeLocation'")
	}
	if args.Options == nil {
		return nil, errors.New("invalid value for required argument 'Options'")
	}
	if args.TransportAttachmentId == nil {
		return nil, errors.New("invalid value for required argument 'TransportAttachmentId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"coreNetworkId",
		"edgeLocation",
		"options",
		"transportAttachmentId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ConnectAttachment
	err := ctx.RegisterResource("aws-native:networkmanager:ConnectAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConnectAttachment gets an existing ConnectAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConnectAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConnectAttachmentState, opts ...pulumi.ResourceOption) (*ConnectAttachment, error) {
	var resource ConnectAttachment
	err := ctx.ReadResource("aws-native:networkmanager:ConnectAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ConnectAttachment resources.
type connectAttachmentState struct {
}

type ConnectAttachmentState struct {
}

func (ConnectAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*connectAttachmentState)(nil)).Elem()
}

type connectAttachmentArgs struct {
	// ID of the CoreNetwork that the attachment will be attached to.
	CoreNetworkId string `pulumi:"coreNetworkId"`
	// Edge location of the attachment.
	EdgeLocation string `pulumi:"edgeLocation"`
	// Protocol options for connect attachment
	Options ConnectAttachmentOptions `pulumi:"options"`
	// The attachment to move from one segment to another.
	ProposedSegmentChange *ConnectAttachmentProposedSegmentChange `pulumi:"proposedSegmentChange"`
	// Tags for the attachment.
	Tags []aws.Tag `pulumi:"tags"`
	// Id of transport attachment
	TransportAttachmentId string `pulumi:"transportAttachmentId"`
}

// The set of arguments for constructing a ConnectAttachment resource.
type ConnectAttachmentArgs struct {
	// ID of the CoreNetwork that the attachment will be attached to.
	CoreNetworkId pulumi.StringInput
	// Edge location of the attachment.
	EdgeLocation pulumi.StringInput
	// Protocol options for connect attachment
	Options ConnectAttachmentOptionsInput
	// The attachment to move from one segment to another.
	ProposedSegmentChange ConnectAttachmentProposedSegmentChangePtrInput
	// Tags for the attachment.
	Tags aws.TagArrayInput
	// Id of transport attachment
	TransportAttachmentId pulumi.StringInput
}

func (ConnectAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*connectAttachmentArgs)(nil)).Elem()
}

type ConnectAttachmentInput interface {
	pulumi.Input

	ToConnectAttachmentOutput() ConnectAttachmentOutput
	ToConnectAttachmentOutputWithContext(ctx context.Context) ConnectAttachmentOutput
}

func (*ConnectAttachment) ElementType() reflect.Type {
	return reflect.TypeOf((**ConnectAttachment)(nil)).Elem()
}

func (i *ConnectAttachment) ToConnectAttachmentOutput() ConnectAttachmentOutput {
	return i.ToConnectAttachmentOutputWithContext(context.Background())
}

func (i *ConnectAttachment) ToConnectAttachmentOutputWithContext(ctx context.Context) ConnectAttachmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConnectAttachmentOutput)
}

type ConnectAttachmentOutput struct{ *pulumi.OutputState }

func (ConnectAttachmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ConnectAttachment)(nil)).Elem()
}

func (o ConnectAttachmentOutput) ToConnectAttachmentOutput() ConnectAttachmentOutput {
	return o
}

func (o ConnectAttachmentOutput) ToConnectAttachmentOutputWithContext(ctx context.Context) ConnectAttachmentOutput {
	return o
}

// The ID of the attachment.
func (o ConnectAttachmentOutput) AttachmentId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.StringOutput { return v.AttachmentId }).(pulumi.StringOutput)
}

// The policy rule number associated with the attachment.
func (o ConnectAttachmentOutput) AttachmentPolicyRuleNumber() pulumi.IntOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.IntOutput { return v.AttachmentPolicyRuleNumber }).(pulumi.IntOutput)
}

// The type of attachment.
func (o ConnectAttachmentOutput) AttachmentType() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.StringOutput { return v.AttachmentType }).(pulumi.StringOutput)
}

// The ARN of a core network.
func (o ConnectAttachmentOutput) CoreNetworkArn() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.StringOutput { return v.CoreNetworkArn }).(pulumi.StringOutput)
}

// ID of the CoreNetwork that the attachment will be attached to.
func (o ConnectAttachmentOutput) CoreNetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.StringOutput { return v.CoreNetworkId }).(pulumi.StringOutput)
}

// Creation time of the attachment.
func (o ConnectAttachmentOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// Edge location of the attachment.
func (o ConnectAttachmentOutput) EdgeLocation() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.StringOutput { return v.EdgeLocation }).(pulumi.StringOutput)
}

// Protocol options for connect attachment
func (o ConnectAttachmentOutput) Options() ConnectAttachmentOptionsOutput {
	return o.ApplyT(func(v *ConnectAttachment) ConnectAttachmentOptionsOutput { return v.Options }).(ConnectAttachmentOptionsOutput)
}

// The ID of the attachment account owner.
func (o ConnectAttachmentOutput) OwnerAccountId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.StringOutput { return v.OwnerAccountId }).(pulumi.StringOutput)
}

// The attachment to move from one segment to another.
func (o ConnectAttachmentOutput) ProposedSegmentChange() ConnectAttachmentProposedSegmentChangePtrOutput {
	return o.ApplyT(func(v *ConnectAttachment) ConnectAttachmentProposedSegmentChangePtrOutput {
		return v.ProposedSegmentChange
	}).(ConnectAttachmentProposedSegmentChangePtrOutput)
}

// The attachment resource ARN.
func (o ConnectAttachmentOutput) ResourceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.StringOutput { return v.ResourceArn }).(pulumi.StringOutput)
}

// The name of the segment attachment.
func (o ConnectAttachmentOutput) SegmentName() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.StringOutput { return v.SegmentName }).(pulumi.StringOutput)
}

// State of the attachment.
func (o ConnectAttachmentOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// Tags for the attachment.
func (o ConnectAttachmentOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *ConnectAttachment) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

// Id of transport attachment
func (o ConnectAttachmentOutput) TransportAttachmentId() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.StringOutput { return v.TransportAttachmentId }).(pulumi.StringOutput)
}

// Last update time of the attachment.
func (o ConnectAttachmentOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *ConnectAttachment) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConnectAttachmentInput)(nil)).Elem(), &ConnectAttachment{})
	pulumi.RegisterOutputType(ConnectAttachmentOutput{})
}
