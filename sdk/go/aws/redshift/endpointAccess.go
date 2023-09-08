// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package redshift

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for a Redshift-managed VPC endpoint.
type EndpointAccess struct {
	pulumi.CustomResourceState

	// The DNS address of the endpoint.
	Address pulumi.StringOutput `pulumi:"address"`
	// A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account
	ClusterIdentifier pulumi.StringOutput `pulumi:"clusterIdentifier"`
	// The time (UTC) that the endpoint was created.
	EndpointCreateTime pulumi.StringOutput `pulumi:"endpointCreateTime"`
	// The name of the endpoint.
	EndpointName pulumi.StringOutput `pulumi:"endpointName"`
	// The status of the endpoint.
	EndpointStatus pulumi.StringOutput `pulumi:"endpointStatus"`
	// The port number on which the cluster accepts incoming connections.
	Port pulumi.IntOutput `pulumi:"port"`
	// The AWS account ID of the owner of the cluster.
	ResourceOwner pulumi.StringPtrOutput `pulumi:"resourceOwner"`
	// The subnet group name where Amazon Redshift chooses to deploy the endpoint.
	SubnetGroupName pulumi.StringOutput `pulumi:"subnetGroupName"`
	// The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.
	VpcEndpoint VpcEndpointPropertiesOutput `pulumi:"vpcEndpoint"`
	// A list of vpc security group ids to apply to the created endpoint access.
	VpcSecurityGroupIds pulumi.StringArrayOutput `pulumi:"vpcSecurityGroupIds"`
	// A list of Virtual Private Cloud (VPC) security groups to be associated with the endpoint.
	VpcSecurityGroups EndpointAccessVpcSecurityGroupArrayOutput `pulumi:"vpcSecurityGroups"`
}

// NewEndpointAccess registers a new resource with the given unique name, arguments, and options.
func NewEndpointAccess(ctx *pulumi.Context,
	name string, args *EndpointAccessArgs, opts ...pulumi.ResourceOption) (*EndpointAccess, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterIdentifier == nil {
		return nil, errors.New("invalid value for required argument 'ClusterIdentifier'")
	}
	if args.EndpointName == nil {
		return nil, errors.New("invalid value for required argument 'EndpointName'")
	}
	if args.SubnetGroupName == nil {
		return nil, errors.New("invalid value for required argument 'SubnetGroupName'")
	}
	if args.VpcSecurityGroupIds == nil {
		return nil, errors.New("invalid value for required argument 'VpcSecurityGroupIds'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"clusterIdentifier",
		"endpointName",
		"resourceOwner",
		"subnetGroupName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource EndpointAccess
	err := ctx.RegisterResource("aws-native:redshift:EndpointAccess", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEndpointAccess gets an existing EndpointAccess resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEndpointAccess(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EndpointAccessState, opts ...pulumi.ResourceOption) (*EndpointAccess, error) {
	var resource EndpointAccess
	err := ctx.ReadResource("aws-native:redshift:EndpointAccess", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EndpointAccess resources.
type endpointAccessState struct {
}

type EndpointAccessState struct {
}

func (EndpointAccessState) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointAccessState)(nil)).Elem()
}

type endpointAccessArgs struct {
	// A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account
	ClusterIdentifier string `pulumi:"clusterIdentifier"`
	// The name of the endpoint.
	EndpointName string `pulumi:"endpointName"`
	// The AWS account ID of the owner of the cluster.
	ResourceOwner *string `pulumi:"resourceOwner"`
	// The subnet group name where Amazon Redshift chooses to deploy the endpoint.
	SubnetGroupName string `pulumi:"subnetGroupName"`
	// A list of vpc security group ids to apply to the created endpoint access.
	VpcSecurityGroupIds []string `pulumi:"vpcSecurityGroupIds"`
}

// The set of arguments for constructing a EndpointAccess resource.
type EndpointAccessArgs struct {
	// A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account
	ClusterIdentifier pulumi.StringInput
	// The name of the endpoint.
	EndpointName pulumi.StringInput
	// The AWS account ID of the owner of the cluster.
	ResourceOwner pulumi.StringPtrInput
	// The subnet group name where Amazon Redshift chooses to deploy the endpoint.
	SubnetGroupName pulumi.StringInput
	// A list of vpc security group ids to apply to the created endpoint access.
	VpcSecurityGroupIds pulumi.StringArrayInput
}

func (EndpointAccessArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointAccessArgs)(nil)).Elem()
}

type EndpointAccessInput interface {
	pulumi.Input

	ToEndpointAccessOutput() EndpointAccessOutput
	ToEndpointAccessOutputWithContext(ctx context.Context) EndpointAccessOutput
}

func (*EndpointAccess) ElementType() reflect.Type {
	return reflect.TypeOf((**EndpointAccess)(nil)).Elem()
}

func (i *EndpointAccess) ToEndpointAccessOutput() EndpointAccessOutput {
	return i.ToEndpointAccessOutputWithContext(context.Background())
}

func (i *EndpointAccess) ToEndpointAccessOutputWithContext(ctx context.Context) EndpointAccessOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointAccessOutput)
}

