// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package neptune

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Neptune::DBCluster
//
// Deprecated: DBCluster is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type DBCluster struct {
	pulumi.CustomResourceState

	AssociatedRoles             DBClusterDBClusterRoleArrayOutput `pulumi:"associatedRoles"`
	AvailabilityZones           pulumi.StringArrayOutput          `pulumi:"availabilityZones"`
	BackupRetentionPeriod       pulumi.IntPtrOutput               `pulumi:"backupRetentionPeriod"`
	ClusterResourceId           pulumi.StringOutput               `pulumi:"clusterResourceId"`
	DBClusterIdentifier         pulumi.StringPtrOutput            `pulumi:"dBClusterIdentifier"`
	DBClusterParameterGroupName pulumi.StringPtrOutput            `pulumi:"dBClusterParameterGroupName"`
	DBSubnetGroupName           pulumi.StringPtrOutput            `pulumi:"dBSubnetGroupName"`
	DeletionProtection          pulumi.BoolPtrOutput              `pulumi:"deletionProtection"`
	EnableCloudwatchLogsExports pulumi.StringArrayOutput          `pulumi:"enableCloudwatchLogsExports"`
	Endpoint                    pulumi.StringOutput               `pulumi:"endpoint"`
	EngineVersion               pulumi.StringPtrOutput            `pulumi:"engineVersion"`
	IamAuthEnabled              pulumi.BoolPtrOutput              `pulumi:"iamAuthEnabled"`
	KmsKeyId                    pulumi.StringPtrOutput            `pulumi:"kmsKeyId"`
	Port                        pulumi.IntPtrOutput               `pulumi:"port"`
	PreferredBackupWindow       pulumi.StringPtrOutput            `pulumi:"preferredBackupWindow"`
	PreferredMaintenanceWindow  pulumi.StringPtrOutput            `pulumi:"preferredMaintenanceWindow"`
	ReadEndpoint                pulumi.StringOutput               `pulumi:"readEndpoint"`
	RestoreToTime               pulumi.StringPtrOutput            `pulumi:"restoreToTime"`
	RestoreType                 pulumi.StringPtrOutput            `pulumi:"restoreType"`
	SnapshotIdentifier          pulumi.StringPtrOutput            `pulumi:"snapshotIdentifier"`
	SourceDBClusterIdentifier   pulumi.StringPtrOutput            `pulumi:"sourceDBClusterIdentifier"`
	StorageEncrypted            pulumi.BoolPtrOutput              `pulumi:"storageEncrypted"`
	Tags                        DBClusterTagArrayOutput           `pulumi:"tags"`
	UseLatestRestorableTime     pulumi.BoolPtrOutput              `pulumi:"useLatestRestorableTime"`
	VpcSecurityGroupIds         pulumi.StringArrayOutput          `pulumi:"vpcSecurityGroupIds"`
}

