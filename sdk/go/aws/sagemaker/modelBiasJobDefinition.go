// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::SageMaker::ModelBiasJobDefinition
type ModelBiasJobDefinition struct {
	pulumi.CustomResourceState

	// The time at which the job definition was created.
	CreationTime pulumi.StringOutput    `pulumi:"creationTime"`
	EndpointName pulumi.StringPtrOutput `pulumi:"endpointName"`
	// The Amazon Resource Name (ARN) of job definition.
	JobDefinitionArn          pulumi.StringOutput                                    `pulumi:"jobDefinitionArn"`
	JobDefinitionName         pulumi.StringPtrOutput                                 `pulumi:"jobDefinitionName"`
	JobResources              ModelBiasJobDefinitionMonitoringResourcesOutput        `pulumi:"jobResources"`
	ModelBiasAppSpecification ModelBiasJobDefinitionModelBiasAppSpecificationOutput  `pulumi:"modelBiasAppSpecification"`
	ModelBiasBaselineConfig   ModelBiasJobDefinitionModelBiasBaselineConfigPtrOutput `pulumi:"modelBiasBaselineConfig"`
	ModelBiasJobInput         ModelBiasJobDefinitionModelBiasJobInputOutput          `pulumi:"modelBiasJobInput"`
	ModelBiasJobOutputConfig  ModelBiasJobDefinitionMonitoringOutputConfigOutput     `pulumi:"modelBiasJobOutputConfig"`
	NetworkConfig             ModelBiasJobDefinitionNetworkConfigPtrOutput           `pulumi:"networkConfig"`
	// The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
	RoleArn           pulumi.StringOutput                              `pulumi:"roleArn"`
	StoppingCondition ModelBiasJobDefinitionStoppingConditionPtrOutput `pulumi:"stoppingCondition"`
	// An array of key-value pairs to apply to this resource.
	Tags ModelBiasJobDefinitionTagArrayOutput `pulumi:"tags"`
}

