// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package connect

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Connect::Instance
type Instance struct {
	pulumi.CustomResourceState

	// An instanceArn is automatically generated on creation based on instanceId.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The attributes for the instance.
	Attributes InstanceAttributesOutput `pulumi:"attributes"`
	// Timestamp of instance creation logged as part of instance creation.
	CreatedTime pulumi.StringOutput `pulumi:"createdTime"`
	// Existing directoryId user wants to map to the new Connect instance.
	DirectoryId pulumi.StringPtrOutput `pulumi:"directoryId"`
	// Specifies the type of directory integration for new instance.
	IdentityManagementType InstanceIdentityManagementTypeOutput `pulumi:"identityManagementType"`
	// Alias of the new directory created as part of new instance creation.
	InstanceAlias pulumi.StringPtrOutput `pulumi:"instanceAlias"`
	// Specifies the creation status of new instance.
	InstanceStatus InstanceStatusOutput `pulumi:"instanceStatus"`
	// Service linked role created as part of instance creation.
	ServiceRole pulumi.StringOutput `pulumi:"serviceRole"`
}

// NewInstance registers a new resource with the given unique name, arguments, and options.
func NewInstance(ctx *pulumi.Context,
	name string, args *InstanceArgs, opts ...pulumi.ResourceOption) (*Instance, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Attributes == nil {
		return nil, errors.New("invalid value for required argument 'Attributes'")
	}
	if args.IdentityManagementType == nil {
		return nil, errors.New("invalid value for required argument 'IdentityManagementType'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"directoryId",
		"identityManagementType",
		"instanceAlias",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Instance
	err := ctx.RegisterResource("aws-native:connect:Instance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstance gets an existing Instance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceState, opts ...pulumi.ResourceOption) (*Instance, error) {
	var resource Instance
	err := ctx.ReadResource("aws-native:connect:Instance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Instance resources.
type instanceState struct {
}

type InstanceState struct {
}

func (InstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceState)(nil)).Elem()
}

type instanceArgs struct {
	// The attributes for the instance.
	Attributes InstanceAttributes `pulumi:"attributes"`
	// Existing directoryId user wants to map to the new Connect instance.
	DirectoryId *string `pulumi:"directoryId"`
	// Specifies the type of directory integration for new instance.
	IdentityManagementType InstanceIdentityManagementType `pulumi:"identityManagementType"`
	// Alias of the new directory created as part of new instance creation.
	InstanceAlias *string `pulumi:"instanceAlias"`
}

// The set of arguments for constructing a Instance resource.
type InstanceArgs struct {
	// The attributes for the instance.
	Attributes InstanceAttributesInput
	// Existing directoryId user wants to map to the new Connect instance.
	DirectoryId pulumi.StringPtrInput
	// Specifies the type of directory integration for new instance.
	IdentityManagementType InstanceIdentityManagementTypeInput
	// Alias of the new directory created as part of new instance creation.
	InstanceAlias pulumi.StringPtrInput
}

func (InstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceArgs)(nil)).Elem()
}

type InstanceInput interface {
	pulumi.Input

	ToInstanceOutput() InstanceOutput
	ToInstanceOutputWithContext(ctx context.Context) InstanceOutput
}

func (*Instance) ElementType() reflect.Type {
	return reflect.TypeOf((**Instance)(nil)).Elem()
}

func (i *Instance) ToInstanceOutput() InstanceOutput {
	return i.ToInstanceOutputWithContext(context.Background())
}

func (i *Instance) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceOutput)
}

func (i *Instance) ToOutput(ctx context.Context) pulumix.Output[*Instance] {
	return pulumix.Output[*Instance]{
		OutputState: i.ToInstanceOutputWithContext(ctx).OutputState,
	}
}

type InstanceOutput struct{ *pulumi.OutputState }

func (InstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Instance)(nil)).Elem()
}

func (o InstanceOutput) ToInstanceOutput() InstanceOutput {
	return o
}

func (o InstanceOutput) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return o
}

func (o InstanceOutput) ToOutput(ctx context.Context) pulumix.Output[*Instance] {
	return pulumix.Output[*Instance]{
		OutputState: o.OutputState,
	}
}

// An instanceArn is automatically generated on creation based on instanceId.
func (o InstanceOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The attributes for the instance.
func (o InstanceOutput) Attributes() InstanceAttributesOutput {
	return o.ApplyT(func(v *Instance) InstanceAttributesOutput { return v.Attributes }).(InstanceAttributesOutput)
}

// Timestamp of instance creation logged as part of instance creation.
func (o InstanceOutput) CreatedTime() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.CreatedTime }).(pulumi.StringOutput)
}

// Existing directoryId user wants to map to the new Connect instance.
func (o InstanceOutput) DirectoryId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringPtrOutput { return v.DirectoryId }).(pulumi.StringPtrOutput)
}

// Specifies the type of directory integration for new instance.
func (o InstanceOutput) IdentityManagementType() InstanceIdentityManagementTypeOutput {
	return o.ApplyT(func(v *Instance) InstanceIdentityManagementTypeOutput { return v.IdentityManagementType }).(InstanceIdentityManagementTypeOutput)
}

// Alias of the new directory created as part of new instance creation.
func (o InstanceOutput) InstanceAlias() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringPtrOutput { return v.InstanceAlias }).(pulumi.StringPtrOutput)
}

// Specifies the creation status of new instance.
func (o InstanceOutput) InstanceStatus() InstanceStatusOutput {
	return o.ApplyT(func(v *Instance) InstanceStatusOutput { return v.InstanceStatus }).(InstanceStatusOutput)
}

// Service linked role created as part of instance creation.
func (o InstanceOutput) ServiceRole() pulumi.StringOutput {
	return o.ApplyT(func(v *Instance) pulumi.StringOutput { return v.ServiceRole }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceInput)(nil)).Elem(), &Instance{})
	pulumi.RegisterOutputType(InstanceOutput{})
}
