// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package codedeploy

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::CodeDeploy::DeploymentConfig
type DeploymentConfig struct {
	pulumi.CustomResourceState

	// The destination platform type for the deployment (Lambda, Server, or ECS).
	ComputePlatform pulumi.StringPtrOutput `pulumi:"computePlatform"`
	// A name for the deployment configuration. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see Name Type.
	DeploymentConfigName pulumi.StringPtrOutput `pulumi:"deploymentConfigName"`
	// The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.
	MinimumHealthyHosts DeploymentConfigMinimumHealthyHostsPtrOutput `pulumi:"minimumHealthyHosts"`
	// The configuration that specifies how the deployment traffic is routed.
	TrafficRoutingConfig DeploymentConfigTrafficRoutingConfigPtrOutput `pulumi:"trafficRoutingConfig"`
}

// NewDeploymentConfig registers a new resource with the given unique name, arguments, and options.
func NewDeploymentConfig(ctx *pulumi.Context,
	name string, args *DeploymentConfigArgs, opts ...pulumi.ResourceOption) (*DeploymentConfig, error) {
	if args == nil {
		args = &DeploymentConfigArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"computePlatform",
		"deploymentConfigName",
		"minimumHealthyHosts",
		"trafficRoutingConfig",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DeploymentConfig
	err := ctx.RegisterResource("aws-native:codedeploy:DeploymentConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDeploymentConfig gets an existing DeploymentConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDeploymentConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeploymentConfigState, opts ...pulumi.ResourceOption) (*DeploymentConfig, error) {
	var resource DeploymentConfig
	err := ctx.ReadResource("aws-native:codedeploy:DeploymentConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DeploymentConfig resources.
type deploymentConfigState struct {
}

type DeploymentConfigState struct {
}

func (DeploymentConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentConfigState)(nil)).Elem()
}

type deploymentConfigArgs struct {
	// The destination platform type for the deployment (Lambda, Server, or ECS).
	ComputePlatform *string `pulumi:"computePlatform"`
	// A name for the deployment configuration. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see Name Type.
	DeploymentConfigName *string `pulumi:"deploymentConfigName"`
	// The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.
	MinimumHealthyHosts *DeploymentConfigMinimumHealthyHosts `pulumi:"minimumHealthyHosts"`
	// The configuration that specifies how the deployment traffic is routed.
	TrafficRoutingConfig *DeploymentConfigTrafficRoutingConfig `pulumi:"trafficRoutingConfig"`
}

// The set of arguments for constructing a DeploymentConfig resource.
type DeploymentConfigArgs struct {
	// The destination platform type for the deployment (Lambda, Server, or ECS).
	ComputePlatform pulumi.StringPtrInput
	// A name for the deployment configuration. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see Name Type.
	DeploymentConfigName pulumi.StringPtrInput
	// The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.
	MinimumHealthyHosts DeploymentConfigMinimumHealthyHostsPtrInput
	// The configuration that specifies how the deployment traffic is routed.
	TrafficRoutingConfig DeploymentConfigTrafficRoutingConfigPtrInput
}

func (DeploymentConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentConfigArgs)(nil)).Elem()
}

type DeploymentConfigInput interface {
	pulumi.Input

	ToDeploymentConfigOutput() DeploymentConfigOutput
	ToDeploymentConfigOutputWithContext(ctx context.Context) DeploymentConfigOutput
}

func (*DeploymentConfig) ElementType() reflect.Type {
	return reflect.TypeOf((**DeploymentConfig)(nil)).Elem()
}

func (i *DeploymentConfig) ToDeploymentConfigOutput() DeploymentConfigOutput {
	return i.ToDeploymentConfigOutputWithContext(context.Background())
}

func (i *DeploymentConfig) ToDeploymentConfigOutputWithContext(ctx context.Context) DeploymentConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeploymentConfigOutput)
}

func (i *DeploymentConfig) ToOutput(ctx context.Context) pulumix.Output[*DeploymentConfig] {
	return pulumix.Output[*DeploymentConfig]{
		OutputState: i.ToDeploymentConfigOutputWithContext(ctx).OutputState,
	}
}

type DeploymentConfigOutput struct{ *pulumi.OutputState }

func (DeploymentConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DeploymentConfig)(nil)).Elem()
}

func (o DeploymentConfigOutput) ToDeploymentConfigOutput() DeploymentConfigOutput {
	return o
}

func (o DeploymentConfigOutput) ToDeploymentConfigOutputWithContext(ctx context.Context) DeploymentConfigOutput {
	return o
}

func (o DeploymentConfigOutput) ToOutput(ctx context.Context) pulumix.Output[*DeploymentConfig] {
	return pulumix.Output[*DeploymentConfig]{
		OutputState: o.OutputState,
	}
}

// The destination platform type for the deployment (Lambda, Server, or ECS).
func (o DeploymentConfigOutput) ComputePlatform() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DeploymentConfig) pulumi.StringPtrOutput { return v.ComputePlatform }).(pulumi.StringPtrOutput)
}

// A name for the deployment configuration. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see Name Type.
func (o DeploymentConfigOutput) DeploymentConfigName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DeploymentConfig) pulumi.StringPtrOutput { return v.DeploymentConfigName }).(pulumi.StringPtrOutput)
}

// The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value.
func (o DeploymentConfigOutput) MinimumHealthyHosts() DeploymentConfigMinimumHealthyHostsPtrOutput {
	return o.ApplyT(func(v *DeploymentConfig) DeploymentConfigMinimumHealthyHostsPtrOutput { return v.MinimumHealthyHosts }).(DeploymentConfigMinimumHealthyHostsPtrOutput)
}

// The configuration that specifies how the deployment traffic is routed.
func (o DeploymentConfigOutput) TrafficRoutingConfig() DeploymentConfigTrafficRoutingConfigPtrOutput {
	return o.ApplyT(func(v *DeploymentConfig) DeploymentConfigTrafficRoutingConfigPtrOutput { return v.TrafficRoutingConfig }).(DeploymentConfigTrafficRoutingConfigPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DeploymentConfigInput)(nil)).Elem(), &DeploymentConfig{})
	pulumi.RegisterOutputType(DeploymentConfigOutput{})
}
