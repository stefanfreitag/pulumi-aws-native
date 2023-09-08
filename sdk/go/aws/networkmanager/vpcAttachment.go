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

// AWS::NetworkManager::VpcAttachment Resoruce Type
type VpcAttachment struct {
	pulumi.CustomResourceState

	// Id of the attachment.
	AttachmentId pulumi.StringOutput `pulumi:"attachmentId"`
	// The policy rule number associated with the attachment.
	AttachmentPolicyRuleNumber pulumi.IntOutput `pulumi:"attachmentPolicyRuleNumber"`
	// Attachment type.
	AttachmentType pulumi.StringOutput `pulumi:"attachmentType"`
	// The ARN of a core network for the VPC attachment.
	CoreNetworkArn pulumi.StringOutput `pulumi:"coreNetworkArn"`
	// The ID of a core network for the VPC attachment.
	CoreNetworkId pulumi.StringOutput `pulumi:"coreNetworkId"`
	// Creation time of the attachment.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The Region where the edge is located.
	EdgeLocation pulumi.StringOutput `pulumi:"edgeLocation"`
	// Vpc options of the attachment.
	Options VpcAttachmentVpcOptionsPtrOutput `pulumi:"options"`
	// Owner account of the attachment.
	OwnerAccountId pulumi.StringOutput `pulumi:"ownerAccountId"`
	// The attachment to move from one segment to another.
	ProposedSegmentChange VpcAttachmentProposedSegmentChangePtrOutput `pulumi:"proposedSegmentChange"`
	// The ARN of the Resource.
	ResourceArn pulumi.StringOutput `pulumi:"resourceArn"`
	// The name of the segment attachment..
	SegmentName pulumi.StringOutput `pulumi:"segmentName"`
	// State of the attachment.
	State pulumi.StringOutput `pulumi:"state"`
	// Subnet Arn list
	SubnetArns pulumi.StringArrayOutput `pulumi:"subnetArns"`
	// Tags for the attachment.
	Tags VpcAttachmentTagArrayOutput `pulumi:"tags"`
	// Last update time of the attachment.
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
	// The ARN of the VPC.
	VpcArn pulumi.StringOutput `pulumi:"vpcArn"`
}

// NewVpcAttachment registers a new resource with the given unique name, arguments, and options.
func NewVpcAttachment(ctx *pulumi.Context,
	name string, args *VpcAttachmentArgs, opts ...pulumi.ResourceOption) (*VpcAttachment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CoreNetworkId == nil {
		return nil, errors.New("invalid value for required argument 'CoreNetworkId'")
	}
	if args.SubnetArns == nil {
		return nil, errors.New("invalid value for required argument 'SubnetArns'")
	}
	if args.VpcArn == nil {
		return nil, errors.New("invalid value for required argument 'VpcArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"coreNetworkId",
		"vpcArn",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource VpcAttachment
	err := ctx.RegisterResource("aws-native:networkmanager:VpcAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVpcAttachment gets an existing VpcAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpcAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VpcAttachmentState, opts ...pulumi.ResourceOption) (*VpcAttachment, error) {
	var resource VpcAttachment
	err := ctx.ReadResource("aws-native:networkmanager:VpcAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VpcAttachment resources.
type vpcAttachmentState struct {
}

type VpcAttachmentState struct {
}

func (VpcAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcAttachmentState)(nil)).Elem()
}

type vpcAttachmentArgs struct {
	// The ID of a core network for the VPC attachment.
	CoreNetworkId string `pulumi:"coreNetworkId"`
	// Vpc options of the attachment.
	Options *VpcAttachmentVpcOptions `pulumi:"options"`
	// The attachment to move from one segment to another.
	ProposedSegmentChange *VpcAttachmentProposedSegmentChange `pulumi:"proposedSegmentChange"`
	// Subnet Arn list
	SubnetArns []string `pulumi:"subnetArns"`
	// Tags for the attachment.
	Tags []VpcAttachmentTag `pulumi:"tags"`
	// The ARN of the VPC.
	VpcArn string `pulumi:"vpcArn"`
}

// The set of arguments for constructing a VpcAttachment resource.
type VpcAttachmentArgs struct {
	// The ID of a core network for the VPC attachment.
	CoreNetworkId pulumi.StringInput
	// Vpc options of the attachment.
	Options VpcAttachmentVpcOptionsPtrInput
	// The attachment to move from one segment to another.
	ProposedSegmentChange VpcAttachmentProposedSegmentChangePtrInput
	// Subnet Arn list
	SubnetArns pulumi.StringArrayInput
	// Tags for the attachment.
	Tags VpcAttachmentTagArrayInput
	// The ARN of the VPC.
	VpcArn pulumi.StringInput
}

func (VpcAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcAttachmentArgs)(nil)).Elem()
}

type VpcAttachmentInput interface {
	pulumi.Input

	ToVpcAttachmentOutput() VpcAttachmentOutput
	ToVpcAttachmentOutputWithContext(ctx context.Context) VpcAttachmentOutput
}

func (*VpcAttachment) ElementType() reflect.Type {
	return reflect.TypeOf((**VpcAttachment)(nil)).Elem()
}

func (i *VpcAttachment) ToVpcAttachmentOutput() VpcAttachmentOutput {
	return i.ToVpcAttachmentOutputWithContext(context.Background())
}

func (i *VpcAttachment) ToVpcAttachmentOutputWithContext(ctx context.Context) VpcAttachmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VpcAttachmentOutput)
}

