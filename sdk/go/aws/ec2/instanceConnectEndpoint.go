// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::EC2::InstanceConnectEndpoint
type InstanceConnectEndpoint struct {
	pulumi.CustomResourceState

	// The client token of the instance connect endpoint.
	ClientToken pulumi.StringPtrOutput `pulumi:"clientToken"`
	// If true, the address of the instance connect endpoint client is preserved when connecting to the end resource
	PreserveClientIp pulumi.BoolPtrOutput `pulumi:"preserveClientIp"`
	// The security group IDs of the instance connect endpoint.
	SecurityGroupIds pulumi.StringArrayOutput `pulumi:"securityGroupIds"`
	// The subnet id of the instance connect endpoint
	SubnetId pulumi.StringOutput `pulumi:"subnetId"`
	// The tags of the instance connect endpoint.
	Tags InstanceConnectEndpointTagArrayOutput `pulumi:"tags"`
}

// NewInstanceConnectEndpoint registers a new resource with the given unique name, arguments, and options.
func NewInstanceConnectEndpoint(ctx *pulumi.Context,
	name string, args *InstanceConnectEndpointArgs, opts ...pulumi.ResourceOption) (*InstanceConnectEndpoint, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.SubnetId == nil {
		return nil, errors.New("invalid value for required argument 'SubnetId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"clientToken",
		"preserveClientIp",
		"securityGroupIds[*]",
		"subnetId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource InstanceConnectEndpoint
	err := ctx.RegisterResource("aws-native:ec2:InstanceConnectEndpoint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstanceConnectEndpoint gets an existing InstanceConnectEndpoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstanceConnectEndpoint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceConnectEndpointState, opts ...pulumi.ResourceOption) (*InstanceConnectEndpoint, error) {
	var resource InstanceConnectEndpoint
	err := ctx.ReadResource("aws-native:ec2:InstanceConnectEndpoint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering InstanceConnectEndpoint resources.
type instanceConnectEndpointState struct {
}

type InstanceConnectEndpointState struct {
}

func (InstanceConnectEndpointState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceConnectEndpointState)(nil)).Elem()
}

type instanceConnectEndpointArgs struct {
	// The client token of the instance connect endpoint.
	ClientToken *string `pulumi:"clientToken"`
	// If true, the address of the instance connect endpoint client is preserved when connecting to the end resource
	PreserveClientIp *bool `pulumi:"preserveClientIp"`
	// The security group IDs of the instance connect endpoint.
	SecurityGroupIds []string `pulumi:"securityGroupIds"`
	// The subnet id of the instance connect endpoint
	SubnetId string `pulumi:"subnetId"`
	// The tags of the instance connect endpoint.
	Tags []InstanceConnectEndpointTag `pulumi:"tags"`
}

// The set of arguments for constructing a InstanceConnectEndpoint resource.
type InstanceConnectEndpointArgs struct {
	// The client token of the instance connect endpoint.
	ClientToken pulumi.StringPtrInput
	// If true, the address of the instance connect endpoint client is preserved when connecting to the end resource
	PreserveClientIp pulumi.BoolPtrInput
	// The security group IDs of the instance connect endpoint.
	SecurityGroupIds pulumi.StringArrayInput
	// The subnet id of the instance connect endpoint
	SubnetId pulumi.StringInput
	// The tags of the instance connect endpoint.
	Tags InstanceConnectEndpointTagArrayInput
}

func (InstanceConnectEndpointArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceConnectEndpointArgs)(nil)).Elem()
}

type InstanceConnectEndpointInput interface {
	pulumi.Input

	ToInstanceConnectEndpointOutput() InstanceConnectEndpointOutput
	ToInstanceConnectEndpointOutputWithContext(ctx context.Context) InstanceConnectEndpointOutput
}

func (*InstanceConnectEndpoint) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceConnectEndpoint)(nil)).Elem()
}

func (i *InstanceConnectEndpoint) ToInstanceConnectEndpointOutput() InstanceConnectEndpointOutput {
	return i.ToInstanceConnectEndpointOutputWithContext(context.Background())
}

func (i *InstanceConnectEndpoint) ToInstanceConnectEndpointOutputWithContext(ctx context.Context) InstanceConnectEndpointOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceConnectEndpointOutput)
}

type InstanceConnectEndpointOutput struct{ *pulumi.OutputState }

func (InstanceConnectEndpointOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**InstanceConnectEndpoint)(nil)).Elem()
}

func (o InstanceConnectEndpointOutput) ToInstanceConnectEndpointOutput() InstanceConnectEndpointOutput {
	return o
}

func (o InstanceConnectEndpointOutput) ToInstanceConnectEndpointOutputWithContext(ctx context.Context) InstanceConnectEndpointOutput {
	return o
}

// The client token of the instance connect endpoint.
func (o InstanceConnectEndpointOutput) ClientToken() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *InstanceConnectEndpoint) pulumi.StringPtrOutput { return v.ClientToken }).(pulumi.StringPtrOutput)
}

// If true, the address of the instance connect endpoint client is preserved when connecting to the end resource
func (o InstanceConnectEndpointOutput) PreserveClientIp() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *InstanceConnectEndpoint) pulumi.BoolPtrOutput { return v.PreserveClientIp }).(pulumi.BoolPtrOutput)
}

// The security group IDs of the instance connect endpoint.
func (o InstanceConnectEndpointOutput) SecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *InstanceConnectEndpoint) pulumi.StringArrayOutput { return v.SecurityGroupIds }).(pulumi.StringArrayOutput)
}

// The subnet id of the instance connect endpoint
func (o InstanceConnectEndpointOutput) SubnetId() pulumi.StringOutput {
	return o.ApplyT(func(v *InstanceConnectEndpoint) pulumi.StringOutput { return v.SubnetId }).(pulumi.StringOutput)
}

// The tags of the instance connect endpoint.
func (o InstanceConnectEndpointOutput) Tags() InstanceConnectEndpointTagArrayOutput {
	return o.ApplyT(func(v *InstanceConnectEndpoint) InstanceConnectEndpointTagArrayOutput { return v.Tags }).(InstanceConnectEndpointTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceConnectEndpointInput)(nil)).Elem(), &InstanceConnectEndpoint{})
	pulumi.RegisterOutputType(InstanceConnectEndpointOutput{})
}
