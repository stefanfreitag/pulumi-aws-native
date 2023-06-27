// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appstream

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AppStream::StackFleetAssociation
//
// Deprecated: StackFleetAssociation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type StackFleetAssociation struct {
	pulumi.CustomResourceState

	FleetName pulumi.StringOutput `pulumi:"fleetName"`
	StackName pulumi.StringOutput `pulumi:"stackName"`
}

// NewStackFleetAssociation registers a new resource with the given unique name, arguments, and options.
func NewStackFleetAssociation(ctx *pulumi.Context,
	name string, args *StackFleetAssociationArgs, opts ...pulumi.ResourceOption) (*StackFleetAssociation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FleetName == nil {
		return nil, errors.New("invalid value for required argument 'FleetName'")
	}
	if args.StackName == nil {
		return nil, errors.New("invalid value for required argument 'StackName'")
	}
	var resource StackFleetAssociation
	err := ctx.RegisterResource("aws-native:appstream:StackFleetAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetStackFleetAssociation gets an existing StackFleetAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetStackFleetAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *StackFleetAssociationState, opts ...pulumi.ResourceOption) (*StackFleetAssociation, error) {
	var resource StackFleetAssociation
	err := ctx.ReadResource("aws-native:appstream:StackFleetAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering StackFleetAssociation resources.
type stackFleetAssociationState struct {
}

type StackFleetAssociationState struct {
}

func (StackFleetAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*stackFleetAssociationState)(nil)).Elem()
}

type stackFleetAssociationArgs struct {
	FleetName string `pulumi:"fleetName"`
	StackName string `pulumi:"stackName"`
}

// The set of arguments for constructing a StackFleetAssociation resource.
type StackFleetAssociationArgs struct {
	FleetName pulumi.StringInput
	StackName pulumi.StringInput
}

func (StackFleetAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*stackFleetAssociationArgs)(nil)).Elem()
}

type StackFleetAssociationInput interface {
	pulumi.Input

	ToStackFleetAssociationOutput() StackFleetAssociationOutput
	ToStackFleetAssociationOutputWithContext(ctx context.Context) StackFleetAssociationOutput
}

func (*StackFleetAssociation) ElementType() reflect.Type {
	return reflect.TypeOf((**StackFleetAssociation)(nil)).Elem()
}

func (i *StackFleetAssociation) ToStackFleetAssociationOutput() StackFleetAssociationOutput {
	return i.ToStackFleetAssociationOutputWithContext(context.Background())
}

func (i *StackFleetAssociation) ToStackFleetAssociationOutputWithContext(ctx context.Context) StackFleetAssociationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(StackFleetAssociationOutput)
}

type StackFleetAssociationOutput struct{ *pulumi.OutputState }

func (StackFleetAssociationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**StackFleetAssociation)(nil)).Elem()
}

func (o StackFleetAssociationOutput) ToStackFleetAssociationOutput() StackFleetAssociationOutput {
	return o
}

func (o StackFleetAssociationOutput) ToStackFleetAssociationOutputWithContext(ctx context.Context) StackFleetAssociationOutput {
	return o
}

func (o StackFleetAssociationOutput) FleetName() pulumi.StringOutput {
	return o.ApplyT(func(v *StackFleetAssociation) pulumi.StringOutput { return v.FleetName }).(pulumi.StringOutput)
}

func (o StackFleetAssociationOutput) StackName() pulumi.StringOutput {
	return o.ApplyT(func(v *StackFleetAssociation) pulumi.StringOutput { return v.StackName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*StackFleetAssociationInput)(nil)).Elem(), &StackFleetAssociation{})
	pulumi.RegisterOutputType(StackFleetAssociationOutput{})
}