func (i *EndpointAccess) ToOutput(ctx context.Context) pulumix.Output[*EndpointAccess] {
	return pulumix.Output[*EndpointAccess]{
		OutputState: i.ToEndpointAccessOutputWithContext(ctx).OutputState,
	}
}

type EndpointAccessOutput struct{ *pulumi.OutputState }

func (EndpointAccessOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EndpointAccess)(nil)).Elem()
}

func (o EndpointAccessOutput) ToEndpointAccessOutput() EndpointAccessOutput {
	return o
}

func (o EndpointAccessOutput) ToEndpointAccessOutputWithContext(ctx context.Context) EndpointAccessOutput {
	return o
}

func (o EndpointAccessOutput) ToOutput(ctx context.Context) pulumix.Output[*EndpointAccess] {
	return pulumix.Output[*EndpointAccess]{
		OutputState: o.OutputState,
	}
}

// The DNS address of the endpoint.
func (o EndpointAccessOutput) Address() pulumi.StringOutput {
	return o.ApplyT(func(v *EndpointAccess) pulumi.StringOutput { return v.Address }).(pulumi.StringOutput)
}

// A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account
func (o EndpointAccessOutput) ClusterIdentifier() pulumi.StringOutput {
	return o.ApplyT(func(v *EndpointAccess) pulumi.StringOutput { return v.ClusterIdentifier }).(pulumi.StringOutput)
}

// The time (UTC) that the endpoint was created.
func (o EndpointAccessOutput) EndpointCreateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *EndpointAccess) pulumi.StringOutput { return v.EndpointCreateTime }).(pulumi.StringOutput)
}

// The name of the endpoint.
func (o EndpointAccessOutput) EndpointName() pulumi.StringOutput {
	return o.ApplyT(func(v *EndpointAccess) pulumi.StringOutput { return v.EndpointName }).(pulumi.StringOutput)
}

// The status of the endpoint.
func (o EndpointAccessOutput) EndpointStatus() pulumi.StringOutput {
	return o.ApplyT(func(v *EndpointAccess) pulumi.StringOutput { return v.EndpointStatus }).(pulumi.StringOutput)
}

// The port number on which the cluster accepts incoming connections.
func (o EndpointAccessOutput) Port() pulumi.IntOutput {
	return o.ApplyT(func(v *EndpointAccess) pulumi.IntOutput { return v.Port }).(pulumi.IntOutput)
}

// The AWS account ID of the owner of the cluster.
func (o EndpointAccessOutput) ResourceOwner() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *EndpointAccess) pulumi.StringPtrOutput { return v.ResourceOwner }).(pulumi.StringPtrOutput)
}

// The subnet group name where Amazon Redshift chooses to deploy the endpoint.
func (o EndpointAccessOutput) SubnetGroupName() pulumi.StringOutput {
	return o.ApplyT(func(v *EndpointAccess) pulumi.StringOutput { return v.SubnetGroupName }).(pulumi.StringOutput)
}

// The connection endpoint for connecting to an Amazon Redshift cluster through the proxy.
func (o EndpointAccessOutput) VpcEndpoint() VpcEndpointPropertiesOutput {
	return o.ApplyT(func(v *EndpointAccess) VpcEndpointPropertiesOutput { return v.VpcEndpoint }).(VpcEndpointPropertiesOutput)
}

// A list of vpc security group ids to apply to the created endpoint access.
func (o EndpointAccessOutput) VpcSecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *EndpointAccess) pulumi.StringArrayOutput { return v.VpcSecurityGroupIds }).(pulumi.StringArrayOutput)
}

// A list of Virtual Private Cloud (VPC) security groups to be associated with the endpoint.
func (o EndpointAccessOutput) VpcSecurityGroups() EndpointAccessVpcSecurityGroupArrayOutput {
	return o.ApplyT(func(v *EndpointAccess) EndpointAccessVpcSecurityGroupArrayOutput { return v.VpcSecurityGroups }).(EndpointAccessVpcSecurityGroupArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*EndpointAccessInput)(nil)).Elem(), &EndpointAccess{})
	pulumi.RegisterOutputType(EndpointAccessOutput{})
}
