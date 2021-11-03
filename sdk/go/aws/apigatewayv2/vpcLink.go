// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigatewayv2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ApiGatewayV2::VpcLink
//
// Deprecated: VpcLink is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type VpcLink struct {
	pulumi.CustomResourceState

	Name             pulumi.StringOutput      `pulumi:"name"`
	SecurityGroupIds pulumi.StringArrayOutput `pulumi:"securityGroupIds"`
	SubnetIds        pulumi.StringArrayOutput `pulumi:"subnetIds"`
	Tags             pulumi.AnyOutput         `pulumi:"tags"`
}

// NewVpcLink registers a new resource with the given unique name, arguments, and options.
func NewVpcLink(ctx *pulumi.Context,
	name string, args *VpcLinkArgs, opts ...pulumi.ResourceOption) (*VpcLink, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	if args.SubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'SubnetIds'")
	}
	var resource VpcLink
	err := ctx.RegisterResource("aws-native:apigatewayv2:VpcLink", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVpcLink gets an existing VpcLink resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpcLink(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VpcLinkState, opts ...pulumi.ResourceOption) (*VpcLink, error) {
	var resource VpcLink
	err := ctx.ReadResource("aws-native:apigatewayv2:VpcLink", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VpcLink resources.
type vpcLinkState struct {
}

type VpcLinkState struct {
}

func (VpcLinkState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcLinkState)(nil)).Elem()
}

type vpcLinkArgs struct {
	Name             string      `pulumi:"name"`
	SecurityGroupIds []string    `pulumi:"securityGroupIds"`
	SubnetIds        []string    `pulumi:"subnetIds"`
	Tags             interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a VpcLink resource.
type VpcLinkArgs struct {
	Name             pulumi.StringInput
	SecurityGroupIds pulumi.StringArrayInput
	SubnetIds        pulumi.StringArrayInput
	Tags             pulumi.Input
}

func (VpcLinkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcLinkArgs)(nil)).Elem()
}

type VpcLinkInput interface {
	pulumi.Input

	ToVpcLinkOutput() VpcLinkOutput
	ToVpcLinkOutputWithContext(ctx context.Context) VpcLinkOutput
}

func (*VpcLink) ElementType() reflect.Type {
	return reflect.TypeOf((*VpcLink)(nil))
}

func (i *VpcLink) ToVpcLinkOutput() VpcLinkOutput {
	return i.ToVpcLinkOutputWithContext(context.Background())
}

func (i *VpcLink) ToVpcLinkOutputWithContext(ctx context.Context) VpcLinkOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VpcLinkOutput)
}

type VpcLinkOutput struct{ *pulumi.OutputState }

func (VpcLinkOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*VpcLink)(nil))
}

func (o VpcLinkOutput) ToVpcLinkOutput() VpcLinkOutput {
	return o
}

func (o VpcLinkOutput) ToVpcLinkOutputWithContext(ctx context.Context) VpcLinkOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VpcLinkInput)(nil)).Elem(), &VpcLink{})
	pulumi.RegisterOutputType(VpcLinkOutput{})
}