// NewModelBiasJobDefinition registers a new resource with the given unique name, arguments, and options.
func NewModelBiasJobDefinition(ctx *pulumi.Context,
	name string, args *ModelBiasJobDefinitionArgs, opts ...pulumi.ResourceOption) (*ModelBiasJobDefinition, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.JobResources == nil {
		return nil, errors.New("invalid value for required argument 'JobResources'")
	}
	if args.ModelBiasAppSpecification == nil {
		return nil, errors.New("invalid value for required argument 'ModelBiasAppSpecification'")
	}
	if args.ModelBiasJobInput == nil {
		return nil, errors.New("invalid value for required argument 'ModelBiasJobInput'")
	}
	if args.ModelBiasJobOutputConfig == nil {
		return nil, errors.New("invalid value for required argument 'ModelBiasJobOutputConfig'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"endpointName",
		"jobDefinitionName",
		"jobResources",
		"modelBiasAppSpecification",
		"modelBiasBaselineConfig",
		"modelBiasJobInput",
		"modelBiasJobOutputConfig",
		"networkConfig",
		"roleArn",
		"stoppingCondition",
		"tags[*]",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ModelBiasJobDefinition
	err := ctx.RegisterResource("aws-native:sagemaker:ModelBiasJobDefinition", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetModelBiasJobDefinition gets an existing ModelBiasJobDefinition resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetModelBiasJobDefinition(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ModelBiasJobDefinitionState, opts ...pulumi.ResourceOption) (*ModelBiasJobDefinition, error) {
	var resource ModelBiasJobDefinition
	err := ctx.ReadResource("aws-native:sagemaker:ModelBiasJobDefinition", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ModelBiasJobDefinition resources.
type modelBiasJobDefinitionState struct {
}

type ModelBiasJobDefinitionState struct {
}

func (ModelBiasJobDefinitionState) ElementType() reflect.Type {
	return reflect.TypeOf((*modelBiasJobDefinitionState)(nil)).Elem()
}

type modelBiasJobDefinitionArgs struct {
	EndpointName              *string                                         `pulumi:"endpointName"`
	JobDefinitionName         *string                                         `pulumi:"jobDefinitionName"`
	JobResources              ModelBiasJobDefinitionMonitoringResources       `pulumi:"jobResources"`
	ModelBiasAppSpecification ModelBiasJobDefinitionModelBiasAppSpecification `pulumi:"modelBiasAppSpecification"`
	ModelBiasBaselineConfig   *ModelBiasJobDefinitionModelBiasBaselineConfig  `pulumi:"modelBiasBaselineConfig"`
	ModelBiasJobInput         ModelBiasJobDefinitionModelBiasJobInput         `pulumi:"modelBiasJobInput"`
	ModelBiasJobOutputConfig  ModelBiasJobDefinitionMonitoringOutputConfig    `pulumi:"modelBiasJobOutputConfig"`
	NetworkConfig             *ModelBiasJobDefinitionNetworkConfig            `pulumi:"networkConfig"`
	// The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
	RoleArn           string                                   `pulumi:"roleArn"`
	StoppingCondition *ModelBiasJobDefinitionStoppingCondition `pulumi:"stoppingCondition"`
	// An array of key-value pairs to apply to this resource.
	Tags []ModelBiasJobDefinitionTag `pulumi:"tags"`
}

// The set of arguments for constructing a ModelBiasJobDefinition resource.
type ModelBiasJobDefinitionArgs struct {
	EndpointName              pulumi.StringPtrInput
	JobDefinitionName         pulumi.StringPtrInput
	JobResources              ModelBiasJobDefinitionMonitoringResourcesInput
	ModelBiasAppSpecification ModelBiasJobDefinitionModelBiasAppSpecificationInput
	ModelBiasBaselineConfig   ModelBiasJobDefinitionModelBiasBaselineConfigPtrInput
	ModelBiasJobInput         ModelBiasJobDefinitionModelBiasJobInputInput
	ModelBiasJobOutputConfig  ModelBiasJobDefinitionMonitoringOutputConfigInput
	NetworkConfig             ModelBiasJobDefinitionNetworkConfigPtrInput
	// The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
	RoleArn           pulumi.StringInput
	StoppingCondition ModelBiasJobDefinitionStoppingConditionPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags ModelBiasJobDefinitionTagArrayInput
}

func (ModelBiasJobDefinitionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*modelBiasJobDefinitionArgs)(nil)).Elem()
}

type ModelBiasJobDefinitionInput interface {
	pulumi.Input

	ToModelBiasJobDefinitionOutput() ModelBiasJobDefinitionOutput
	ToModelBiasJobDefinitionOutputWithContext(ctx context.Context) ModelBiasJobDefinitionOutput
}

func (*ModelBiasJobDefinition) ElementType() reflect.Type {
	return reflect.TypeOf((**ModelBiasJobDefinition)(nil)).Elem()
}

func (i *ModelBiasJobDefinition) ToModelBiasJobDefinitionOutput() ModelBiasJobDefinitionOutput {
	return i.ToModelBiasJobDefinitionOutputWithContext(context.Background())
}

func (i *ModelBiasJobDefinition) ToModelBiasJobDefinitionOutputWithContext(ctx context.Context) ModelBiasJobDefinitionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelBiasJobDefinitionOutput)
}

func (i *ModelBiasJobDefinition) ToOutput(ctx context.Context) pulumix.Output[*ModelBiasJobDefinition] {
	return pulumix.Output[*ModelBiasJobDefinition]{
		OutputState: i.ToModelBiasJobDefinitionOutputWithContext(ctx).OutputState,
	}
}

type ModelBiasJobDefinitionOutput struct{ *pulumi.OutputState }

func (ModelBiasJobDefinitionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ModelBiasJobDefinition)(nil)).Elem()
}

func (o ModelBiasJobDefinitionOutput) ToModelBiasJobDefinitionOutput() ModelBiasJobDefinitionOutput {
	return o
}

func (o ModelBiasJobDefinitionOutput) ToModelBiasJobDefinitionOutputWithContext(ctx context.Context) ModelBiasJobDefinitionOutput {
	return o
}