func (i *VpcAttachment) ToOutput(ctx context.Context) pulumix.Output[*VpcAttachment] {
	return pulumix.Output[*VpcAttachment]{
		OutputState: i.ToVpcAttachmentOutputWithContext(ctx).OutputState,
	}
}

type VpcAttachmentOutput struct{ *pulumi.OutputState }

func (VpcAttachmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VpcAttachment)(nil)).Elem()
}

func (o VpcAttachmentOutput) ToVpcAttachmentOutput() VpcAttachmentOutput {
	return o
}

func (o VpcAttachmentOutput) ToVpcAttachmentOutputWithContext(ctx context.Context) VpcAttachmentOutput {
	return o
}

func (o VpcAttachmentOutput) ToOutput(ctx context.Context) pulumix.Output[*VpcAttachment] {
	return pulumix.Output[*VpcAttachment]{
		OutputState: o.OutputState,
	}
}

// Id of the attachment.
func (o VpcAttachmentOutput) AttachmentId() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringOutput { return v.AttachmentId }).(pulumi.StringOutput)
}

// The policy rule number associated with the attachment.
func (o VpcAttachmentOutput) AttachmentPolicyRuleNumber() pulumi.IntOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.IntOutput { return v.AttachmentPolicyRuleNumber }).(pulumi.IntOutput)
}

// Attachment type.
func (o VpcAttachmentOutput) AttachmentType() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringOutput { return v.AttachmentType }).(pulumi.StringOutput)
}

// The ARN of a core network for the VPC attachment.
func (o VpcAttachmentOutput) CoreNetworkArn() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringOutput { return v.CoreNetworkArn }).(pulumi.StringOutput)
}

// The ID of a core network for the VPC attachment.
func (o VpcAttachmentOutput) CoreNetworkId() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringOutput { return v.CoreNetworkId }).(pulumi.StringOutput)
}

// Creation time of the attachment.
func (o VpcAttachmentOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringOutput { return v.CreatedAt }).(pulumi.StringOutput)
}

// The Region where the edge is located.
func (o VpcAttachmentOutput) EdgeLocation() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringOutput { return v.EdgeLocation }).(pulumi.StringOutput)
}

// Vpc options of the attachment.
func (o VpcAttachmentOutput) Options() VpcAttachmentVpcOptionsPtrOutput {
	return o.ApplyT(func(v *VpcAttachment) VpcAttachmentVpcOptionsPtrOutput { return v.Options }).(VpcAttachmentVpcOptionsPtrOutput)
}

// Owner account of the attachment.
func (o VpcAttachmentOutput) OwnerAccountId() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringOutput { return v.OwnerAccountId }).(pulumi.StringOutput)
}

// The attachment to move from one segment to another.
func (o VpcAttachmentOutput) ProposedSegmentChange() VpcAttachmentProposedSegmentChangePtrOutput {
	return o.ApplyT(func(v *VpcAttachment) VpcAttachmentProposedSegmentChangePtrOutput { return v.ProposedSegmentChange }).(VpcAttachmentProposedSegmentChangePtrOutput)
}

// The ARN of the Resource.
func (o VpcAttachmentOutput) ResourceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringOutput { return v.ResourceArn }).(pulumi.StringOutput)
}

// The name of the segment attachment..
func (o VpcAttachmentOutput) SegmentName() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringOutput { return v.SegmentName }).(pulumi.StringOutput)
}

// State of the attachment.
func (o VpcAttachmentOutput) State() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringOutput { return v.State }).(pulumi.StringOutput)
}

// Subnet Arn list
func (o VpcAttachmentOutput) SubnetArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringArrayOutput { return v.SubnetArns }).(pulumi.StringArrayOutput)
}

// Tags for the attachment.
func (o VpcAttachmentOutput) Tags() VpcAttachmentTagArrayOutput {
	return o.ApplyT(func(v *VpcAttachment) VpcAttachmentTagArrayOutput { return v.Tags }).(VpcAttachmentTagArrayOutput)
}

// Last update time of the attachment.
func (o VpcAttachmentOutput) UpdatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringOutput { return v.UpdatedAt }).(pulumi.StringOutput)
}

// The ARN of the VPC.
func (o VpcAttachmentOutput) VpcArn() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcAttachment) pulumi.StringOutput { return v.VpcArn }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VpcAttachmentInput)(nil)).Elem(), &VpcAttachment{})
	pulumi.RegisterOutputType(VpcAttachmentOutput{})
}
