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

// Resource Type definition for AWS::EC2::VPCEndpointServicePermissions
type VpcEndpointServicePermissions struct {
	pulumi.CustomResourceState

	AllowedPrincipals pulumi.StringArrayOutput `pulumi:"allowedPrincipals"`
	ServiceId         pulumi.StringOutput      `pulumi:"serviceId"`
}

// NewVpcEndpointServicePermissions registers a new resource with the given unique name, arguments, and options.
func NewVpcEndpointServicePermissions(ctx *pulumi.Context,
	name string, args *VpcEndpointServicePermissionsArgs, opts ...pulumi.ResourceOption) (*VpcEndpointServicePermissions, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ServiceId == nil {
		return nil, errors.New("invalid value for required argument 'ServiceId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"serviceId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource VpcEndpointServicePermissions
	err := ctx.RegisterResource("aws-native:ec2:VpcEndpointServicePermissions", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVpcEndpointServicePermissions gets an existing VpcEndpointServicePermissions resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpcEndpointServicePermissions(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VpcEndpointServicePermissionsState, opts ...pulumi.ResourceOption) (*VpcEndpointServicePermissions, error) {
	var resource VpcEndpointServicePermissions
	err := ctx.ReadResource("aws-native:ec2:VpcEndpointServicePermissions", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VpcEndpointServicePermissions resources.
type vpcEndpointServicePermissionsState struct {
}

type VpcEndpointServicePermissionsState struct {
}

func (VpcEndpointServicePermissionsState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcEndpointServicePermissionsState)(nil)).Elem()
}

type vpcEndpointServicePermissionsArgs struct {
	AllowedPrincipals []string `pulumi:"allowedPrincipals"`
	ServiceId         string   `pulumi:"serviceId"`
}

// The set of arguments for constructing a VpcEndpointServicePermissions resource.
type VpcEndpointServicePermissionsArgs struct {
	AllowedPrincipals pulumi.StringArrayInput
	ServiceId         pulumi.StringInput
}

func (VpcEndpointServicePermissionsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcEndpointServicePermissionsArgs)(nil)).Elem()
}

type VpcEndpointServicePermissionsInput interface {
	pulumi.Input

	ToVpcEndpointServicePermissionsOutput() VpcEndpointServicePermissionsOutput
	ToVpcEndpointServicePermissionsOutputWithContext(ctx context.Context) VpcEndpointServicePermissionsOutput
}

func (*VpcEndpointServicePermissions) ElementType() reflect.Type {
	return reflect.TypeOf((**VpcEndpointServicePermissions)(nil)).Elem()
}

func (i *VpcEndpointServicePermissions) ToVpcEndpointServicePermissionsOutput() VpcEndpointServicePermissionsOutput {
	return i.ToVpcEndpointServicePermissionsOutputWithContext(context.Background())
}

func (i *VpcEndpointServicePermissions) ToVpcEndpointServicePermissionsOutputWithContext(ctx context.Context) VpcEndpointServicePermissionsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VpcEndpointServicePermissionsOutput)
}

func (i *VpcEndpointServicePermissions) ToOutput(ctx context.Context) pulumix.Output[*VpcEndpointServicePermissions] {
	return pulumix.Output[*VpcEndpointServicePermissions]{
		OutputState: i.ToVpcEndpointServicePermissionsOutputWithContext(ctx).OutputState,
	}
}

type VpcEndpointServicePermissionsOutput struct{ *pulumi.OutputState }

func (VpcEndpointServicePermissionsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VpcEndpointServicePermissions)(nil)).Elem()
}

func (o VpcEndpointServicePermissionsOutput) ToVpcEndpointServicePermissionsOutput() VpcEndpointServicePermissionsOutput {
	return o
}

func (o VpcEndpointServicePermissionsOutput) ToVpcEndpointServicePermissionsOutputWithContext(ctx context.Context) VpcEndpointServicePermissionsOutput {
	return o
}

func (o VpcEndpointServicePermissionsOutput) ToOutput(ctx context.Context) pulumix.Output[*VpcEndpointServicePermissions] {
	return pulumix.Output[*VpcEndpointServicePermissions]{
		OutputState: o.OutputState,
	}
}

func (o VpcEndpointServicePermissionsOutput) AllowedPrincipals() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *VpcEndpointServicePermissions) pulumi.StringArrayOutput { return v.AllowedPrincipals }).(pulumi.StringArrayOutput)
}

func (o VpcEndpointServicePermissionsOutput) ServiceId() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcEndpointServicePermissions) pulumi.StringOutput { return v.ServiceId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VpcEndpointServicePermissionsInput)(nil)).Elem(), &VpcEndpointServicePermissions{})
	pulumi.RegisterOutputType(VpcEndpointServicePermissionsOutput{})
}
