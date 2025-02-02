// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SageMaker::Space
type Space struct {
	pulumi.CustomResourceState

	// The ID of the associated Domain.
	DomainId          pulumi.StringOutput             `pulumi:"domainId"`
	OwnershipSettings SpaceOwnershipSettingsPtrOutput `pulumi:"ownershipSettings"`
	// The space Amazon Resource Name (ARN).
	SpaceArn         pulumi.StringOutput    `pulumi:"spaceArn"`
	SpaceDisplayName pulumi.StringPtrOutput `pulumi:"spaceDisplayName"`
	// A name for the Space.
	SpaceName pulumi.StringOutput `pulumi:"spaceName"`
	// A collection of settings.
	SpaceSettings        SpaceSettingsPtrOutput        `pulumi:"spaceSettings"`
	SpaceSharingSettings SpaceSharingSettingsPtrOutput `pulumi:"spaceSharingSettings"`
	// A list of tags to apply to the space.
	Tags aws.TagArrayOutput  `pulumi:"tags"`
	Url  pulumi.StringOutput `pulumi:"url"`
}

// NewSpace registers a new resource with the given unique name, arguments, and options.
func NewSpace(ctx *pulumi.Context,
	name string, args *SpaceArgs, opts ...pulumi.ResourceOption) (*Space, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DomainId == nil {
		return nil, errors.New("invalid value for required argument 'DomainId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"domainId",
		"ownershipSettings",
		"spaceName",
		"spaceSharingSettings",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Space
	err := ctx.RegisterResource("aws-native:sagemaker:Space", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSpace gets an existing Space resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSpace(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SpaceState, opts ...pulumi.ResourceOption) (*Space, error) {
	var resource Space
	err := ctx.ReadResource("aws-native:sagemaker:Space", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Space resources.
type spaceState struct {
}

type SpaceState struct {
}

func (SpaceState) ElementType() reflect.Type {
	return reflect.TypeOf((*spaceState)(nil)).Elem()
}

type spaceArgs struct {
	// The ID of the associated Domain.
	DomainId          string                  `pulumi:"domainId"`
	OwnershipSettings *SpaceOwnershipSettings `pulumi:"ownershipSettings"`
	SpaceDisplayName  *string                 `pulumi:"spaceDisplayName"`
	// A name for the Space.
	SpaceName *string `pulumi:"spaceName"`
	// A collection of settings.
	SpaceSettings        *SpaceSettings        `pulumi:"spaceSettings"`
	SpaceSharingSettings *SpaceSharingSettings `pulumi:"spaceSharingSettings"`
	// A list of tags to apply to the space.
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a Space resource.
type SpaceArgs struct {
	// The ID of the associated Domain.
	DomainId          pulumi.StringInput
	OwnershipSettings SpaceOwnershipSettingsPtrInput
	SpaceDisplayName  pulumi.StringPtrInput
	// A name for the Space.
	SpaceName pulumi.StringPtrInput
	// A collection of settings.
	SpaceSettings        SpaceSettingsPtrInput
	SpaceSharingSettings SpaceSharingSettingsPtrInput
	// A list of tags to apply to the space.
	Tags aws.TagArrayInput
}

func (SpaceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*spaceArgs)(nil)).Elem()
}

type SpaceInput interface {
	pulumi.Input

	ToSpaceOutput() SpaceOutput
	ToSpaceOutputWithContext(ctx context.Context) SpaceOutput
}

func (*Space) ElementType() reflect.Type {
	return reflect.TypeOf((**Space)(nil)).Elem()
}

func (i *Space) ToSpaceOutput() SpaceOutput {
	return i.ToSpaceOutputWithContext(context.Background())
}

func (i *Space) ToSpaceOutputWithContext(ctx context.Context) SpaceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SpaceOutput)
}

type SpaceOutput struct{ *pulumi.OutputState }

func (SpaceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Space)(nil)).Elem()
}

func (o SpaceOutput) ToSpaceOutput() SpaceOutput {
	return o
}

func (o SpaceOutput) ToSpaceOutputWithContext(ctx context.Context) SpaceOutput {
	return o
}

// The ID of the associated Domain.
func (o SpaceOutput) DomainId() pulumi.StringOutput {
	return o.ApplyT(func(v *Space) pulumi.StringOutput { return v.DomainId }).(pulumi.StringOutput)
}

func (o SpaceOutput) OwnershipSettings() SpaceOwnershipSettingsPtrOutput {
	return o.ApplyT(func(v *Space) SpaceOwnershipSettingsPtrOutput { return v.OwnershipSettings }).(SpaceOwnershipSettingsPtrOutput)
}

// The space Amazon Resource Name (ARN).
func (o SpaceOutput) SpaceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Space) pulumi.StringOutput { return v.SpaceArn }).(pulumi.StringOutput)
}

func (o SpaceOutput) SpaceDisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Space) pulumi.StringPtrOutput { return v.SpaceDisplayName }).(pulumi.StringPtrOutput)
}

// A name for the Space.
func (o SpaceOutput) SpaceName() pulumi.StringOutput {
	return o.ApplyT(func(v *Space) pulumi.StringOutput { return v.SpaceName }).(pulumi.StringOutput)
}

// A collection of settings.
func (o SpaceOutput) SpaceSettings() SpaceSettingsPtrOutput {
	return o.ApplyT(func(v *Space) SpaceSettingsPtrOutput { return v.SpaceSettings }).(SpaceSettingsPtrOutput)
}

func (o SpaceOutput) SpaceSharingSettings() SpaceSharingSettingsPtrOutput {
	return o.ApplyT(func(v *Space) SpaceSharingSettingsPtrOutput { return v.SpaceSharingSettings }).(SpaceSharingSettingsPtrOutput)
}

// A list of tags to apply to the space.
func (o SpaceOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Space) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func (o SpaceOutput) Url() pulumi.StringOutput {
	return o.ApplyT(func(v *Space) pulumi.StringOutput { return v.Url }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SpaceInput)(nil)).Elem(), &Space{})
	pulumi.RegisterOutputType(SpaceOutput{})
}
