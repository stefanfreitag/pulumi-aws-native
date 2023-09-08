// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package fsx

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::FSx::StorageVirtualMachine
//
// Deprecated: StorageVirtualMachine is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type StorageVirtualMachine struct {
	pulumi.CustomResourceState

	ActiveDirectoryConfiguration StorageVirtualMachineActiveDirectoryConfigurationPtrOutput `pulumi:"activeDirectoryConfiguration"`
	FileSystemId                 pulumi.StringOutput                                        `pulumi:"fileSystemId"`
	Name                         pulumi.StringOutput                                        `pulumi:"name"`
	ResourceArn                  pulumi.StringOutput                                        `pulumi:"resourceArn"`
	RootVolumeSecurityStyle      pulumi.StringPtrOutput                                     `pulumi:"rootVolumeSecurityStyle"`
	StorageVirtualMachineId      pulumi.StringOutput                                        `pulumi:"storageVirtualMachineId"`
	SvmAdminPassword             pulumi.StringPtrOutput                                     `pulumi:"svmAdminPassword"`
	Tags                         StorageVirtualMachineTagArrayOutput                        `pulumi:"tags"`
	Uuid                         pulumi.StringOutput                                        `pulumi:"uuid"`
}

// NewStorageVirtualMachine registers a new resource with the given unique name, arguments, and options.
func NewStorageVirtualMachine(ctx *pulumi.Context,
	name string, args *StorageVirtualMachineArgs, opts ...pulumi.ResourceOption) (*StorageVirtualMachine, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FileSystemId == nil {
		return nil, errors.New("invalid value for required argument 'FileSystemId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"fileSystemId",
		"name",
		"rootVolumeSecurityStyle",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource StorageVirtualMachine
	err := ctx.RegisterResource("aws-native:fsx:StorageVirtualMachine", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStorageVirtualMachine gets an existing StorageVirtualMachine resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStorageVirtualMachine(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StorageVirtualMachineState, opts ...pulumi.ResourceOption) (*StorageVirtualMachine, error) {
	var resource StorageVirtualMachine
	err := ctx.ReadResource("aws-native:fsx:StorageVirtualMachine", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StorageVirtualMachine resources.
type storageVirtualMachineState struct {
}

type StorageVirtualMachineState struct {
}

func (StorageVirtualMachineState) ElementType() reflect.Type {
	return reflect.TypeOf((*storageVirtualMachineState)(nil)).Elem()
}

type storageVirtualMachineArgs struct {
	ActiveDirectoryConfiguration *StorageVirtualMachineActiveDirectoryConfiguration `pulumi:"activeDirectoryConfiguration"`
	FileSystemId                 string                                             `pulumi:"fileSystemId"`
	Name                         *string                                            `pulumi:"name"`
	RootVolumeSecurityStyle      *string                                            `pulumi:"rootVolumeSecurityStyle"`
	SvmAdminPassword             *string                                            `pulumi:"svmAdminPassword"`
	Tags                         []StorageVirtualMachineTag                         `pulumi:"tags"`
}

// The set of arguments for constructing a StorageVirtualMachine resource.
type StorageVirtualMachineArgs struct {
	ActiveDirectoryConfiguration StorageVirtualMachineActiveDirectoryConfigurationPtrInput
	FileSystemId                 pulumi.StringInput
	Name                         pulumi.StringPtrInput
	RootVolumeSecurityStyle      pulumi.StringPtrInput
	SvmAdminPassword             pulumi.StringPtrInput
	Tags                         StorageVirtualMachineTagArrayInput
}

func (StorageVirtualMachineArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*storageVirtualMachineArgs)(nil)).Elem()
}

type StorageVirtualMachineInput interface {
	pulumi.Input

	ToStorageVirtualMachineOutput() StorageVirtualMachineOutput
	ToStorageVirtualMachineOutputWithContext(ctx context.Context) StorageVirtualMachineOutput
}

func (*StorageVirtualMachine) ElementType() reflect.Type {
	return reflect.TypeOf((**StorageVirtualMachine)(nil)).Elem()
}

func (i *StorageVirtualMachine) ToStorageVirtualMachineOutput() StorageVirtualMachineOutput {
	return i.ToStorageVirtualMachineOutputWithContext(context.Background())
}

func (i *StorageVirtualMachine) ToStorageVirtualMachineOutputWithContext(ctx context.Context) StorageVirtualMachineOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StorageVirtualMachineOutput)
}

func (i *StorageVirtualMachine) ToOutput(ctx context.Context) pulumix.Output[*StorageVirtualMachine] {
	return pulumix.Output[*StorageVirtualMachine]{
		OutputState: i.ToStorageVirtualMachineOutputWithContext(ctx).OutputState,
	}
}

type StorageVirtualMachineOutput struct{ *pulumi.OutputState }

func (StorageVirtualMachineOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StorageVirtualMachine)(nil)).Elem()
}

func (o StorageVirtualMachineOutput) ToStorageVirtualMachineOutput() StorageVirtualMachineOutput {
	return o
}

func (o StorageVirtualMachineOutput) ToStorageVirtualMachineOutputWithContext(ctx context.Context) StorageVirtualMachineOutput {
	return o
}

func (o StorageVirtualMachineOutput) ToOutput(ctx context.Context) pulumix.Output[*StorageVirtualMachine] {
	return pulumix.Output[*StorageVirtualMachine]{
		OutputState: o.OutputState,
	}
}

func (o StorageVirtualMachineOutput) ActiveDirectoryConfiguration() StorageVirtualMachineActiveDirectoryConfigurationPtrOutput {
	return o.ApplyT(func(v *StorageVirtualMachine) StorageVirtualMachineActiveDirectoryConfigurationPtrOutput {
		return v.ActiveDirectoryConfiguration
	}).(StorageVirtualMachineActiveDirectoryConfigurationPtrOutput)
}

func (o StorageVirtualMachineOutput) FileSystemId() pulumi.StringOutput {
	return o.ApplyT(func(v *StorageVirtualMachine) pulumi.StringOutput { return v.FileSystemId }).(pulumi.StringOutput)
}

func (o StorageVirtualMachineOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *StorageVirtualMachine) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o StorageVirtualMachineOutput) ResourceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *StorageVirtualMachine) pulumi.StringOutput { return v.ResourceArn }).(pulumi.StringOutput)
}

func (o StorageVirtualMachineOutput) RootVolumeSecurityStyle() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StorageVirtualMachine) pulumi.StringPtrOutput { return v.RootVolumeSecurityStyle }).(pulumi.StringPtrOutput)
}

func (o StorageVirtualMachineOutput) StorageVirtualMachineId() pulumi.StringOutput {
	return o.ApplyT(func(v *StorageVirtualMachine) pulumi.StringOutput { return v.StorageVirtualMachineId }).(pulumi.StringOutput)
}

func (o StorageVirtualMachineOutput) SvmAdminPassword() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *StorageVirtualMachine) pulumi.StringPtrOutput { return v.SvmAdminPassword }).(pulumi.StringPtrOutput)
}

func (o StorageVirtualMachineOutput) Tags() StorageVirtualMachineTagArrayOutput {
	return o.ApplyT(func(v *StorageVirtualMachine) StorageVirtualMachineTagArrayOutput { return v.Tags }).(StorageVirtualMachineTagArrayOutput)
}

func (o StorageVirtualMachineOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v *StorageVirtualMachine) pulumi.StringOutput { return v.Uuid }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StorageVirtualMachineInput)(nil)).Elem(), &StorageVirtualMachine{})
	pulumi.RegisterOutputType(StorageVirtualMachineOutput{})
}
