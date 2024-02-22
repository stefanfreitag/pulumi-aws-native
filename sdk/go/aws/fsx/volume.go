// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fsx

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::FSx::Volume
//
// Deprecated: Volume is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Volume struct {
	pulumi.CustomResourceState

	BackupId             pulumi.StringPtrOutput              `pulumi:"backupId"`
	Name                 pulumi.StringOutput                 `pulumi:"name"`
	OntapConfiguration   VolumeOntapConfigurationPtrOutput   `pulumi:"ontapConfiguration"`
	OpenZfsConfiguration VolumeOpenZfsConfigurationPtrOutput `pulumi:"openZfsConfiguration"`
	ResourceArn          pulumi.StringOutput                 `pulumi:"resourceArn"`
	Tags                 aws.TagArrayOutput                  `pulumi:"tags"`
	Uuid                 pulumi.StringOutput                 `pulumi:"uuid"`
	VolumeId             pulumi.StringOutput                 `pulumi:"volumeId"`
	VolumeType           pulumi.StringPtrOutput              `pulumi:"volumeType"`
}

// NewVolume registers a new resource with the given unique name, arguments, and options.
func NewVolume(ctx *pulumi.Context,
	name string, args *VolumeArgs, opts ...pulumi.ResourceOption) (*Volume, error) {
	if args == nil {
		args = &VolumeArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"backupId",
		"volumeType",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Volume
	err := ctx.RegisterResource("aws-native:fsx:Volume", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVolume gets an existing Volume resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVolume(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VolumeState, opts ...pulumi.ResourceOption) (*Volume, error) {
	var resource Volume
	err := ctx.ReadResource("aws-native:fsx:Volume", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Volume resources.
type volumeState struct {
}

type VolumeState struct {
}

func (VolumeState) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeState)(nil)).Elem()
}

type volumeArgs struct {
	BackupId             *string                     `pulumi:"backupId"`
	Name                 *string                     `pulumi:"name"`
	OntapConfiguration   *VolumeOntapConfiguration   `pulumi:"ontapConfiguration"`
	OpenZfsConfiguration *VolumeOpenZfsConfiguration `pulumi:"openZfsConfiguration"`
	Tags                 []aws.Tag                   `pulumi:"tags"`
	VolumeType           *string                     `pulumi:"volumeType"`
}

// The set of arguments for constructing a Volume resource.
type VolumeArgs struct {
	BackupId             pulumi.StringPtrInput
	Name                 pulumi.StringPtrInput
	OntapConfiguration   VolumeOntapConfigurationPtrInput
	OpenZfsConfiguration VolumeOpenZfsConfigurationPtrInput
	Tags                 aws.TagArrayInput
	VolumeType           pulumi.StringPtrInput
}

func (VolumeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeArgs)(nil)).Elem()
}

type VolumeInput interface {
	pulumi.Input

	ToVolumeOutput() VolumeOutput
	ToVolumeOutputWithContext(ctx context.Context) VolumeOutput
}

func (*Volume) ElementType() reflect.Type {
	return reflect.TypeOf((**Volume)(nil)).Elem()
}

func (i *Volume) ToVolumeOutput() VolumeOutput {
	return i.ToVolumeOutputWithContext(context.Background())
}

func (i *Volume) ToVolumeOutputWithContext(ctx context.Context) VolumeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeOutput)
}

type VolumeOutput struct{ *pulumi.OutputState }

func (VolumeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Volume)(nil)).Elem()
}

func (o VolumeOutput) ToVolumeOutput() VolumeOutput {
	return o
}

func (o VolumeOutput) ToVolumeOutputWithContext(ctx context.Context) VolumeOutput {
	return o
}

func (o VolumeOutput) BackupId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringPtrOutput { return v.BackupId }).(pulumi.StringPtrOutput)
}

func (o VolumeOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o VolumeOutput) OntapConfiguration() VolumeOntapConfigurationPtrOutput {
	return o.ApplyT(func(v *Volume) VolumeOntapConfigurationPtrOutput { return v.OntapConfiguration }).(VolumeOntapConfigurationPtrOutput)
}

func (o VolumeOutput) OpenZfsConfiguration() VolumeOpenZfsConfigurationPtrOutput {
	return o.ApplyT(func(v *Volume) VolumeOpenZfsConfigurationPtrOutput { return v.OpenZfsConfiguration }).(VolumeOpenZfsConfigurationPtrOutput)
}

func (o VolumeOutput) ResourceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringOutput { return v.ResourceArn }).(pulumi.StringOutput)
}

func (o VolumeOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Volume) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func (o VolumeOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringOutput { return v.Uuid }).(pulumi.StringOutput)
}

func (o VolumeOutput) VolumeId() pulumi.StringOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringOutput { return v.VolumeId }).(pulumi.StringOutput)
}

func (o VolumeOutput) VolumeType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Volume) pulumi.StringPtrOutput { return v.VolumeType }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VolumeInput)(nil)).Elem(), &Volume{})
	pulumi.RegisterOutputType(VolumeOutput{})
}
