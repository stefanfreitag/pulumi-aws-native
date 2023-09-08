// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ecs

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Create an Elastic Container Service (ECS) cluster.
type Cluster struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the Amazon ECS cluster, such as arn:aws:ecs:us-east-2:123456789012:cluster/MyECSCluster.
	Arn               pulumi.StringOutput      `pulumi:"arn"`
	CapacityProviders pulumi.StringArrayOutput `pulumi:"capacityProviders"`
	// A user-generated string that you use to identify your cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID for the name.
	ClusterName                     pulumi.StringPtrOutput                         `pulumi:"clusterName"`
	ClusterSettings                 ClusterSettingsArrayOutput                     `pulumi:"clusterSettings"`
	Configuration                   ClusterConfigurationPtrOutput                  `pulumi:"configuration"`
	DefaultCapacityProviderStrategy ClusterCapacityProviderStrategyItemArrayOutput `pulumi:"defaultCapacityProviderStrategy"`
	ServiceConnectDefaults          ClusterServiceConnectDefaultsPtrOutput         `pulumi:"serviceConnectDefaults"`
	Tags                            ClusterTagArrayOutput                          `pulumi:"tags"`
}

// NewCluster registers a new resource with the given unique name, arguments, and options.
func NewCluster(ctx *pulumi.Context,
	name string, args *ClusterArgs, opts ...pulumi.ResourceOption) (*Cluster, error) {
	if args == nil {
		args = &ClusterArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"clusterName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Cluster
	err := ctx.RegisterResource("aws-native:ecs:Cluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCluster gets an existing Cluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ClusterState, opts ...pulumi.ResourceOption) (*Cluster, error) {
	var resource Cluster
	err := ctx.ReadResource("aws-native:ecs:Cluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Cluster resources.
type clusterState struct {
}

type ClusterState struct {
}

func (ClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterState)(nil)).Elem()
}

type clusterArgs struct {
	CapacityProviders []string `pulumi:"capacityProviders"`
	// A user-generated string that you use to identify your cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID for the name.
	ClusterName                     *string                               `pulumi:"clusterName"`
	ClusterSettings                 []ClusterSettings                     `pulumi:"clusterSettings"`
	Configuration                   *ClusterConfiguration                 `pulumi:"configuration"`
	DefaultCapacityProviderStrategy []ClusterCapacityProviderStrategyItem `pulumi:"defaultCapacityProviderStrategy"`
	ServiceConnectDefaults          *ClusterServiceConnectDefaults        `pulumi:"serviceConnectDefaults"`
	Tags                            []ClusterTag                          `pulumi:"tags"`
}

// The set of arguments for constructing a Cluster resource.
type ClusterArgs struct {
	CapacityProviders pulumi.StringArrayInput
	// A user-generated string that you use to identify your cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID for the name.
	ClusterName                     pulumi.StringPtrInput
	ClusterSettings                 ClusterSettingsArrayInput
	Configuration                   ClusterConfigurationPtrInput
	DefaultCapacityProviderStrategy ClusterCapacityProviderStrategyItemArrayInput
	ServiceConnectDefaults          ClusterServiceConnectDefaultsPtrInput
	Tags                            ClusterTagArrayInput
}

func (ClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterArgs)(nil)).Elem()
}

type ClusterInput interface {
	pulumi.Input

	ToClusterOutput() ClusterOutput
	ToClusterOutputWithContext(ctx context.Context) ClusterOutput
}

func (*Cluster) ElementType() reflect.Type {
	return reflect.TypeOf((**Cluster)(nil)).Elem()
}

func (i *Cluster) ToClusterOutput() ClusterOutput {
	return i.ToClusterOutputWithContext(context.Background())
}

func (i *Cluster) ToClusterOutputWithContext(ctx context.Context) ClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterOutput)
}

func (i *Cluster) ToOutput(ctx context.Context) pulumix.Output[*Cluster] {
	return pulumix.Output[*Cluster]{
		OutputState: i.ToClusterOutputWithContext(ctx).OutputState,
	}
}

type ClusterOutput struct{ *pulumi.OutputState }

func (ClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Cluster)(nil)).Elem()
}

func (o ClusterOutput) ToClusterOutput() ClusterOutput {
	return o
}

func (o ClusterOutput) ToClusterOutputWithContext(ctx context.Context) ClusterOutput {
	return o
}

func (o ClusterOutput) ToOutput(ctx context.Context) pulumix.Output[*Cluster] {
	return pulumix.Output[*Cluster]{
		OutputState: o.OutputState,
	}
}

// The Amazon Resource Name (ARN) of the Amazon ECS cluster, such as arn:aws:ecs:us-east-2:123456789012:cluster/MyECSCluster.
func (o ClusterOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o ClusterOutput) CapacityProviders() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringArrayOutput { return v.CapacityProviders }).(pulumi.StringArrayOutput)
}

// A user-generated string that you use to identify your cluster. If you don't specify a name, AWS CloudFormation generates a unique physical ID for the name.
func (o ClusterOutput) ClusterName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Cluster) pulumi.StringPtrOutput { return v.ClusterName }).(pulumi.StringPtrOutput)
}

func (o ClusterOutput) ClusterSettings() ClusterSettingsArrayOutput {
	return o.ApplyT(func(v *Cluster) ClusterSettingsArrayOutput { return v.ClusterSettings }).(ClusterSettingsArrayOutput)
}

func (o ClusterOutput) Configuration() ClusterConfigurationPtrOutput {
	return o.ApplyT(func(v *Cluster) ClusterConfigurationPtrOutput { return v.Configuration }).(ClusterConfigurationPtrOutput)
}

func (o ClusterOutput) DefaultCapacityProviderStrategy() ClusterCapacityProviderStrategyItemArrayOutput {
	return o.ApplyT(func(v *Cluster) ClusterCapacityProviderStrategyItemArrayOutput {
		return v.DefaultCapacityProviderStrategy
	}).(ClusterCapacityProviderStrategyItemArrayOutput)
}

func (o ClusterOutput) ServiceConnectDefaults() ClusterServiceConnectDefaultsPtrOutput {
	return o.ApplyT(func(v *Cluster) ClusterServiceConnectDefaultsPtrOutput { return v.ServiceConnectDefaults }).(ClusterServiceConnectDefaultsPtrOutput)
}

func (o ClusterOutput) Tags() ClusterTagArrayOutput {
	return o.ApplyT(func(v *Cluster) ClusterTagArrayOutput { return v.Tags }).(ClusterTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ClusterInput)(nil)).Elem(), &Cluster{})
	pulumi.RegisterOutputType(ClusterOutput{})
}
