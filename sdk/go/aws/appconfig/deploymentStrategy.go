// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package appconfig

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::AppConfig::DeploymentStrategy
//
// Deprecated: DeploymentStrategy is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type DeploymentStrategy struct {
	pulumi.CustomResourceState

	DeploymentDurationInMinutes pulumi.Float64Output              `pulumi:"deploymentDurationInMinutes"`
	Description                 pulumi.StringPtrOutput            `pulumi:"description"`
	FinalBakeTimeInMinutes      pulumi.Float64PtrOutput           `pulumi:"finalBakeTimeInMinutes"`
	GrowthFactor                pulumi.Float64Output              `pulumi:"growthFactor"`
	GrowthType                  pulumi.StringPtrOutput            `pulumi:"growthType"`
	Name                        pulumi.StringOutput               `pulumi:"name"`
	ReplicateTo                 pulumi.StringOutput               `pulumi:"replicateTo"`
	Tags                        DeploymentStrategyTagsArrayOutput `pulumi:"tags"`
}

// NewDeploymentStrategy registers a new resource with the given unique name, arguments, and options.
func NewDeploymentStrategy(ctx *pulumi.Context,
	name string, args *DeploymentStrategyArgs, opts ...pulumi.ResourceOption) (*DeploymentStrategy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DeploymentDurationInMinutes == nil {
		return nil, errors.New("invalid value for required argument 'DeploymentDurationInMinutes'")
	}
	if args.GrowthFactor == nil {
		return nil, errors.New("invalid value for required argument 'GrowthFactor'")
	}
	if args.ReplicateTo == nil {
		return nil, errors.New("invalid value for required argument 'ReplicateTo'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
		"replicateTo",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DeploymentStrategy
	err := ctx.RegisterResource("aws-native:appconfig:DeploymentStrategy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDeploymentStrategy gets an existing DeploymentStrategy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDeploymentStrategy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeploymentStrategyState, opts ...pulumi.ResourceOption) (*DeploymentStrategy, error) {
	var resource DeploymentStrategy
	err := ctx.ReadResource("aws-native:appconfig:DeploymentStrategy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DeploymentStrategy resources.
type deploymentStrategyState struct {
}

type DeploymentStrategyState struct {
}

func (DeploymentStrategyState) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentStrategyState)(nil)).Elem()
}

type deploymentStrategyArgs struct {
	DeploymentDurationInMinutes float64                  `pulumi:"deploymentDurationInMinutes"`
	Description                 *string                  `pulumi:"description"`
	FinalBakeTimeInMinutes      *float64                 `pulumi:"finalBakeTimeInMinutes"`
	GrowthFactor                float64                  `pulumi:"growthFactor"`
	GrowthType                  *string                  `pulumi:"growthType"`
	Name                        *string                  `pulumi:"name"`
	ReplicateTo                 string                   `pulumi:"replicateTo"`
	Tags                        []DeploymentStrategyTags `pulumi:"tags"`
}

// The set of arguments for constructing a DeploymentStrategy resource.
type DeploymentStrategyArgs struct {
	DeploymentDurationInMinutes pulumi.Float64Input
	Description                 pulumi.StringPtrInput
	FinalBakeTimeInMinutes      pulumi.Float64PtrInput
	GrowthFactor                pulumi.Float64Input
	GrowthType                  pulumi.StringPtrInput
	Name                        pulumi.StringPtrInput
	ReplicateTo                 pulumi.StringInput
	Tags                        DeploymentStrategyTagsArrayInput
}

func (DeploymentStrategyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentStrategyArgs)(nil)).Elem()
}

type DeploymentStrategyInput interface {
	pulumi.Input

	ToDeploymentStrategyOutput() DeploymentStrategyOutput
	ToDeploymentStrategyOutputWithContext(ctx context.Context) DeploymentStrategyOutput
}

func (*DeploymentStrategy) ElementType() reflect.Type {
	return reflect.TypeOf((**DeploymentStrategy)(nil)).Elem()
}

func (i *DeploymentStrategy) ToDeploymentStrategyOutput() DeploymentStrategyOutput {
	return i.ToDeploymentStrategyOutputWithContext(context.Background())
}

func (i *DeploymentStrategy) ToDeploymentStrategyOutputWithContext(ctx context.Context) DeploymentStrategyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeploymentStrategyOutput)
}

func (i *DeploymentStrategy) ToOutput(ctx context.Context) pulumix.Output[*DeploymentStrategy] {
	return pulumix.Output[*DeploymentStrategy]{
		OutputState: i.ToDeploymentStrategyOutputWithContext(ctx).OutputState,
	}
}

type DeploymentStrategyOutput struct{ *pulumi.OutputState }

func (DeploymentStrategyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DeploymentStrategy)(nil)).Elem()
}

func (o DeploymentStrategyOutput) ToDeploymentStrategyOutput() DeploymentStrategyOutput {
	return o
}

func (o DeploymentStrategyOutput) ToDeploymentStrategyOutputWithContext(ctx context.Context) DeploymentStrategyOutput {
	return o
}

func (o DeploymentStrategyOutput) ToOutput(ctx context.Context) pulumix.Output[*DeploymentStrategy] {
	return pulumix.Output[*DeploymentStrategy]{
		OutputState: o.OutputState,
	}
}

func (o DeploymentStrategyOutput) DeploymentDurationInMinutes() pulumi.Float64Output {
	return o.ApplyT(func(v *DeploymentStrategy) pulumi.Float64Output { return v.DeploymentDurationInMinutes }).(pulumi.Float64Output)
}

func (o DeploymentStrategyOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DeploymentStrategy) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o DeploymentStrategyOutput) FinalBakeTimeInMinutes() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v *DeploymentStrategy) pulumi.Float64PtrOutput { return v.FinalBakeTimeInMinutes }).(pulumi.Float64PtrOutput)
}

func (o DeploymentStrategyOutput) GrowthFactor() pulumi.Float64Output {
	return o.ApplyT(func(v *DeploymentStrategy) pulumi.Float64Output { return v.GrowthFactor }).(pulumi.Float64Output)
}

func (o DeploymentStrategyOutput) GrowthType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DeploymentStrategy) pulumi.StringPtrOutput { return v.GrowthType }).(pulumi.StringPtrOutput)
}

func (o DeploymentStrategyOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentStrategy) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o DeploymentStrategyOutput) ReplicateTo() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentStrategy) pulumi.StringOutput { return v.ReplicateTo }).(pulumi.StringOutput)
}

func (o DeploymentStrategyOutput) Tags() DeploymentStrategyTagsArrayOutput {
	return o.ApplyT(func(v *DeploymentStrategy) DeploymentStrategyTagsArrayOutput { return v.Tags }).(DeploymentStrategyTagsArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DeploymentStrategyInput)(nil)).Elem(), &DeploymentStrategy{})
	pulumi.RegisterOutputType(DeploymentStrategyOutput{})
}
