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

// Resource Type definition for AWS::EC2::VPNConnection
type VpnConnection struct {
	pulumi.CustomResourceState

	// The ID of the customer gateway at your end of the VPN connection.
	CustomerGatewayId pulumi.StringOutput `pulumi:"customerGatewayId"`
	// Indicates whether the VPN connection uses static routes only.
	StaticRoutesOnly pulumi.BoolPtrOutput `pulumi:"staticRoutesOnly"`
	// Any tags assigned to the VPN connection.
	Tags VpnConnectionTagArrayOutput `pulumi:"tags"`
	// The ID of the transit gateway associated with the VPN connection.
	TransitGatewayId pulumi.StringPtrOutput `pulumi:"transitGatewayId"`
	// The type of VPN connection.
	Type pulumi.StringOutput `pulumi:"type"`
	// The provider-assigned unique ID for this managed resource
	VpnConnectionId pulumi.StringOutput `pulumi:"vpnConnectionId"`
	// The ID of the virtual private gateway at the AWS side of the VPN connection.
	VpnGatewayId pulumi.StringPtrOutput `pulumi:"vpnGatewayId"`
	// The tunnel options for the VPN connection.
	VpnTunnelOptionsSpecifications VpnConnectionVpnTunnelOptionsSpecificationArrayOutput `pulumi:"vpnTunnelOptionsSpecifications"`
}

// NewVpnConnection registers a new resource with the given unique name, arguments, and options.
func NewVpnConnection(ctx *pulumi.Context,
	name string, args *VpnConnectionArgs, opts ...pulumi.ResourceOption) (*VpnConnection, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CustomerGatewayId == nil {
		return nil, errors.New("invalid value for required argument 'CustomerGatewayId'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"customerGatewayId",
		"staticRoutesOnly",
		"transitGatewayId",
		"type",
		"vpnGatewayId",
		"vpnTunnelOptionsSpecifications[*]",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource VpnConnection
	err := ctx.RegisterResource("aws-native:ec2:VpnConnection", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVpnConnection gets an existing VpnConnection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpnConnection(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VpnConnectionState, opts ...pulumi.ResourceOption) (*VpnConnection, error) {
	var resource VpnConnection
	err := ctx.ReadResource("aws-native:ec2:VpnConnection", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VpnConnection resources.
type vpnConnectionState struct {
}

type VpnConnectionState struct {
}

func (VpnConnectionState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpnConnectionState)(nil)).Elem()
}

type vpnConnectionArgs struct {
	// The ID of the customer gateway at your end of the VPN connection.
	CustomerGatewayId string `pulumi:"customerGatewayId"`
	// Indicates whether the VPN connection uses static routes only.
	StaticRoutesOnly *bool `pulumi:"staticRoutesOnly"`
	// Any tags assigned to the VPN connection.
	Tags []VpnConnectionTag `pulumi:"tags"`
	// The ID of the transit gateway associated with the VPN connection.
	TransitGatewayId *string `pulumi:"transitGatewayId"`
	// The type of VPN connection.
	Type string `pulumi:"type"`
	// The ID of the virtual private gateway at the AWS side of the VPN connection.
	VpnGatewayId *string `pulumi:"vpnGatewayId"`
	// The tunnel options for the VPN connection.
	VpnTunnelOptionsSpecifications []VpnConnectionVpnTunnelOptionsSpecification `pulumi:"vpnTunnelOptionsSpecifications"`
}

// The set of arguments for constructing a VpnConnection resource.
type VpnConnectionArgs struct {
	// The ID of the customer gateway at your end of the VPN connection.
	CustomerGatewayId pulumi.StringInput
	// Indicates whether the VPN connection uses static routes only.
	StaticRoutesOnly pulumi.BoolPtrInput
	// Any tags assigned to the VPN connection.
	Tags VpnConnectionTagArrayInput
	// The ID of the transit gateway associated with the VPN connection.
	TransitGatewayId pulumi.StringPtrInput
	// The type of VPN connection.
	Type pulumi.StringInput
	// The ID of the virtual private gateway at the AWS side of the VPN connection.
	VpnGatewayId pulumi.StringPtrInput
	// The tunnel options for the VPN connection.
	VpnTunnelOptionsSpecifications VpnConnectionVpnTunnelOptionsSpecificationArrayInput
}

func (VpnConnectionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpnConnectionArgs)(nil)).Elem()
}

type VpnConnectionInput interface {
	pulumi.Input

	ToVpnConnectionOutput() VpnConnectionOutput
	ToVpnConnectionOutputWithContext(ctx context.Context) VpnConnectionOutput
}

func (*VpnConnection) ElementType() reflect.Type {
	return reflect.TypeOf((**VpnConnection)(nil)).Elem()
}

func (i *VpnConnection) ToVpnConnectionOutput() VpnConnectionOutput {
	return i.ToVpnConnectionOutputWithContext(context.Background())
}

func (i *VpnConnection) ToVpnConnectionOutputWithContext(ctx context.Context) VpnConnectionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VpnConnectionOutput)
}

