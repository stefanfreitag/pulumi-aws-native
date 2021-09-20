// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cassandra

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::Cassandra::Table
type Table struct {
	pulumi.CustomResourceState

	BillingMode TableBillingModePtrOutput `pulumi:"billingMode"`
	// Clustering key columns of the table
	ClusteringKeyColumns    TableClusteringKeyColumnArrayOutput   `pulumi:"clusteringKeyColumns"`
	EncryptionSpecification TableEncryptionSpecificationPtrOutput `pulumi:"encryptionSpecification"`
	// Name for Cassandra keyspace
	KeyspaceName pulumi.StringOutput `pulumi:"keyspaceName"`
	// Partition key columns of the table
	PartitionKeyColumns TableColumnArrayOutput `pulumi:"partitionKeyColumns"`
	// Indicates whether point in time recovery is enabled (true) or disabled (false) on the table
	PointInTimeRecoveryEnabled pulumi.BoolPtrOutput `pulumi:"pointInTimeRecoveryEnabled"`
	// Non-key columns of the table
	RegularColumns TableColumnArrayOutput `pulumi:"regularColumns"`
	// Name for Cassandra table
	TableName pulumi.StringPtrOutput `pulumi:"tableName"`
	// An array of key-value pairs to apply to this resource
	Tags TableTagArrayOutput `pulumi:"tags"`
}

// NewTable registers a new resource with the given unique name, arguments, and options.
func NewTable(ctx *pulumi.Context,
	name string, args *TableArgs, opts ...pulumi.ResourceOption) (*Table, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.KeyspaceName == nil {
		return nil, errors.New("invalid value for required argument 'KeyspaceName'")
	}
	if args.PartitionKeyColumns == nil {
		return nil, errors.New("invalid value for required argument 'PartitionKeyColumns'")
	}
	var resource Table
	err := ctx.RegisterResource("aws-native:cassandra:Table", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTable gets an existing Table resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTable(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TableState, opts ...pulumi.ResourceOption) (*Table, error) {
	var resource Table
	err := ctx.ReadResource("aws-native:cassandra:Table", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Table resources.
type tableState struct {
}

type TableState struct {
}

func (TableState) ElementType() reflect.Type {
	return reflect.TypeOf((*tableState)(nil)).Elem()
}

type tableArgs struct {
	BillingMode *TableBillingMode `pulumi:"billingMode"`
	// Clustering key columns of the table
	ClusteringKeyColumns    []TableClusteringKeyColumn    `pulumi:"clusteringKeyColumns"`
	EncryptionSpecification *TableEncryptionSpecification `pulumi:"encryptionSpecification"`
	// Name for Cassandra keyspace
	KeyspaceName string `pulumi:"keyspaceName"`
	// Partition key columns of the table
	PartitionKeyColumns []TableColumn `pulumi:"partitionKeyColumns"`
	// Indicates whether point in time recovery is enabled (true) or disabled (false) on the table
	PointInTimeRecoveryEnabled *bool `pulumi:"pointInTimeRecoveryEnabled"`
	// Non-key columns of the table
	RegularColumns []TableColumn `pulumi:"regularColumns"`
	// Name for Cassandra table
	TableName *string `pulumi:"tableName"`
	// An array of key-value pairs to apply to this resource
	Tags []TableTag `pulumi:"tags"`
}

// The set of arguments for constructing a Table resource.
type TableArgs struct {
	BillingMode TableBillingModePtrInput
	// Clustering key columns of the table
	ClusteringKeyColumns    TableClusteringKeyColumnArrayInput
	EncryptionSpecification TableEncryptionSpecificationPtrInput
	// Name for Cassandra keyspace
	KeyspaceName pulumi.StringInput
	// Partition key columns of the table
	PartitionKeyColumns TableColumnArrayInput
	// Indicates whether point in time recovery is enabled (true) or disabled (false) on the table
	PointInTimeRecoveryEnabled pulumi.BoolPtrInput
	// Non-key columns of the table
	RegularColumns TableColumnArrayInput
	// Name for Cassandra table
	TableName pulumi.StringPtrInput
	// An array of key-value pairs to apply to this resource
	Tags TableTagArrayInput
}

func (TableArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tableArgs)(nil)).Elem()
}

type TableInput interface {
	pulumi.Input

	ToTableOutput() TableOutput
	ToTableOutputWithContext(ctx context.Context) TableOutput
}

func (*Table) ElementType() reflect.Type {
	return reflect.TypeOf((*Table)(nil))
}

func (i *Table) ToTableOutput() TableOutput {
	return i.ToTableOutputWithContext(context.Background())
}

func (i *Table) ToTableOutputWithContext(ctx context.Context) TableOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TableOutput)
}

type TableOutput struct{ *pulumi.OutputState }

func (TableOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Table)(nil))
}

func (o TableOutput) ToTableOutput() TableOutput {
	return o
}

func (o TableOutput) ToTableOutputWithContext(ctx context.Context) TableOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(TableOutput{})
}
