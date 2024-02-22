// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package devicefarm

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// AWS::DeviceFarm::InstanceProfile creates a new Device Farm Instance Profile
type InstanceProfile struct {
	pulumi.CustomResourceState

	Arn                           pulumi.StringOutput      `pulumi:"arn"`
	Description                   pulumi.StringPtrOutput   `pulumi:"description"`
	ExcludeAppPackagesFromCleanup pulumi.StringArrayOutput `pulumi:"excludeAppPackagesFromCleanup"`
	Name                          pulumi.StringOutput      `pulumi:"name"`
	PackageCleanup                pulumi.BoolPtrOutput     `pulumi:"packageCleanup"`
	RebootAfterUse                pulumi.BoolPtrOutput     `pulumi:"rebootAfterUse"`
	Tags                          aws.TagArrayOutput       `pulumi:"tags"`
}

// NewInstanceProfile registers a new resource with the given unique name, arguments, and options.
func NewInstanceProfile(ctx *pulumi.Context,
	name string, args *InstanceProfileArgs, opts ...pulumi.ResourceOption) (*InstanceProfile, error) {
	if args == nil {
		args = &InstanceProfileArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource InstanceProfile
	err := ctx.RegisterResource("aws-native:devicefarm:InstanceProfile", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstanceProfile gets an existing InstanceProfile resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstanceProfile(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceProfileState, opts ...pulumi.ResourceOption) (*InstanceProfile, error) {
	var resource InstanceProfile
	err := ctx.ReadResource("aws-native:devicefarm:InstanceProfile", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering InstanceProfile resources.
type instanceProfileState struct {
}

type InstanceProfileState struct {
}

func (InstanceProfileState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceProfileState)(nil)).Elem()
}

type instanceProfileArgs struct {
	Description                   *string   `pulumi:"description"`
	ExcludeAppPackagesFromCleanup []string  `pulumi:"excludeAppPackagesFromCleanup"`
	Name                          *string   `pulumi:"name"`
	PackageCleanup                *bool     `pulumi:"packageCleanup"`
	RebootAfterUse                *bool     `pulumi:"rebootAfterUse"`
	Tags                          []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a InstanceProfile resource.
type InstanceProfileArgs struct {
	Description                   pulumi.StringPtrInput
	ExcludeAppPackagesFromCleanup pulumi.StringArrayInput
	Name                          pulumi.StringPtrInput
	PackageCleanup                pulumi.BoolPtrInput
	RebootAfterUse                pulumi.BoolPtrInput
	Tags                          aws.TagArrayInput
}

func (InstanceProfileArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceProfileArgs)(nil)).Elem()
}

type InstanceProfileInput interface {
	pulumi.Input

	ToInstanceProfileOutput() InstanceProfileOutput
	ToInstanceProfileOutputWithContext(ctx context.Context) InstanceProfileOutput
}

func (*InstanceProfile) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceProfile)(nil)).Elem()
}

func (i *InstanceProfile) ToInstanceProfileOutput() InstanceProfileOutput {
	return i.ToInstanceProfileOutputWithContext(context.Background())
}

func (i *InstanceProfile) ToInstanceProfileOutputWithContext(ctx context.Context) InstanceProfileOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceProfileOutput)
}

type InstanceProfileOutput struct{ *pulumi.OutputState }

func (InstanceProfileOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceProfile)(nil)).Elem()
}

func (o InstanceProfileOutput) ToInstanceProfileOutput() InstanceProfileOutput {
	return o
}

func (o InstanceProfileOutput) ToInstanceProfileOutputWithContext(ctx context.Context) InstanceProfileOutput {
	return o
}

func (o InstanceProfileOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceProfile) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o InstanceProfileOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *InstanceProfile) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o InstanceProfileOutput) ExcludeAppPackagesFromCleanup() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *InstanceProfile) pulumi.StringArrayOutput { return v.ExcludeAppPackagesFromCleanup }).(pulumi.StringArrayOutput)
}

func (o InstanceProfileOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceProfile) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o InstanceProfileOutput) PackageCleanup() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *InstanceProfile) pulumi.BoolPtrOutput { return v.PackageCleanup }).(pulumi.BoolPtrOutput)
}

func (o InstanceProfileOutput) RebootAfterUse() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *InstanceProfile) pulumi.BoolPtrOutput { return v.RebootAfterUse }).(pulumi.BoolPtrOutput)
}

func (o InstanceProfileOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *InstanceProfile) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceProfileInput)(nil)).Elem(), &InstanceProfile{})
	pulumi.RegisterOutputType(InstanceProfileOutput{})
}