func (i *VpnConnection) ToOutput(ctx context.Context) pulumix.Output[*VpnConnection] {
	return pulumix.Output[*VpnConnection]{
		OutputState: i.ToVpnConnectionOutputWithContext(ctx).OutputState,
	}
}

type VpnConnectionOutput struct{ *pulumi.OutputState }

func (VpnConnectionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VpnConnection)(nil)).Elem()
}

func (o VpnConnectionOutput) ToVpnConnectionOutput() VpnConnectionOutput {
	return o
}

func (o VpnConnectionOutput) ToVpnConnectionOutputWithContext(ctx context.Context) VpnConnectionOutput {
	return o
}

func (o VpnConnectionOutput) ToOutput(ctx context.Context) pulumix.Output[*VpnConnection] {
	return pulumix.Output[*VpnConnection]{
		OutputState: o.OutputState,
	}
}

// The ID of the customer gateway at your end of the VPN connection.
func (o VpnConnectionOutput) CustomerGatewayId() pulumi.StringOutput {
	return o.ApplyT(func(v *VpnConnection) pulumi.StringOutput { return v.CustomerGatewayId }).(pulumi.StringOutput)
}

// Indicates whether the VPN connection uses static routes only.
func (o VpnConnectionOutput) StaticRoutesOnly() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *VpnConnection) pulumi.BoolPtrOutput { return v.StaticRoutesOnly }).(pulumi.BoolPtrOutput)
}

// Any tags assigned to the VPN connection.
func (o VpnConnectionOutput) Tags() VpnConnectionTagArrayOutput {
	return o.ApplyT(func(v *VpnConnection) VpnConnectionTagArrayOutput { return v.Tags }).(VpnConnectionTagArrayOutput)
}

// The ID of the transit gateway associated with the VPN connection.
func (o VpnConnectionOutput) TransitGatewayId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VpnConnection) pulumi.StringPtrOutput { return v.TransitGatewayId }).(pulumi.StringPtrOutput)
}

// The type of VPN connection.
func (o VpnConnectionOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v *VpnConnection) pulumi.StringOutput { return v.Type }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource
func (o VpnConnectionOutput) VpnConnectionId() pulumi.StringOutput {
	return o.ApplyT(func(v *VpnConnection) pulumi.StringOutput { return v.VpnConnectionId }).(pulumi.StringOutput)
}

// The ID of the virtual private gateway at the AWS side of the VPN connection.
func (o VpnConnectionOutput) VpnGatewayId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VpnConnection) pulumi.StringPtrOutput { return v.VpnGatewayId }).(pulumi.StringPtrOutput)
}

// The tunnel options for the VPN connection.
func (o VpnConnectionOutput) VpnTunnelOptionsSpecifications() VpnConnectionVpnTunnelOptionsSpecificationArrayOutput {
	return o.ApplyT(func(v *VpnConnection) VpnConnectionVpnTunnelOptionsSpecificationArrayOutput {
		return v.VpnTunnelOptionsSpecifications
	}).(VpnConnectionVpnTunnelOptionsSpecificationArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VpnConnectionInput)(nil)).Elem(), &VpnConnection{})
	pulumi.RegisterOutputType(VpnConnectionOutput{})
}
