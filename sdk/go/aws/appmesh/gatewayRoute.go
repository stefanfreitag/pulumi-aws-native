// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appmesh

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::AppMesh::GatewayRoute
//
// Deprecated: GatewayRoute is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type GatewayRoute struct {
	pulumi.CustomResourceState

	Arn                pulumi.StringOutput        `pulumi:"arn"`
	GatewayRouteName   pulumi.StringPtrOutput     `pulumi:"gatewayRouteName"`
	MeshName           pulumi.StringOutput        `pulumi:"meshName"`
	MeshOwner          pulumi.StringPtrOutput     `pulumi:"meshOwner"`
	ResourceOwner      pulumi.StringOutput        `pulumi:"resourceOwner"`
	Spec               GatewayRouteSpecOutput     `pulumi:"spec"`
	Tags               GatewayRouteTagArrayOutput `pulumi:"tags"`
	Uid                pulumi.StringOutput        `pulumi:"uid"`
	VirtualGatewayName pulumi.StringOutput        `pulumi:"virtualGatewayName"`
}

// NewGatewayRoute registers a new resource with the given unique name, arguments, and options.
func NewGatewayRoute(ctx *pulumi.Context,
	name string, args *GatewayRouteArgs, opts ...pulumi.ResourceOption) (*GatewayRoute, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.MeshName == nil {
		return nil, errors.New("invalid value for required argument 'MeshName'")
	}
	if args.Spec == nil {
		return nil, errors.New("invalid value for required argument 'Spec'")
	}
	if args.VirtualGatewayName == nil {
		return nil, errors.New("invalid value for required argument 'VirtualGatewayName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"gatewayRouteName",
		"meshName",
		"meshOwner",
		"virtualGatewayName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource GatewayRoute
	err := ctx.RegisterResource("aws-native:appmesh:GatewayRoute", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGatewayRoute gets an existing GatewayRoute resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGatewayRoute(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GatewayRouteState, opts ...pulumi.ResourceOption) (*GatewayRoute, error) {
	var resource GatewayRoute
	err := ctx.ReadResource("aws-native:appmesh:GatewayRoute", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GatewayRoute resources.
type gatewayRouteState struct {
}

type GatewayRouteState struct {
}

func (GatewayRouteState) ElementType() reflect.Type {
	return reflect.TypeOf((*gatewayRouteState)(nil)).Elem()
}

type gatewayRouteArgs struct {
	GatewayRouteName   *string           `pulumi:"gatewayRouteName"`
	MeshName           string            `pulumi:"meshName"`
	MeshOwner          *string           `pulumi:"meshOwner"`
	Spec               GatewayRouteSpec  `pulumi:"spec"`
	Tags               []GatewayRouteTag `pulumi:"tags"`
	VirtualGatewayName string            `pulumi:"virtualGatewayName"`
}

// The set of arguments for constructing a GatewayRoute resource.
type GatewayRouteArgs struct {
	GatewayRouteName   pulumi.StringPtrInput
	MeshName           pulumi.StringInput
	MeshOwner          pulumi.StringPtrInput
	Spec               GatewayRouteSpecInput
	Tags               GatewayRouteTagArrayInput
	VirtualGatewayName pulumi.StringInput
}

func (GatewayRouteArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*gatewayRouteArgs)(nil)).Elem()
}

type GatewayRouteInput interface {
	pulumi.Input

	ToGatewayRouteOutput() GatewayRouteOutput
	ToGatewayRouteOutputWithContext(ctx context.Context) GatewayRouteOutput
}

func (*GatewayRoute) ElementType() reflect.Type {
	return reflect.TypeOf((**GatewayRoute)(nil)).Elem()
}

func (i *GatewayRoute) ToGatewayRouteOutput() GatewayRouteOutput {
	return i.ToGatewayRouteOutputWithContext(context.Background())
}

func (i *GatewayRoute) ToGatewayRouteOutputWithContext(ctx context.Context) GatewayRouteOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GatewayRouteOutput)
}

func (i *GatewayRoute) ToOutput(ctx context.Context) pulumix.Output[*GatewayRoute] {
	return pulumix.Output[*GatewayRoute]{
		OutputState: i.ToGatewayRouteOutputWithContext(ctx).OutputState,
	}
}

type GatewayRouteOutput struct{ *pulumi.OutputState }

func (GatewayRouteOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GatewayRoute)(nil)).Elem()
}

func (o GatewayRouteOutput) ToGatewayRouteOutput() GatewayRouteOutput {
	return o
}

func (o GatewayRouteOutput) ToGatewayRouteOutputWithContext(ctx context.Context) GatewayRouteOutput {
	return o
}

func (o GatewayRouteOutput) ToOutput(ctx context.Context) pulumix.Output[*GatewayRoute] {
	return pulumix.Output[*GatewayRoute]{
		OutputState: o.OutputState,
	}
}

func (o GatewayRouteOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *GatewayRoute) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o GatewayRouteOutput) GatewayRouteName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *GatewayRoute) pulumi.StringPtrOutput { return v.GatewayRouteName }).(pulumi.StringPtrOutput)
}

func (o GatewayRouteOutput) MeshName() pulumi.StringOutput {
	return o.ApplyT(func(v *GatewayRoute) pulumi.StringOutput { return v.MeshName }).(pulumi.StringOutput)
}

func (o GatewayRouteOutput) MeshOwner() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *GatewayRoute) pulumi.StringPtrOutput { return v.MeshOwner }).(pulumi.StringPtrOutput)
}

func (o GatewayRouteOutput) ResourceOwner() pulumi.StringOutput {
	return o.ApplyT(func(v *GatewayRoute) pulumi.StringOutput { return v.ResourceOwner }).(pulumi.StringOutput)
}

func (o GatewayRouteOutput) Spec() GatewayRouteSpecOutput {
	return o.ApplyT(func(v *GatewayRoute) GatewayRouteSpecOutput { return v.Spec }).(GatewayRouteSpecOutput)
}

func (o GatewayRouteOutput) Tags() GatewayRouteTagArrayOutput {
	return o.ApplyT(func(v *GatewayRoute) GatewayRouteTagArrayOutput { return v.Tags }).(GatewayRouteTagArrayOutput)
}

func (o GatewayRouteOutput) Uid() pulumi.StringOutput {
	return o.ApplyT(func(v *GatewayRoute) pulumi.StringOutput { return v.Uid }).(pulumi.StringOutput)
}

func (o GatewayRouteOutput) VirtualGatewayName() pulumi.StringOutput {
	return o.ApplyT(func(v *GatewayRoute) pulumi.StringOutput { return v.VirtualGatewayName }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GatewayRouteInput)(nil)).Elem(), &GatewayRoute{})
	pulumi.RegisterOutputType(GatewayRouteOutput{})
}
