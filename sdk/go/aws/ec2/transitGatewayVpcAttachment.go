// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::EC2::TransitGatewayVpcAttachment
type TransitGatewayVpcAttachment struct {
	pulumi.CustomResourceState

	AddSubnetIds pulumi.StringArrayOutput `pulumi:"addSubnetIds"`
	// The options for the transit gateway vpc attachment.
	Options          OptionsPropertiesPtrOutput `pulumi:"options"`
	RemoveSubnetIds  pulumi.StringArrayOutput   `pulumi:"removeSubnetIds"`
	SubnetIds        pulumi.StringArrayOutput   `pulumi:"subnetIds"`
	Tags             aws.TagArrayOutput         `pulumi:"tags"`
	TransitGatewayId pulumi.StringOutput        `pulumi:"transitGatewayId"`
	VpcId            pulumi.StringOutput        `pulumi:"vpcId"`
}

// NewTransitGatewayVpcAttachment registers a new resource with the given unique name, arguments, and options.
func NewTransitGatewayVpcAttachment(ctx *pulumi.Context,
	name string, args *TransitGatewayVpcAttachmentArgs, opts ...pulumi.ResourceOption) (*TransitGatewayVpcAttachment, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'SubnetIds'")
	}
	if args.TransitGatewayId == nil {
		return nil, errors.New("invalid value for required argument 'TransitGatewayId'")
	}
	if args.VpcId == nil {
		return nil, errors.New("invalid value for required argument 'VpcId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"subnetIds[*]",
		"transitGatewayId",
		"vpcId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource TransitGatewayVpcAttachment
	err := ctx.RegisterResource("aws-native:ec2:TransitGatewayVpcAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTransitGatewayVpcAttachment gets an existing TransitGatewayVpcAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTransitGatewayVpcAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TransitGatewayVpcAttachmentState, opts ...pulumi.ResourceOption) (*TransitGatewayVpcAttachment, error) {
	var resource TransitGatewayVpcAttachment
	err := ctx.ReadResource("aws-native:ec2:TransitGatewayVpcAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TransitGatewayVpcAttachment resources.
type transitGatewayVpcAttachmentState struct {
}

type TransitGatewayVpcAttachmentState struct {
}

func (TransitGatewayVpcAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*transitGatewayVpcAttachmentState)(nil)).Elem()
}

type transitGatewayVpcAttachmentArgs struct {
	AddSubnetIds []string `pulumi:"addSubnetIds"`
	// The options for the transit gateway vpc attachment.
	Options          *OptionsProperties `pulumi:"options"`
	RemoveSubnetIds  []string           `pulumi:"removeSubnetIds"`
	SubnetIds        []string           `pulumi:"subnetIds"`
	Tags             []aws.Tag          `pulumi:"tags"`
	TransitGatewayId string             `pulumi:"transitGatewayId"`
	VpcId            string             `pulumi:"vpcId"`
}

// The set of arguments for constructing a TransitGatewayVpcAttachment resource.
type TransitGatewayVpcAttachmentArgs struct {
	AddSubnetIds pulumi.StringArrayInput
	// The options for the transit gateway vpc attachment.
	Options          OptionsPropertiesPtrInput
	RemoveSubnetIds  pulumi.StringArrayInput
	SubnetIds        pulumi.StringArrayInput
	Tags             aws.TagArrayInput
	TransitGatewayId pulumi.StringInput
	VpcId            pulumi.StringInput
}

func (TransitGatewayVpcAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*transitGatewayVpcAttachmentArgs)(nil)).Elem()
}

type TransitGatewayVpcAttachmentInput interface {
	pulumi.Input

	ToTransitGatewayVpcAttachmentOutput() TransitGatewayVpcAttachmentOutput
	ToTransitGatewayVpcAttachmentOutputWithContext(ctx context.Context) TransitGatewayVpcAttachmentOutput
}

func (*TransitGatewayVpcAttachment) ElementType() reflect.Type {
	return reflect.TypeOf((**TransitGatewayVpcAttachment)(nil)).Elem()
}

func (i *TransitGatewayVpcAttachment) ToTransitGatewayVpcAttachmentOutput() TransitGatewayVpcAttachmentOutput {
	return i.ToTransitGatewayVpcAttachmentOutputWithContext(context.Background())
}

func (i *TransitGatewayVpcAttachment) ToTransitGatewayVpcAttachmentOutputWithContext(ctx context.Context) TransitGatewayVpcAttachmentOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TransitGatewayVpcAttachmentOutput)
}

type TransitGatewayVpcAttachmentOutput struct{ *pulumi.OutputState }

func (TransitGatewayVpcAttachmentOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TransitGatewayVpcAttachment)(nil)).Elem()
}

func (o TransitGatewayVpcAttachmentOutput) ToTransitGatewayVpcAttachmentOutput() TransitGatewayVpcAttachmentOutput {
	return o
}

func (o TransitGatewayVpcAttachmentOutput) ToTransitGatewayVpcAttachmentOutputWithContext(ctx context.Context) TransitGatewayVpcAttachmentOutput {
	return o
}

func (o TransitGatewayVpcAttachmentOutput) AddSubnetIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *TransitGatewayVpcAttachment) pulumi.StringArrayOutput { return v.AddSubnetIds }).(pulumi.StringArrayOutput)
}

// The options for the transit gateway vpc attachment.
func (o TransitGatewayVpcAttachmentOutput) Options() OptionsPropertiesPtrOutput {
	return o.ApplyT(func(v *TransitGatewayVpcAttachment) OptionsPropertiesPtrOutput { return v.Options }).(OptionsPropertiesPtrOutput)
}

func (o TransitGatewayVpcAttachmentOutput) RemoveSubnetIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *TransitGatewayVpcAttachment) pulumi.StringArrayOutput { return v.RemoveSubnetIds }).(pulumi.StringArrayOutput)
}

func (o TransitGatewayVpcAttachmentOutput) SubnetIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *TransitGatewayVpcAttachment) pulumi.StringArrayOutput { return v.SubnetIds }).(pulumi.StringArrayOutput)
}

func (o TransitGatewayVpcAttachmentOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *TransitGatewayVpcAttachment) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func (o TransitGatewayVpcAttachmentOutput) TransitGatewayId() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayVpcAttachment) pulumi.StringOutput { return v.TransitGatewayId }).(pulumi.StringOutput)
}

func (o TransitGatewayVpcAttachmentOutput) VpcId() pulumi.StringOutput {
	return o.ApplyT(func(v *TransitGatewayVpcAttachment) pulumi.StringOutput { return v.VpcId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TransitGatewayVpcAttachmentInput)(nil)).Elem(), &TransitGatewayVpcAttachment{})
	pulumi.RegisterOutputType(TransitGatewayVpcAttachmentOutput{})
}
