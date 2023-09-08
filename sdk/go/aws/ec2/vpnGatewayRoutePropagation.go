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

// Resource Type definition for AWS::EC2::VPNGatewayRoutePropagation
//
// Deprecated: VpnGatewayRoutePropagation is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type VpnGatewayRoutePropagation struct {
	pulumi.CustomResourceState

	RouteTableIds pulumi.StringArrayOutput `pulumi:"routeTableIds"`
	VpnGatewayId  pulumi.StringOutput      `pulumi:"vpnGatewayId"`
}

// NewVpnGatewayRoutePropagation registers a new resource with the given unique name, arguments, and options.
func NewVpnGatewayRoutePropagation(ctx *pulumi.Context,
	name string, args *VpnGatewayRoutePropagationArgs, opts ...pulumi.ResourceOption) (*VpnGatewayRoutePropagation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.RouteTableIds == nil {
		return nil, errors.New("invalid value for required argument 'RouteTableIds'")
	}
	if args.VpnGatewayId == nil {
		return nil, errors.New("invalid value for required argument 'VpnGatewayId'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource VpnGatewayRoutePropagation
	err := ctx.RegisterResource("aws-native:ec2:VpnGatewayRoutePropagation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVpnGatewayRoutePropagation gets an existing VpnGatewayRoutePropagation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpnGatewayRoutePropagation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VpnGatewayRoutePropagationState, opts ...pulumi.ResourceOption) (*VpnGatewayRoutePropagation, error) {
	var resource VpnGatewayRoutePropagation
	err := ctx.ReadResource("aws-native:ec2:VpnGatewayRoutePropagation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VpnGatewayRoutePropagation resources.
type vpnGatewayRoutePropagationState struct {
}

type VpnGatewayRoutePropagationState struct {
}

func (VpnGatewayRoutePropagationState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpnGatewayRoutePropagationState)(nil)).Elem()
}

type vpnGatewayRoutePropagationArgs struct {
	RouteTableIds []string `pulumi:"routeTableIds"`
	VpnGatewayId  string   `pulumi:"vpnGatewayId"`
}

// The set of arguments for constructing a VpnGatewayRoutePropagation resource.
type VpnGatewayRoutePropagationArgs struct {
	RouteTableIds pulumi.StringArrayInput
	VpnGatewayId  pulumi.StringInput
}

func (VpnGatewayRoutePropagationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpnGatewayRoutePropagationArgs)(nil)).Elem()
}

type VpnGatewayRoutePropagationInput interface {
	pulumi.Input

	ToVpnGatewayRoutePropagationOutput() VpnGatewayRoutePropagationOutput
	ToVpnGatewayRoutePropagationOutputWithContext(ctx context.Context) VpnGatewayRoutePropagationOutput
}

func (*VpnGatewayRoutePropagation) ElementType() reflect.Type {
	return reflect.TypeOf((**VpnGatewayRoutePropagation)(nil)).Elem()
}

func (i *VpnGatewayRoutePropagation) ToVpnGatewayRoutePropagationOutput() VpnGatewayRoutePropagationOutput {
	return i.ToVpnGatewayRoutePropagationOutputWithContext(context.Background())
}

func (i *VpnGatewayRoutePropagation) ToVpnGatewayRoutePropagationOutputWithContext(ctx context.Context) VpnGatewayRoutePropagationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VpnGatewayRoutePropagationOutput)
}

func (i *VpnGatewayRoutePropagation) ToOutput(ctx context.Context) pulumix.Output[*VpnGatewayRoutePropagation] {
	return pulumix.Output[*VpnGatewayRoutePropagation]{
		OutputState: i.ToVpnGatewayRoutePropagationOutputWithContext(ctx).OutputState,
	}
}

type VpnGatewayRoutePropagationOutput struct{ *pulumi.OutputState }

func (VpnGatewayRoutePropagationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VpnGatewayRoutePropagation)(nil)).Elem()
}

func (o VpnGatewayRoutePropagationOutput) ToVpnGatewayRoutePropagationOutput() VpnGatewayRoutePropagationOutput {
	return o
}

func (o VpnGatewayRoutePropagationOutput) ToVpnGatewayRoutePropagationOutputWithContext(ctx context.Context) VpnGatewayRoutePropagationOutput {
	return o
}

func (o VpnGatewayRoutePropagationOutput) ToOutput(ctx context.Context) pulumix.Output[*VpnGatewayRoutePropagation] {
	return pulumix.Output[*VpnGatewayRoutePropagation]{
		OutputState: o.OutputState,
	}
}

func (o VpnGatewayRoutePropagationOutput) RouteTableIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *VpnGatewayRoutePropagation) pulumi.StringArrayOutput { return v.RouteTableIds }).(pulumi.StringArrayOutput)
}

func (o VpnGatewayRoutePropagationOutput) VpnGatewayId() pulumi.StringOutput {
	return o.ApplyT(func(v *VpnGatewayRoutePropagation) pulumi.StringOutput { return v.VpnGatewayId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VpnGatewayRoutePropagationInput)(nil)).Elem(), &VpnGatewayRoutePropagation{})
	pulumi.RegisterOutputType(VpnGatewayRoutePropagationOutput{})
}
