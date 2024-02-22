// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::RDS::DBProxyEndpoint.
type DbProxyEndpoint struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) for the DB proxy endpoint.
	DbProxyEndpointArn pulumi.StringOutput `pulumi:"dbProxyEndpointArn"`
	// The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.
	DbProxyEndpointName pulumi.StringOutput `pulumi:"dbProxyEndpointName"`
	// The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
	DbProxyName pulumi.StringOutput `pulumi:"dbProxyName"`
	// The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.
	Endpoint pulumi.StringOutput `pulumi:"endpoint"`
	// A value that indicates whether this endpoint is the default endpoint for the associated DB proxy. Default DB proxy endpoints always have read/write capability. Other endpoints that you associate with the DB proxy can be either read/write or read-only.
	IsDefault pulumi.BoolOutput `pulumi:"isDefault"`
	// An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.
	Tags aws.TagArrayOutput `pulumi:"tags"`
	// A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.
	TargetRole DbProxyEndpointTargetRolePtrOutput `pulumi:"targetRole"`
	// VPC ID to associate with the new DB proxy endpoint.
	VpcId pulumi.StringOutput `pulumi:"vpcId"`
	// VPC security group IDs to associate with the new DB proxy endpoint.
	VpcSecurityGroupIds pulumi.StringArrayOutput `pulumi:"vpcSecurityGroupIds"`
	// VPC subnet IDs to associate with the new DB proxy endpoint.
	VpcSubnetIds pulumi.StringArrayOutput `pulumi:"vpcSubnetIds"`
}

// NewDbProxyEndpoint registers a new resource with the given unique name, arguments, and options.
func NewDbProxyEndpoint(ctx *pulumi.Context,
	name string, args *DbProxyEndpointArgs, opts ...pulumi.ResourceOption) (*DbProxyEndpoint, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DbProxyName == nil {
		return nil, errors.New("invalid value for required argument 'DbProxyName'")
	}
	if args.VpcSubnetIds == nil {
		return nil, errors.New("invalid value for required argument 'VpcSubnetIds'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"dbProxyEndpointName",
		"dbProxyName",
		"vpcSubnetIds[*]",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DbProxyEndpoint
	err := ctx.RegisterResource("aws-native:rds:DbProxyEndpoint", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDbProxyEndpoint gets an existing DbProxyEndpoint resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDbProxyEndpoint(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DbProxyEndpointState, opts ...pulumi.ResourceOption) (*DbProxyEndpoint, error) {
	var resource DbProxyEndpoint
	err := ctx.ReadResource("aws-native:rds:DbProxyEndpoint", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DbProxyEndpoint resources.
type dbProxyEndpointState struct {
}

type DbProxyEndpointState struct {
}

func (DbProxyEndpointState) ElementType() reflect.Type {
	return reflect.TypeOf((*dbProxyEndpointState)(nil)).Elem()
}

type dbProxyEndpointArgs struct {
	// The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.
	DbProxyEndpointName *string `pulumi:"dbProxyEndpointName"`
	// The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
	DbProxyName string `pulumi:"dbProxyName"`
	// An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.
	Tags []aws.Tag `pulumi:"tags"`
	// A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.
	TargetRole *DbProxyEndpointTargetRole `pulumi:"targetRole"`
	// VPC security group IDs to associate with the new DB proxy endpoint.
	VpcSecurityGroupIds []string `pulumi:"vpcSecurityGroupIds"`
	// VPC subnet IDs to associate with the new DB proxy endpoint.
	VpcSubnetIds []string `pulumi:"vpcSubnetIds"`
}

// The set of arguments for constructing a DbProxyEndpoint resource.
type DbProxyEndpointArgs struct {
	// The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.
	DbProxyEndpointName pulumi.StringPtrInput
	// The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
	DbProxyName pulumi.StringInput
	// An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.
	Tags aws.TagArrayInput
	// A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.
	TargetRole DbProxyEndpointTargetRolePtrInput
	// VPC security group IDs to associate with the new DB proxy endpoint.
	VpcSecurityGroupIds pulumi.StringArrayInput
	// VPC subnet IDs to associate with the new DB proxy endpoint.
	VpcSubnetIds pulumi.StringArrayInput
}

func (DbProxyEndpointArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dbProxyEndpointArgs)(nil)).Elem()
}

type DbProxyEndpointInput interface {
	pulumi.Input

	ToDbProxyEndpointOutput() DbProxyEndpointOutput
	ToDbProxyEndpointOutputWithContext(ctx context.Context) DbProxyEndpointOutput
}

func (*DbProxyEndpoint) ElementType() reflect.Type {
	return reflect.TypeOf((**DbProxyEndpoint)(nil)).Elem()
}

func (i *DbProxyEndpoint) ToDbProxyEndpointOutput() DbProxyEndpointOutput {
	return i.ToDbProxyEndpointOutputWithContext(context.Background())
}

func (i *DbProxyEndpoint) ToDbProxyEndpointOutputWithContext(ctx context.Context) DbProxyEndpointOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DbProxyEndpointOutput)
}

type DbProxyEndpointOutput struct{ *pulumi.OutputState }

func (DbProxyEndpointOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DbProxyEndpoint)(nil)).Elem()
}

