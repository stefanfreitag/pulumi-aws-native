// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Describes a route for a local gateway route table.
type LocalGatewayRoute struct {
	pulumi.CustomResourceState

	// The CIDR block used for destination matches.
	DestinationCidrBlock pulumi.StringOutput `pulumi:"destinationCidrBlock"`
	// The ID of the local gateway route table.
	LocalGatewayRouteTableId pulumi.StringOutput `pulumi:"localGatewayRouteTableId"`
	// The ID of the virtual interface group.
	LocalGatewayVirtualInterfaceGroupId pulumi.StringOutput `pulumi:"localGatewayVirtualInterfaceGroupId"`
	// The state of the route.
	State pulumi.StringOutput `pulumi:"state"`
	// The route type.
	Type pulumi.StringOutput `pulumi:"type"`
}

// NewLocalGatewayRoute registers a new resource with the given unique name, arguments, and options.
func NewLocalGatewayRoute(ctx *pulumi.Context,
	name string, args *LocalGatewayRouteArgs, opts ...pulumi.ResourceOption) (*LocalGatewayRoute, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DestinationCidrBlock == nil {
		return nil, errors.New("invalid value for required argument 'DestinationCidrBlock'")
	}
	if args.LocalGatewayRouteTableId == nil {
		return nil, errors.New("invalid value for required argument 'LocalGatewayRouteTableId'")
	}
	if args.LocalGatewayVirtualInterfaceGroupId == nil {
		return nil, errors.New("invalid value for required argument 'LocalGatewayVirtualInterfaceGroupId'")
	}
	var resource LocalGatewayRoute
	err := ctx.RegisterResource("aws-native:ec2:LocalGatewayRoute", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLocalGatewayRoute gets an existing LocalGatewayRoute resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLocalGatewayRoute(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LocalGatewayRouteState, opts ...pulumi.ResourceOption) (*LocalGatewayRoute, error) {
	var resource LocalGatewayRoute
	err := ctx.ReadResource("aws-native:ec2:LocalGatewayRoute", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LocalGatewayRoute resources.
type localGatewayRouteState struct {
}

type LocalGatewayRouteState struct {
}

func (LocalGatewayRouteState) ElementType() reflect.Type {
	return reflect.TypeOf((*localGatewayRouteState)(nil)).Elem()
}

type localGatewayRouteArgs struct {
	// The CIDR block used for destination matches.
	DestinationCidrBlock string `pulumi:"destinationCidrBlock"`
	// The ID of the local gateway route table.
	LocalGatewayRouteTableId string `pulumi:"localGatewayRouteTableId"`
	// The ID of the virtual interface group.
	LocalGatewayVirtualInterfaceGroupId string `pulumi:"localGatewayVirtualInterfaceGroupId"`
}

// The set of arguments for constructing a LocalGatewayRoute resource.
type LocalGatewayRouteArgs struct {
	// The CIDR block used for destination matches.
	DestinationCidrBlock pulumi.StringInput
	// The ID of the local gateway route table.
	LocalGatewayRouteTableId pulumi.StringInput
	// The ID of the virtual interface group.
	LocalGatewayVirtualInterfaceGroupId pulumi.StringInput
}

func (LocalGatewayRouteArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*localGatewayRouteArgs)(nil)).Elem()
}

type LocalGatewayRouteInput interface {
	pulumi.Input

	ToLocalGatewayRouteOutput() LocalGatewayRouteOutput
	ToLocalGatewayRouteOutputWithContext(ctx context.Context) LocalGatewayRouteOutput
}

func (*LocalGatewayRoute) ElementType() reflect.Type {
	return reflect.TypeOf((*LocalGatewayRoute)(nil))
}

func (i *LocalGatewayRoute) ToLocalGatewayRouteOutput() LocalGatewayRouteOutput {
	return i.ToLocalGatewayRouteOutputWithContext(context.Background())
}

func (i *LocalGatewayRoute) ToLocalGatewayRouteOutputWithContext(ctx context.Context) LocalGatewayRouteOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LocalGatewayRouteOutput)
}

type LocalGatewayRouteOutput struct{ *pulumi.OutputState }

func (LocalGatewayRouteOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LocalGatewayRoute)(nil))
}

func (o LocalGatewayRouteOutput) ToLocalGatewayRouteOutput() LocalGatewayRouteOutput {
	return o
}

func (o LocalGatewayRouteOutput) ToLocalGatewayRouteOutputWithContext(ctx context.Context) LocalGatewayRouteOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(LocalGatewayRouteOutput{})
}
