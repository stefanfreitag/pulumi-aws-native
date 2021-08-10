// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html
type GlobalCluster struct {
	pulumi.CustomResourceState

	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-deletionprotection
	DeletionProtection pulumi.BoolPtrOutput `pulumi:"deletionProtection"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engine
	Engine pulumi.StringPtrOutput `pulumi:"engine"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engineversion
	EngineVersion pulumi.StringPtrOutput `pulumi:"engineVersion"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-globalclusteridentifier
	GlobalClusterIdentifier pulumi.StringPtrOutput `pulumi:"globalClusterIdentifier"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-sourcedbclusteridentifier
	SourceDBClusterIdentifier pulumi.StringPtrOutput `pulumi:"sourceDBClusterIdentifier"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-storageencrypted
	StorageEncrypted pulumi.BoolPtrOutput `pulumi:"storageEncrypted"`
}

// NewGlobalCluster registers a new resource with the given unique name, arguments, and options.
func NewGlobalCluster(ctx *pulumi.Context,
	name string, args *GlobalClusterArgs, opts ...pulumi.ResourceOption) (*GlobalCluster, error) {
	if args == nil {
		args = &GlobalClusterArgs{}
	}

	var resource GlobalCluster
	err := ctx.RegisterResource("aws-native:RDS:GlobalCluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGlobalCluster gets an existing GlobalCluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGlobalCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GlobalClusterState, opts ...pulumi.ResourceOption) (*GlobalCluster, error) {
	var resource GlobalCluster
	err := ctx.ReadResource("aws-native:RDS:GlobalCluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GlobalCluster resources.
type globalClusterState struct {
}

type GlobalClusterState struct {
}

func (GlobalClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*globalClusterState)(nil)).Elem()
}

type globalClusterArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-deletionprotection
	DeletionProtection *bool `pulumi:"deletionProtection"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engine
	Engine *string `pulumi:"engine"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engineversion
	EngineVersion *string `pulumi:"engineVersion"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-globalclusteridentifier
	GlobalClusterIdentifier *string `pulumi:"globalClusterIdentifier"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-sourcedbclusteridentifier
	SourceDBClusterIdentifier *string `pulumi:"sourceDBClusterIdentifier"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-storageencrypted
	StorageEncrypted *bool `pulumi:"storageEncrypted"`
}

// The set of arguments for constructing a GlobalCluster resource.
type GlobalClusterArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-deletionprotection
	DeletionProtection pulumi.BoolPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engine
	Engine pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-engineversion
	EngineVersion pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-globalclusteridentifier
	GlobalClusterIdentifier pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-sourcedbclusteridentifier
	SourceDBClusterIdentifier pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#cfn-rds-globalcluster-storageencrypted
	StorageEncrypted pulumi.BoolPtrInput
}

func (GlobalClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*globalClusterArgs)(nil)).Elem()
}

type GlobalClusterInput interface {
	pulumi.Input

	ToGlobalClusterOutput() GlobalClusterOutput
	ToGlobalClusterOutputWithContext(ctx context.Context) GlobalClusterOutput
}

func (*GlobalCluster) ElementType() reflect.Type {
	return reflect.TypeOf((*GlobalCluster)(nil))
}

func (i *GlobalCluster) ToGlobalClusterOutput() GlobalClusterOutput {
	return i.ToGlobalClusterOutputWithContext(context.Background())
}

func (i *GlobalCluster) ToGlobalClusterOutputWithContext(ctx context.Context) GlobalClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GlobalClusterOutput)
}

type GlobalClusterOutput struct{ *pulumi.OutputState }

func (GlobalClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GlobalCluster)(nil))
}

func (o GlobalClusterOutput) ToGlobalClusterOutput() GlobalClusterOutput {
	return o
}

func (o GlobalClusterOutput) ToGlobalClusterOutputWithContext(ctx context.Context) GlobalClusterOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(GlobalClusterOutput{})
}
