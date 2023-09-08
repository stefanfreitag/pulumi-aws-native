// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::EC2::EIPAssociation
type EipAssociation struct {
	pulumi.CustomResourceState

	AllocationId       pulumi.StringPtrOutput `pulumi:"allocationId"`
	Eip                pulumi.StringPtrOutput `pulumi:"eip"`
	InstanceId         pulumi.StringPtrOutput `pulumi:"instanceId"`
	NetworkInterfaceId pulumi.StringPtrOutput `pulumi:"networkInterfaceId"`
	PrivateIpAddress   pulumi.StringPtrOutput `pulumi:"privateIpAddress"`
}

// NewEipAssociation registers a new resource with the given unique name, arguments, and options.
func NewEipAssociation(ctx *pulumi.Context,
	name string, args *EipAssociationArgs, opts ...pulumi.ResourceOption) (*EipAssociation, error) {
	if args == nil {
		args = &EipAssociationArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource EipAssociation
	err := ctx.RegisterResource("aws-native:ec2:EipAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEipAssociation gets an existing EipAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEipAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EipAssociationState, opts ...pulumi.ResourceOption) (*EipAssociation, error) {
	var resource EipAssociation
	err := ctx.ReadResource("aws-native:ec2:EipAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EipAssociation resources.
type eipAssociationState struct {
}

type EipAssociationState struct {
}

func (EipAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*eipAssociationState)(nil)).Elem()
}

type eipAssociationArgs struct {
	AllocationId       *string `pulumi:"allocationId"`
	Eip                *string `pulumi:"eip"`
	InstanceId         *string `pulumi:"instanceId"`
	NetworkInterfaceId *string `pulumi:"networkInterfaceId"`
	PrivateIpAddress   *string `pulumi:"privateIpAddress"`
}

// The set of arguments for constructing a EipAssociation resource.
type EipAssociationArgs struct {
	AllocationId       pulumi.StringPtrInput
	Eip                pulumi.StringPtrInput
	InstanceId         pulumi.StringPtrInput
	NetworkInterfaceId pulumi.StringPtrInput
	PrivateIpAddress   pulumi.StringPtrInput
}

func (EipAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*eipAssociationArgs)(nil)).Elem()
}

type EipAssociationInput interface {
	pulumi.Input

	ToEipAssociationOutput() EipAssociationOutput
	ToEipAssociationOutputWithContext(ctx context.Context) EipAssociationOutput
}

func (*EipAssociation) ElementType() reflect.Type {
	return reflect.TypeOf((**EipAssociation)(nil)).Elem()
}

func (i *EipAssociation) ToEipAssociationOutput() EipAssociationOutput {
	return i.ToEipAssociationOutputWithContext(context.Background())
}

func (i *EipAssociation) ToEipAssociationOutputWithContext(ctx context.Context) EipAssociationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EipAssociationOutput)
}

func (i *EipAssociation) ToOutput(ctx context.Context) pulumix.Output[*EipAssociation] {
	return pulumix.Output[*EipAssociation]{
		OutputState: i.ToEipAssociationOutputWithContext(ctx).OutputState,
	}
}

type EipAssociationOutput struct{ *pulumi.OutputState }

func (EipAssociationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EipAssociation)(nil)).Elem()
}

func (o EipAssociationOutput) ToEipAssociationOutput() EipAssociationOutput {
	return o
}

func (o EipAssociationOutput) ToEipAssociationOutputWithContext(ctx context.Context) EipAssociationOutput {
	return o
}

func (o EipAssociationOutput) ToOutput(ctx context.Context) pulumix.Output[*EipAssociation] {
	return pulumix.Output[*EipAssociation]{
		OutputState: o.OutputState,
	}
}

func (o EipAssociationOutput) AllocationId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EipAssociation) pulumi.StringPtrOutput { return v.AllocationId }).(pulumi.StringPtrOutput)
}

func (o EipAssociationOutput) Eip() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EipAssociation) pulumi.StringPtrOutput { return v.Eip }).(pulumi.StringPtrOutput)
}

func (o EipAssociationOutput) InstanceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EipAssociation) pulumi.StringPtrOutput { return v.InstanceId }).(pulumi.StringPtrOutput)
}

func (o EipAssociationOutput) NetworkInterfaceId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EipAssociation) pulumi.StringPtrOutput { return v.NetworkInterfaceId }).(pulumi.StringPtrOutput)
}

func (o EipAssociationOutput) PrivateIpAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EipAssociation) pulumi.StringPtrOutput { return v.PrivateIpAddress }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EipAssociationInput)(nil)).Elem(), &EipAssociation{})
	pulumi.RegisterOutputType(EipAssociationOutput{})
}
