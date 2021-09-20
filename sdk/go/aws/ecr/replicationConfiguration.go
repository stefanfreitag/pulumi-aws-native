// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ecr

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::ECR::ReplicationConfiguration resource configures the replication destinations for an Amazon Elastic Container Registry (Amazon Private ECR). For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html
type ReplicationConfiguration struct {
	pulumi.CustomResourceState

	// The RegistryId associated with the aws account.
	RegistryId               pulumi.StringOutput                                    `pulumi:"registryId"`
	ReplicationConfiguration ReplicationConfigurationReplicationConfigurationOutput `pulumi:"replicationConfiguration"`
}

// NewReplicationConfiguration registers a new resource with the given unique name, arguments, and options.
func NewReplicationConfiguration(ctx *pulumi.Context,
	name string, args *ReplicationConfigurationArgs, opts ...pulumi.ResourceOption) (*ReplicationConfiguration, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ReplicationConfiguration == nil {
		return nil, errors.New("invalid value for required argument 'ReplicationConfiguration'")
	}
	var resource ReplicationConfiguration
	err := ctx.RegisterResource("aws-native:ecr:ReplicationConfiguration", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetReplicationConfiguration gets an existing ReplicationConfiguration resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetReplicationConfiguration(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ReplicationConfigurationState, opts ...pulumi.ResourceOption) (*ReplicationConfiguration, error) {
	var resource ReplicationConfiguration
	err := ctx.ReadResource("aws-native:ecr:ReplicationConfiguration", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ReplicationConfiguration resources.
type replicationConfigurationState struct {
}

type ReplicationConfigurationState struct {
}

func (ReplicationConfigurationState) ElementType() reflect.Type {
	return reflect.TypeOf((*replicationConfigurationState)(nil)).Elem()
}

type replicationConfigurationArgs struct {
	ReplicationConfiguration ReplicationConfigurationReplicationConfiguration `pulumi:"replicationConfiguration"`
}

// The set of arguments for constructing a ReplicationConfiguration resource.
type ReplicationConfigurationArgs struct {
	ReplicationConfiguration ReplicationConfigurationReplicationConfigurationInput
}

func (ReplicationConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*replicationConfigurationArgs)(nil)).Elem()
}

type ReplicationConfigurationInput interface {
	pulumi.Input

	ToReplicationConfigurationOutput() ReplicationConfigurationOutput
	ToReplicationConfigurationOutputWithContext(ctx context.Context) ReplicationConfigurationOutput
}

func (*ReplicationConfiguration) ElementType() reflect.Type {
	return reflect.TypeOf((*ReplicationConfiguration)(nil))
}

func (i *ReplicationConfiguration) ToReplicationConfigurationOutput() ReplicationConfigurationOutput {
	return i.ToReplicationConfigurationOutputWithContext(context.Background())
}

func (i *ReplicationConfiguration) ToReplicationConfigurationOutputWithContext(ctx context.Context) ReplicationConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ReplicationConfigurationOutput)
}

type ReplicationConfigurationOutput struct{ *pulumi.OutputState }

func (ReplicationConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ReplicationConfiguration)(nil))
}

func (o ReplicationConfigurationOutput) ToReplicationConfigurationOutput() ReplicationConfigurationOutput {
	return o
}

func (o ReplicationConfigurationOutput) ToReplicationConfigurationOutputWithContext(ctx context.Context) ReplicationConfigurationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ReplicationConfigurationOutput{})
}