func (o ModelBiasJobDefinitionOutput) ToOutput(ctx context.Context) pulumix.Output[*ModelBiasJobDefinition] {
	return pulumix.Output[*ModelBiasJobDefinition]{
		OutputState: o.OutputState,
	}
}

// The time at which the job definition was created.
func (o ModelBiasJobDefinitionOutput) CreationTime() pulumi.StringOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) pulumi.StringOutput { return v.CreationTime }).(pulumi.StringOutput)
}

func (o ModelBiasJobDefinitionOutput) EndpointName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) pulumi.StringPtrOutput { return v.EndpointName }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) of job definition.
func (o ModelBiasJobDefinitionOutput) JobDefinitionArn() pulumi.StringOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) pulumi.StringOutput { return v.JobDefinitionArn }).(pulumi.StringOutput)
}

func (o ModelBiasJobDefinitionOutput) JobDefinitionName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) pulumi.StringPtrOutput { return v.JobDefinitionName }).(pulumi.StringPtrOutput)
}

func (o ModelBiasJobDefinitionOutput) JobResources() ModelBiasJobDefinitionMonitoringResourcesOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) ModelBiasJobDefinitionMonitoringResourcesOutput { return v.JobResources }).(ModelBiasJobDefinitionMonitoringResourcesOutput)
}

func (o ModelBiasJobDefinitionOutput) ModelBiasAppSpecification() ModelBiasJobDefinitionModelBiasAppSpecificationOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) ModelBiasJobDefinitionModelBiasAppSpecificationOutput {
		return v.ModelBiasAppSpecification
	}).(ModelBiasJobDefinitionModelBiasAppSpecificationOutput)
}

func (o ModelBiasJobDefinitionOutput) ModelBiasBaselineConfig() ModelBiasJobDefinitionModelBiasBaselineConfigPtrOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) ModelBiasJobDefinitionModelBiasBaselineConfigPtrOutput {
		return v.ModelBiasBaselineConfig
	}).(ModelBiasJobDefinitionModelBiasBaselineConfigPtrOutput)
}

func (o ModelBiasJobDefinitionOutput) ModelBiasJobInput() ModelBiasJobDefinitionModelBiasJobInputOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) ModelBiasJobDefinitionModelBiasJobInputOutput {
		return v.ModelBiasJobInput
	}).(ModelBiasJobDefinitionModelBiasJobInputOutput)
}

func (o ModelBiasJobDefinitionOutput) ModelBiasJobOutputConfig() ModelBiasJobDefinitionMonitoringOutputConfigOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) ModelBiasJobDefinitionMonitoringOutputConfigOutput {
		return v.ModelBiasJobOutputConfig
	}).(ModelBiasJobDefinitionMonitoringOutputConfigOutput)
}

func (o ModelBiasJobDefinitionOutput) NetworkConfig() ModelBiasJobDefinitionNetworkConfigPtrOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) ModelBiasJobDefinitionNetworkConfigPtrOutput { return v.NetworkConfig }).(ModelBiasJobDefinitionNetworkConfigPtrOutput)
}

// The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
func (o ModelBiasJobDefinitionOutput) RoleArn() pulumi.StringOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) pulumi.StringOutput { return v.RoleArn }).(pulumi.StringOutput)
}

func (o ModelBiasJobDefinitionOutput) StoppingCondition() ModelBiasJobDefinitionStoppingConditionPtrOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) ModelBiasJobDefinitionStoppingConditionPtrOutput {
		return v.StoppingCondition
	}).(ModelBiasJobDefinitionStoppingConditionPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o ModelBiasJobDefinitionOutput) Tags() ModelBiasJobDefinitionTagArrayOutput {
	return o.ApplyT(func(v *ModelBiasJobDefinition) ModelBiasJobDefinitionTagArrayOutput { return v.Tags }).(ModelBiasJobDefinitionTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ModelBiasJobDefinitionInput)(nil)).Elem(), &ModelBiasJobDefinition{})
	pulumi.RegisterOutputType(ModelBiasJobDefinitionOutput{})
}
