// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package elasticache

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::ElastiCache::ReplicationGroup
func LookupReplicationGroup(ctx *pulumi.Context, args *LookupReplicationGroupArgs, opts ...pulumi.InvokeOption) (*LookupReplicationGroupResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupReplicationGroupResult
	err := ctx.Invoke("aws-native:elasticache:getReplicationGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupReplicationGroupArgs struct {
	ReplicationGroupId string `pulumi:"replicationGroupId"`
}

type LookupReplicationGroupResult struct {
	AuthToken                    *string                                           `pulumi:"authToken"`
	AutoMinorVersionUpgrade      *bool                                             `pulumi:"autoMinorVersionUpgrade"`
	AutomaticFailoverEnabled     *bool                                             `pulumi:"automaticFailoverEnabled"`
	CacheNodeType                *string                                           `pulumi:"cacheNodeType"`
	CacheParameterGroupName      *string                                           `pulumi:"cacheParameterGroupName"`
	CacheSecurityGroupNames      []string                                          `pulumi:"cacheSecurityGroupNames"`
	ClusterMode                  *string                                           `pulumi:"clusterMode"`
	ConfigurationEndPointAddress *string                                           `pulumi:"configurationEndPointAddress"`
	ConfigurationEndPointPort    *string                                           `pulumi:"configurationEndPointPort"`
	EngineVersion                *string                                           `pulumi:"engineVersion"`
	IpDiscovery                  *string                                           `pulumi:"ipDiscovery"`
	LogDeliveryConfigurations    []ReplicationGroupLogDeliveryConfigurationRequest `pulumi:"logDeliveryConfigurations"`
	MultiAzEnabled               *bool                                             `pulumi:"multiAzEnabled"`
	NodeGroupConfiguration       []ReplicationGroupNodeGroupConfiguration          `pulumi:"nodeGroupConfiguration"`
	NotificationTopicArn         *string                                           `pulumi:"notificationTopicArn"`
	NumCacheClusters             *int                                              `pulumi:"numCacheClusters"`
	NumNodeGroups                *int                                              `pulumi:"numNodeGroups"`
	PreferredMaintenanceWindow   *string                                           `pulumi:"preferredMaintenanceWindow"`
	PrimaryClusterId             *string                                           `pulumi:"primaryClusterId"`
	PrimaryEndPointAddress       *string                                           `pulumi:"primaryEndPointAddress"`
	PrimaryEndPointPort          *string                                           `pulumi:"primaryEndPointPort"`
	ReadEndPointAddresses        *string                                           `pulumi:"readEndPointAddresses"`
	ReadEndPointAddressesList    []string                                          `pulumi:"readEndPointAddressesList"`
	ReadEndPointPorts            *string                                           `pulumi:"readEndPointPorts"`
	ReadEndPointPortsList        []string                                          `pulumi:"readEndPointPortsList"`
	ReaderEndPointAddress        *string                                           `pulumi:"readerEndPointAddress"`
	ReaderEndPointPort           *string                                           `pulumi:"readerEndPointPort"`
	ReplicationGroupDescription  *string                                           `pulumi:"replicationGroupDescription"`
	SecurityGroupIds             []string                                          `pulumi:"securityGroupIds"`
	SnapshotRetentionLimit       *int                                              `pulumi:"snapshotRetentionLimit"`
	SnapshotWindow               *string                                           `pulumi:"snapshotWindow"`
	SnapshottingClusterId        *string                                           `pulumi:"snapshottingClusterId"`
	Tags                         []ReplicationGroupTag                             `pulumi:"tags"`
	TransitEncryptionEnabled     *bool                                             `pulumi:"transitEncryptionEnabled"`
	TransitEncryptionMode        *string                                           `pulumi:"transitEncryptionMode"`
	UserGroupIds                 []string                                          `pulumi:"userGroupIds"`
}

func LookupReplicationGroupOutput(ctx *pulumi.Context, args LookupReplicationGroupOutputArgs, opts ...pulumi.InvokeOption) LookupReplicationGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupReplicationGroupResult, error) {
			args := v.(LookupReplicationGroupArgs)
			r, err := LookupReplicationGroup(ctx, &args, opts...)
			var s LookupReplicationGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupReplicationGroupResultOutput)
}

type LookupReplicationGroupOutputArgs struct {
	ReplicationGroupId pulumi.StringInput `pulumi:"replicationGroupId"`
}

func (LookupReplicationGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupReplicationGroupArgs)(nil)).Elem()
}

type LookupReplicationGroupResultOutput struct{ *pulumi.OutputState }

func (LookupReplicationGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupReplicationGroupResult)(nil)).Elem()
}