// NewDBCluster registers a new resource with the given unique name, arguments, and options.
func NewDBCluster(ctx *pulumi.Context,
	name string, args *DBClusterArgs, opts ...pulumi.ResourceOption) (*DBCluster, error) {
	if args == nil {
		args = &DBClusterArgs{}
	}

	var resource DBCluster
	err := ctx.RegisterResource("aws-native:neptune:DBCluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDBCluster gets an existing DBCluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDBCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DBClusterState, opts ...pulumi.ResourceOption) (*DBCluster, error) {
	var resource DBCluster
	err := ctx.ReadResource("aws-native:neptune:DBCluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DBCluster resources.
type dbclusterState struct {
}

type DBClusterState struct {
}

func (DBClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*dbclusterState)(nil)).Elem()
}

type dbclusterArgs struct {
	AssociatedRoles             []DBClusterDBClusterRole `pulumi:"associatedRoles"`
	AvailabilityZones           []string                 `pulumi:"availabilityZones"`
	BackupRetentionPeriod       *int                     `pulumi:"backupRetentionPeriod"`
	DBClusterIdentifier         *string                  `pulumi:"dBClusterIdentifier"`
	DBClusterParameterGroupName *string                  `pulumi:"dBClusterParameterGroupName"`
	DBSubnetGroupName           *string                  `pulumi:"dBSubnetGroupName"`
	DeletionProtection          *bool                    `pulumi:"deletionProtection"`
	EnableCloudwatchLogsExports []string                 `pulumi:"enableCloudwatchLogsExports"`
	EngineVersion               *string                  `pulumi:"engineVersion"`
	IamAuthEnabled              *bool                    `pulumi:"iamAuthEnabled"`
	KmsKeyId                    *string                  `pulumi:"kmsKeyId"`
	Port                        *int                     `pulumi:"port"`
	PreferredBackupWindow       *string                  `pulumi:"preferredBackupWindow"`
	PreferredMaintenanceWindow  *string                  `pulumi:"preferredMaintenanceWindow"`
	RestoreToTime               *string                  `pulumi:"restoreToTime"`
	RestoreType                 *string                  `pulumi:"restoreType"`
	SnapshotIdentifier          *string                  `pulumi:"snapshotIdentifier"`
	SourceDBClusterIdentifier   *string                  `pulumi:"sourceDBClusterIdentifier"`
	StorageEncrypted            *bool                    `pulumi:"storageEncrypted"`
	Tags                        []DBClusterTag           `pulumi:"tags"`
	UseLatestRestorableTime     *bool                    `pulumi:"useLatestRestorableTime"`
	VpcSecurityGroupIds         []string                 `pulumi:"vpcSecurityGroupIds"`
}

// The set of arguments for constructing a DBCluster resource.
type DBClusterArgs struct {
	AssociatedRoles             DBClusterDBClusterRoleArrayInput
	AvailabilityZones           pulumi.StringArrayInput
	BackupRetentionPeriod       pulumi.IntPtrInput
	DBClusterIdentifier         pulumi.StringPtrInput
	DBClusterParameterGroupName pulumi.StringPtrInput
	DBSubnetGroupName           pulumi.StringPtrInput
	DeletionProtection          pulumi.BoolPtrInput
	EnableCloudwatchLogsExports pulumi.StringArrayInput
	EngineVersion               pulumi.StringPtrInput
	IamAuthEnabled              pulumi.BoolPtrInput
	KmsKeyId                    pulumi.StringPtrInput
	Port                        pulumi.IntPtrInput
	PreferredBackupWindow       pulumi.StringPtrInput
	PreferredMaintenanceWindow  pulumi.StringPtrInput
	RestoreToTime               pulumi.StringPtrInput
	RestoreType                 pulumi.StringPtrInput
	SnapshotIdentifier          pulumi.StringPtrInput
	SourceDBClusterIdentifier   pulumi.StringPtrInput
	StorageEncrypted            pulumi.BoolPtrInput
	Tags                        DBClusterTagArrayInput
	UseLatestRestorableTime     pulumi.BoolPtrInput
	VpcSecurityGroupIds         pulumi.StringArrayInput
}

func (DBClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dbclusterArgs)(nil)).Elem()
}

type DBClusterInput interface {
	pulumi.Input

	ToDBClusterOutput() DBClusterOutput
	ToDBClusterOutputWithContext(ctx context.Context) DBClusterOutput
}

func (*DBCluster) ElementType() reflect.Type {
	return reflect.TypeOf((*DBCluster)(nil))
}

func (i *DBCluster) ToDBClusterOutput() DBClusterOutput {
	return i.ToDBClusterOutputWithContext(context.Background())
}

func (i *DBCluster) ToDBClusterOutputWithContext(ctx context.Context) DBClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DBClusterOutput)
}

type DBClusterOutput struct{ *pulumi.OutputState }

func (DBClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DBCluster)(nil))
}

func (o DBClusterOutput) ToDBClusterOutput() DBClusterOutput {
	return o
}

func (o DBClusterOutput) ToDBClusterOutputWithContext(ctx context.Context) DBClusterOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DBClusterOutput{})
}
