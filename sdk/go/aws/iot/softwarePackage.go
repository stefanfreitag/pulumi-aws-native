// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iot

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// resource definition
type SoftwarePackage struct {
	pulumi.CustomResourceState

	Description pulumi.StringPtrOutput `pulumi:"description"`
	PackageArn  pulumi.StringOutput    `pulumi:"packageArn"`
	PackageName pulumi.StringPtrOutput `pulumi:"packageName"`
	// An array of key-value pairs to apply to this resource.
	Tags SoftwarePackageTagArrayOutput `pulumi:"tags"`
}

// NewSoftwarePackage registers a new resource with the given unique name, arguments, and options.
func NewSoftwarePackage(ctx *pulumi.Context,
	name string, args *SoftwarePackageArgs, opts ...pulumi.ResourceOption) (*SoftwarePackage, error) {
	if args == nil {
		args = &SoftwarePackageArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"packageName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SoftwarePackage
	err := ctx.RegisterResource("aws-native:iot:SoftwarePackage", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSoftwarePackage gets an existing SoftwarePackage resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSoftwarePackage(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SoftwarePackageState, opts ...pulumi.ResourceOption) (*SoftwarePackage, error) {
	var resource SoftwarePackage
	err := ctx.ReadResource("aws-native:iot:SoftwarePackage", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SoftwarePackage resources.
type softwarePackageState struct {
}

type SoftwarePackageState struct {
}

func (SoftwarePackageState) ElementType() reflect.Type {
	return reflect.TypeOf((*softwarePackageState)(nil)).Elem()
}

type softwarePackageArgs struct {
	Description *string `pulumi:"description"`
	PackageName *string `pulumi:"packageName"`
	// An array of key-value pairs to apply to this resource.
	Tags []SoftwarePackageTag `pulumi:"tags"`
}

// The set of arguments for constructing a SoftwarePackage resource.
type SoftwarePackageArgs struct {
	Description pulumi.StringPtrInput
	PackageName pulumi.StringPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags SoftwarePackageTagArrayInput
}

func (SoftwarePackageArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*softwarePackageArgs)(nil)).Elem()
}

type SoftwarePackageInput interface {
	pulumi.Input

	ToSoftwarePackageOutput() SoftwarePackageOutput
	ToSoftwarePackageOutputWithContext(ctx context.Context) SoftwarePackageOutput
}

func (*SoftwarePackage) ElementType() reflect.Type {
	return reflect.TypeOf((**SoftwarePackage)(nil)).Elem()
}

func (i *SoftwarePackage) ToSoftwarePackageOutput() SoftwarePackageOutput {
	return i.ToSoftwarePackageOutputWithContext(context.Background())
}

func (i *SoftwarePackage) ToSoftwarePackageOutputWithContext(ctx context.Context) SoftwarePackageOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SoftwarePackageOutput)
}

func (i *SoftwarePackage) ToOutput(ctx context.Context) pulumix.Output[*SoftwarePackage] {
	return pulumix.Output[*SoftwarePackage]{
		OutputState: i.ToSoftwarePackageOutputWithContext(ctx).OutputState,
	}
}

type SoftwarePackageOutput struct{ *pulumi.OutputState }

func (SoftwarePackageOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SoftwarePackage)(nil)).Elem()
}

func (o SoftwarePackageOutput) ToSoftwarePackageOutput() SoftwarePackageOutput {
	return o
}

func (o SoftwarePackageOutput) ToSoftwarePackageOutputWithContext(ctx context.Context) SoftwarePackageOutput {
	return o
}

func (o SoftwarePackageOutput) ToOutput(ctx context.Context) pulumix.Output[*SoftwarePackage] {
	return pulumix.Output[*SoftwarePackage]{
		OutputState: o.OutputState,
	}
}

func (o SoftwarePackageOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SoftwarePackage) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o SoftwarePackageOutput) PackageArn() pulumi.StringOutput {
	return o.ApplyT(func(v *SoftwarePackage) pulumi.StringOutput { return v.PackageArn }).(pulumi.StringOutput)
}

func (o SoftwarePackageOutput) PackageName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SoftwarePackage) pulumi.StringPtrOutput { return v.PackageName }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o SoftwarePackageOutput) Tags() SoftwarePackageTagArrayOutput {
	return o.ApplyT(func(v *SoftwarePackage) SoftwarePackageTagArrayOutput { return v.Tags }).(SoftwarePackageTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SoftwarePackageInput)(nil)).Elem(), &SoftwarePackage{})
	pulumi.RegisterOutputType(SoftwarePackageOutput{})
}
