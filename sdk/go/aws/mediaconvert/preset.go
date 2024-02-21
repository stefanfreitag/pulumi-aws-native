// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package mediaconvert

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::MediaConvert::Preset
//
// Deprecated: Preset is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Preset struct {
	pulumi.CustomResourceState

	Arn         pulumi.StringOutput    `pulumi:"arn"`
	Category    pulumi.StringPtrOutput `pulumi:"category"`
	Description pulumi.StringPtrOutput `pulumi:"description"`
	Name        pulumi.StringPtrOutput `pulumi:"name"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
	SettingsJson pulumi.AnyOutput `pulumi:"settingsJson"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
	Tags pulumi.AnyOutput `pulumi:"tags"`
}

// NewPreset registers a new resource with the given unique name, arguments, and options.
func NewPreset(ctx *pulumi.Context,
	name string, args *PresetArgs, opts ...pulumi.ResourceOption) (*Preset, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SettingsJson == nil {
		return nil, errors.New("invalid value for required argument 'SettingsJson'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Preset
	err := ctx.RegisterResource("aws-native:mediaconvert:Preset", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPreset gets an existing Preset resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPreset(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PresetState, opts ...pulumi.ResourceOption) (*Preset, error) {
	var resource Preset
	err := ctx.ReadResource("aws-native:mediaconvert:Preset", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Preset resources.
type presetState struct {
}

type PresetState struct {
}

func (PresetState) ElementType() reflect.Type {
	return reflect.TypeOf((*presetState)(nil)).Elem()
}

type presetArgs struct {
	Category    *string `pulumi:"category"`
	Description *string `pulumi:"description"`
	Name        *string `pulumi:"name"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
	SettingsJson interface{} `pulumi:"settingsJson"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
	Tags interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a Preset resource.
type PresetArgs struct {
	Category    pulumi.StringPtrInput
	Description pulumi.StringPtrInput
	Name        pulumi.StringPtrInput
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
	SettingsJson pulumi.Input
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
	Tags pulumi.Input
}

func (PresetArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*presetArgs)(nil)).Elem()
}

type PresetInput interface {
	pulumi.Input

	ToPresetOutput() PresetOutput
	ToPresetOutputWithContext(ctx context.Context) PresetOutput
}

func (*Preset) ElementType() reflect.Type {
	return reflect.TypeOf((**Preset)(nil)).Elem()
}

func (i *Preset) ToPresetOutput() PresetOutput {
	return i.ToPresetOutputWithContext(context.Background())
}

func (i *Preset) ToPresetOutputWithContext(ctx context.Context) PresetOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PresetOutput)
}

type PresetOutput struct{ *pulumi.OutputState }

func (PresetOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Preset)(nil)).Elem()
}

func (o PresetOutput) ToPresetOutput() PresetOutput {
	return o
}

func (o PresetOutput) ToPresetOutputWithContext(ctx context.Context) PresetOutput {
	return o
}

func (o PresetOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Preset) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o PresetOutput) Category() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Preset) pulumi.StringPtrOutput { return v.Category }).(pulumi.StringPtrOutput)
}

func (o PresetOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Preset) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o PresetOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Preset) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
func (o PresetOutput) SettingsJson() pulumi.AnyOutput {
	return o.ApplyT(func(v *Preset) pulumi.AnyOutput { return v.SettingsJson }).(pulumi.AnyOutput)
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::MediaConvert::Preset` for more information about the expected schema for this property.
func (o PresetOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v *Preset) pulumi.AnyOutput { return v.Tags }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PresetInput)(nil)).Elem(), &Preset{})
	pulumi.RegisterOutputType(PresetOutput{})
}