func (o DbProxyEndpointOutput) ToDbProxyEndpointOutput() DbProxyEndpointOutput {
	return o
}

func (o DbProxyEndpointOutput) ToDbProxyEndpointOutputWithContext(ctx context.Context) DbProxyEndpointOutput {
	return o
}

// The Amazon Resource Name (ARN) for the DB proxy endpoint.
func (o DbProxyEndpointOutput) DbProxyEndpointArn() pulumi.StringOutput {
	return o.ApplyT(func(v *DbProxyEndpoint) pulumi.StringOutput { return v.DbProxyEndpointArn }).(pulumi.StringOutput)
}

// The identifier for the DB proxy endpoint. This name must be unique for all DB proxy endpoints owned by your AWS account in the specified AWS Region.
func (o DbProxyEndpointOutput) DbProxyEndpointName() pulumi.StringOutput {
	return o.ApplyT(func(v *DbProxyEndpoint) pulumi.StringOutput { return v.DbProxyEndpointName }).(pulumi.StringOutput)
}

// The identifier for the proxy. This name must be unique for all proxies owned by your AWS account in the specified AWS Region.
func (o DbProxyEndpointOutput) DbProxyName() pulumi.StringOutput {
	return o.ApplyT(func(v *DbProxyEndpoint) pulumi.StringOutput { return v.DbProxyName }).(pulumi.StringOutput)
}

// The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.
func (o DbProxyEndpointOutput) Endpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *DbProxyEndpoint) pulumi.StringOutput { return v.Endpoint }).(pulumi.StringOutput)
}

// A value that indicates whether this endpoint is the default endpoint for the associated DB proxy. Default DB proxy endpoints always have read/write capability. Other endpoints that you associate with the DB proxy can be either read/write or read-only.
func (o DbProxyEndpointOutput) IsDefault() pulumi.BoolOutput {
	return o.ApplyT(func(v *DbProxyEndpoint) pulumi.BoolOutput { return v.IsDefault }).(pulumi.BoolOutput)
}

// An optional set of key-value pairs to associate arbitrary data of your choosing with the DB proxy endpoint.
func (o DbProxyEndpointOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *DbProxyEndpoint) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

// A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.
func (o DbProxyEndpointOutput) TargetRole() DbProxyEndpointTargetRolePtrOutput {
	return o.ApplyT(func(v *DbProxyEndpoint) DbProxyEndpointTargetRolePtrOutput { return v.TargetRole }).(DbProxyEndpointTargetRolePtrOutput)
}

// VPC ID to associate with the new DB proxy endpoint.
func (o DbProxyEndpointOutput) VpcId() pulumi.StringOutput {
	return o.ApplyT(func(v *DbProxyEndpoint) pulumi.StringOutput { return v.VpcId }).(pulumi.StringOutput)
}

// VPC security group IDs to associate with the new DB proxy endpoint.
func (o DbProxyEndpointOutput) VpcSecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *DbProxyEndpoint) pulumi.StringArrayOutput { return v.VpcSecurityGroupIds }).(pulumi.StringArrayOutput)
}

// VPC subnet IDs to associate with the new DB proxy endpoint.
func (o DbProxyEndpointOutput) VpcSubnetIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *DbProxyEndpoint) pulumi.StringArrayOutput { return v.VpcSubnetIds }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DbProxyEndpointInput)(nil)).Elem(), &DbProxyEndpoint{})
	pulumi.RegisterOutputType(DbProxyEndpointOutput{})
}
