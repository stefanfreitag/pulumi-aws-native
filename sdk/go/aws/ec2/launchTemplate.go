// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::EC2::LaunchTemplate
type LaunchTemplate struct {
	pulumi.CustomResourceState

	// The default version of the launch template
	DefaultVersionNumber pulumi.StringOutput `pulumi:"defaultVersionNumber"`
	// The latest version of the launch template
	LatestVersionNumber pulumi.StringOutput      `pulumi:"latestVersionNumber"`
	LaunchTemplateData  LaunchTemplateDataOutput `pulumi:"launchTemplateData"`
	// LaunchTemplate ID generated by service
	LaunchTemplateId pulumi.StringOutput `pulumi:"launchTemplateId"`
	// A name for the launch template.
	LaunchTemplateName pulumi.StringPtrOutput `pulumi:"launchTemplateName"`
	// The tags to apply to the launch template on creation.
	TagSpecifications LaunchTemplateTagSpecificationArrayOutput `pulumi:"tagSpecifications"`
	// A description for the first version of the launch template.
	VersionDescription pulumi.StringPtrOutput `pulumi:"versionDescription"`
}

// NewLaunchTemplate registers a new resource with the given unique name, arguments, and options.
func NewLaunchTemplate(ctx *pulumi.Context,
	name string, args *LaunchTemplateArgs, opts ...pulumi.ResourceOption) (*LaunchTemplate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.LaunchTemplateData == nil {
		return nil, errors.New("invalid value for required argument 'LaunchTemplateData'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"launchTemplateName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource LaunchTemplate
	err := ctx.RegisterResource("aws-native:ec2:LaunchTemplate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLaunchTemplate gets an existing LaunchTemplate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLaunchTemplate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LaunchTemplateState, opts ...pulumi.ResourceOption) (*LaunchTemplate, error) {
	var resource LaunchTemplate
	err := ctx.ReadResource("aws-native:ec2:LaunchTemplate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LaunchTemplate resources.
type launchTemplateState struct {
}

type LaunchTemplateState struct {
}

func (LaunchTemplateState) ElementType() reflect.Type {
	return reflect.TypeOf((*launchTemplateState)(nil)).Elem()
}

type launchTemplateArgs struct {
	LaunchTemplateData LaunchTemplateData `pulumi:"launchTemplateData"`
	// A name for the launch template.
	LaunchTemplateName *string `pulumi:"launchTemplateName"`
	// The tags to apply to the launch template on creation.
	TagSpecifications []LaunchTemplateTagSpecification `pulumi:"tagSpecifications"`
	// A description for the first version of the launch template.
	VersionDescription *string `pulumi:"versionDescription"`
}

// The set of arguments for constructing a LaunchTemplate resource.
type LaunchTemplateArgs struct {
	LaunchTemplateData LaunchTemplateDataInput
	// A name for the launch template.
	LaunchTemplateName pulumi.StringPtrInput
	// The tags to apply to the launch template on creation.
	TagSpecifications LaunchTemplateTagSpecificationArrayInput
	// A description for the first version of the launch template.
	VersionDescription pulumi.StringPtrInput
}

func (LaunchTemplateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*launchTemplateArgs)(nil)).Elem()
}

type LaunchTemplateInput interface {
	pulumi.Input

	ToLaunchTemplateOutput() LaunchTemplateOutput
	ToLaunchTemplateOutputWithContext(ctx context.Context) LaunchTemplateOutput
}

func (*LaunchTemplate) ElementType() reflect.Type {
	return reflect.TypeOf((**LaunchTemplate)(nil)).Elem()
}

func (i *LaunchTemplate) ToLaunchTemplateOutput() LaunchTemplateOutput {
	return i.ToLaunchTemplateOutputWithContext(context.Background())
}

func (i *LaunchTemplate) ToLaunchTemplateOutputWithContext(ctx context.Context) LaunchTemplateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LaunchTemplateOutput)
}

func (i *LaunchTemplate) ToOutput(ctx context.Context) pulumix.Output[*LaunchTemplate] {
	return pulumix.Output[*LaunchTemplate]{
		OutputState: i.ToLaunchTemplateOutputWithContext(ctx).OutputState,
	}
}

type LaunchTemplateOutput struct{ *pulumi.OutputState }

func (LaunchTemplateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**LaunchTemplate)(nil)).Elem()
}

func (o LaunchTemplateOutput) ToLaunchTemplateOutput() LaunchTemplateOutput {
	return o
}

func (o LaunchTemplateOutput) ToLaunchTemplateOutputWithContext(ctx context.Context) LaunchTemplateOutput {
	return o
}

func (o LaunchTemplateOutput) ToOutput(ctx context.Context) pulumix.Output[*LaunchTemplate] {
	return pulumix.Output[*LaunchTemplate]{
		OutputState: o.OutputState,
	}
}

// The default version of the launch template
func (o LaunchTemplateOutput) DefaultVersionNumber() pulumi.StringOutput {
	return o.ApplyT(func(v *LaunchTemplate) pulumi.StringOutput { return v.DefaultVersionNumber }).(pulumi.StringOutput)
}

// The latest version of the launch template
func (o LaunchTemplateOutput) LatestVersionNumber() pulumi.StringOutput {
	return o.ApplyT(func(v *LaunchTemplate) pulumi.StringOutput { return v.LatestVersionNumber }).(pulumi.StringOutput)
}

func (o LaunchTemplateOutput) LaunchTemplateData() LaunchTemplateDataOutput {
	return o.ApplyT(func(v *LaunchTemplate) LaunchTemplateDataOutput { return v.LaunchTemplateData }).(LaunchTemplateDataOutput)
}

// LaunchTemplate ID generated by service
func (o LaunchTemplateOutput) LaunchTemplateId() pulumi.StringOutput {
	return o.ApplyT(func(v *LaunchTemplate) pulumi.StringOutput { return v.LaunchTemplateId }).(pulumi.StringOutput)
}

// A name for the launch template.
func (o LaunchTemplateOutput) LaunchTemplateName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LaunchTemplate) pulumi.StringPtrOutput { return v.LaunchTemplateName }).(pulumi.StringPtrOutput)
}

// The tags to apply to the launch template on creation.
func (o LaunchTemplateOutput) TagSpecifications() LaunchTemplateTagSpecificationArrayOutput {
	return o.ApplyT(func(v *LaunchTemplate) LaunchTemplateTagSpecificationArrayOutput { return v.TagSpecifications }).(LaunchTemplateTagSpecificationArrayOutput)
}

// A description for the first version of the launch template.
func (o LaunchTemplateOutput) VersionDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *LaunchTemplate) pulumi.StringPtrOutput { return v.VersionDescription }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*LaunchTemplateInput)(nil)).Elem(), &LaunchTemplate{})
	pulumi.RegisterOutputType(LaunchTemplateOutput{})
}