func (o LookupReplicationGroupResultOutput) ToLookupReplicationGroupResultOutput() LookupReplicationGroupResultOutput {
	return o
}

func (o LookupReplicationGroupResultOutput) ToLookupReplicationGroupResultOutputWithContext(ctx context.Context) LookupReplicationGroupResultOutput {
	return o
}

func (o LookupReplicationGroupResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupReplicationGroupResult] {
	return pulumix.Output[LookupReplicationGroupResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupReplicationGroupResultOutput) AuthToken() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.AuthToken }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) AutoMinorVersionUpgrade() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *bool { return v.AutoMinorVersionUpgrade }).(pulumi.BoolPtrOutput)
}

func (o LookupReplicationGroupResultOutput) AutomaticFailoverEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *bool { return v.AutomaticFailoverEnabled }).(pulumi.BoolPtrOutput)
}

func (o LookupReplicationGroupResultOutput) CacheNodeType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.CacheNodeType }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) CacheParameterGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.CacheParameterGroupName }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) CacheSecurityGroupNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) []string { return v.CacheSecurityGroupNames }).(pulumi.StringArrayOutput)
}

func (o LookupReplicationGroupResultOutput) ClusterMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.ClusterMode }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) ConfigurationEndPointAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.ConfigurationEndPointAddress }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) ConfigurationEndPointPort() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.ConfigurationEndPointPort }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) EngineVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.EngineVersion }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) IpDiscovery() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.IpDiscovery }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) LogDeliveryConfigurations() ReplicationGroupLogDeliveryConfigurationRequestArrayOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) []ReplicationGroupLogDeliveryConfigurationRequest {
		return v.LogDeliveryConfigurations
	}).(ReplicationGroupLogDeliveryConfigurationRequestArrayOutput)
}

func (o LookupReplicationGroupResultOutput) MultiAzEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *bool { return v.MultiAzEnabled }).(pulumi.BoolPtrOutput)
}

func (o LookupReplicationGroupResultOutput) NodeGroupConfiguration() ReplicationGroupNodeGroupConfigurationArrayOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) []ReplicationGroupNodeGroupConfiguration {
		return v.NodeGroupConfiguration
	}).(ReplicationGroupNodeGroupConfigurationArrayOutput)
}

func (o LookupReplicationGroupResultOutput) NotificationTopicArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.NotificationTopicArn }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) NumCacheClusters() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *int { return v.NumCacheClusters }).(pulumi.IntPtrOutput)
}

func (o LookupReplicationGroupResultOutput) NumNodeGroups() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *int { return v.NumNodeGroups }).(pulumi.IntPtrOutput)
}

func (o LookupReplicationGroupResultOutput) PreferredMaintenanceWindow() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.PreferredMaintenanceWindow }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) PrimaryClusterId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.PrimaryClusterId }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) PrimaryEndPointAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.PrimaryEndPointAddress }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) PrimaryEndPointPort() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.PrimaryEndPointPort }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) ReadEndPointAddresses() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.ReadEndPointAddresses }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) ReadEndPointAddressesList() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) []string { return v.ReadEndPointAddressesList }).(pulumi.StringArrayOutput)
}

func (o LookupReplicationGroupResultOutput) ReadEndPointPorts() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.ReadEndPointPorts }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) ReadEndPointPortsList() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) []string { return v.ReadEndPointPortsList }).(pulumi.StringArrayOutput)
}

func (o LookupReplicationGroupResultOutput) ReaderEndPointAddress() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.ReaderEndPointAddress }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) ReaderEndPointPort() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.ReaderEndPointPort }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) ReplicationGroupDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.ReplicationGroupDescription }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) SecurityGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) []string { return v.SecurityGroupIds }).(pulumi.StringArrayOutput)
}

func (o LookupReplicationGroupResultOutput) SnapshotRetentionLimit() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *int { return v.SnapshotRetentionLimit }).(pulumi.IntPtrOutput)
}

func (o LookupReplicationGroupResultOutput) SnapshotWindow() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.SnapshotWindow }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) SnapshottingClusterId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.SnapshottingClusterId }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) Tags() ReplicationGroupTagArrayOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) []ReplicationGroupTag { return v.Tags }).(ReplicationGroupTagArrayOutput)
}

func (o LookupReplicationGroupResultOutput) TransitEncryptionEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *bool { return v.TransitEncryptionEnabled }).(pulumi.BoolPtrOutput)
}

func (o LookupReplicationGroupResultOutput) TransitEncryptionMode() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) *string { return v.TransitEncryptionMode }).(pulumi.StringPtrOutput)
}

func (o LookupReplicationGroupResultOutput) UserGroupIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupReplicationGroupResult) []string { return v.UserGroupIds }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupReplicationGroupResultOutput{})
}
