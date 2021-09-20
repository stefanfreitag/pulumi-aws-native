// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SageMaker::ModelQualityJobDefinition
type ModelQualityJobDefinition struct {
	pulumi.CustomResourceState

	// The time at which the job definition was created.
	CreationTime pulumi.StringOutput `pulumi:"creationTime"`
	// The Amazon Resource Name (ARN) of job definition.
	JobDefinitionArn             pulumi.StringOutput                                          `pulumi:"jobDefinitionArn"`
	JobDefinitionName            pulumi.StringPtrOutput                                       `pulumi:"jobDefinitionName"`
	JobResources                 ModelQualityJobDefinitionMonitoringResourcesOutput           `pulumi:"jobResources"`
	ModelQualityAppSpecification ModelQualityJobDefinitionModelQualityAppSpecificationOutput  `pulumi:"modelQualityAppSpecification"`
	ModelQualityBaselineConfig   ModelQualityJobDefinitionModelQualityBaselineConfigPtrOutput `pulumi:"modelQualityBaselineConfig"`
	ModelQualityJobInput         ModelQualityJobDefinitionModelQualityJobInputOutput          `pulumi:"modelQualityJobInput"`
	ModelQualityJobOutputConfig  ModelQualityJobDefinitionMonitoringOutputConfigOutput        `pulumi:"modelQualityJobOutputConfig"`
	NetworkConfig                ModelQualityJobDefinitionNetworkConfigPtrOutput              `pulumi:"networkConfig"`
	// The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
	RoleArn           pulumi.StringOutput                                 `pulumi:"roleArn"`
	StoppingCondition ModelQualityJobDefinitionStoppingConditionPtrOutput `pulumi:"stoppingCondition"`
	// An array of key-value pairs to apply to this resource.
	Tags ModelQualityJobDefinitionTagArrayOutput `pulumi:"tags"`
}

// NewModelQualityJobDefinition registers a new resource with the given unique name, arguments, and options.
func NewModelQualityJobDefinition(ctx *pulumi.Context,
	name string, args *ModelQualityJobDefinitionArgs, opts ...pulumi.ResourceOption) (*ModelQualityJobDefinition, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.JobResources == nil {
		return nil, errors.New("invalid value for required argument 'JobResources'")
	}
	if args.ModelQualityAppSpecification == nil {
		return nil, errors.New("invalid value for required argument 'ModelQualityAppSpecification'")
	}
	if args.ModelQualityJobInput == nil {
		return nil, errors.New("invalid value for required argument 'ModelQualityJobInput'")
	}
	if args.ModelQualityJobOutputConfig == nil {
		return nil, errors.New("invalid value for required argument 'ModelQualityJobOutputConfig'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	var resource ModelQualityJobDefinition
	err := ctx.RegisterResource("aws-native:sagemaker:ModelQualityJobDefinition", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetModelQualityJobDefinition gets an existing ModelQualityJobDefinition resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetModelQualityJobDefinition(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ModelQualityJobDefinitionState, opts ...pulumi.ResourceOption) (*ModelQualityJobDefinition, error) {
	var resource ModelQualityJobDefinition
	err := ctx.ReadResource("aws-native:sagemaker:ModelQualityJobDefinition", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ModelQualityJobDefinition resources.
type modelQualityJobDefinitionState struct {
}

type ModelQualityJobDefinitionState struct {
}

func (ModelQualityJobDefinitionState) ElementType() reflect.Type {
	return reflect.TypeOf((*modelQualityJobDefinitionState)(nil)).Elem()
}

type modelQualityJobDefinitionArgs struct {
	JobDefinitionName            *string                                               `pulumi:"jobDefinitionName"`
	JobResources                 ModelQualityJobDefinitionMonitoringResources          `pulumi:"jobResources"`
	ModelQualityAppSpecification ModelQualityJobDefinitionModelQualityAppSpecification `pulumi:"modelQualityAppSpecification"`
	ModelQualityBaselineConfig   *ModelQualityJobDefinitionModelQualityBaselineConfig  `pulumi:"modelQualityBaselineConfig"`
	ModelQualityJobInput         ModelQualityJobDefinitionModelQualityJobInput         `pulumi:"modelQualityJobInput"`
	ModelQualityJobOutputConfig  ModelQualityJobDefinitionMonitoringOutputConfig       `pulumi:"modelQualityJobOutputConfig"`
	NetworkConfig                *ModelQualityJobDefinitionNetworkConfig               `pulumi:"networkConfig"`
	// The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
	RoleArn           string                                      `pulumi:"roleArn"`
	StoppingCondition *ModelQualityJobDefinitionStoppingCondition `pulumi:"stoppingCondition"`
	// An array of key-value pairs to apply to this resource.
	Tags []ModelQualityJobDefinitionTag `pulumi:"tags"`
}

// The set of arguments for constructing a ModelQualityJobDefinition resource.
type ModelQualityJobDefinitionArgs struct {
	JobDefinitionName            pulumi.StringPtrInput
	JobResources                 ModelQualityJobDefinitionMonitoringResourcesInput
	ModelQualityAppSpecification ModelQualityJobDefinitionModelQualityAppSpecificationInput
	ModelQualityBaselineConfig   ModelQualityJobDefinitionModelQualityBaselineConfigPtrInput
	ModelQualityJobInput         ModelQualityJobDefinitionModelQualityJobInputInput
	ModelQualityJobOutputConfig  ModelQualityJobDefinitionMonitoringOutputConfigInput
	NetworkConfig                ModelQualityJobDefinitionNetworkConfigPtrInput
	// The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
	RoleArn           pulumi.StringInput
	StoppingCondition ModelQualityJobDefinitionStoppingConditionPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags ModelQualityJobDefinitionTagArrayInput
}

func (ModelQualityJobDefinitionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*modelQualityJobDefinitionArgs)(nil)).Elem()
}

type ModelQualityJobDefinitionInput interface {
	pulumi.Input

	ToModelQualityJobDefinitionOutput() ModelQualityJobDefinitionOutput
	ToModelQualityJobDefinitionOutputWithContext(ctx context.Context) ModelQualityJobDefinitionOutput
}

func (*ModelQualityJobDefinition) ElementType() reflect.Type {
	return reflect.TypeOf((*ModelQualityJobDefinition)(nil))
}

func (i *ModelQualityJobDefinition) ToModelQualityJobDefinitionOutput() ModelQualityJobDefinitionOutput {
	return i.ToModelQualityJobDefinitionOutputWithContext(context.Background())
}

func (i *ModelQualityJobDefinition) ToModelQualityJobDefinitionOutputWithContext(ctx context.Context) ModelQualityJobDefinitionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelQualityJobDefinitionOutput)
}

type ModelQualityJobDefinitionOutput struct{ *pulumi.OutputState }

func (ModelQualityJobDefinitionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ModelQualityJobDefinition)(nil))
}

func (o ModelQualityJobDefinitionOutput) ToModelQualityJobDefinitionOutput() ModelQualityJobDefinitionOutput {
	return o
}

func (o ModelQualityJobDefinitionOutput) ToModelQualityJobDefinitionOutputWithContext(ctx context.Context) ModelQualityJobDefinitionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ModelQualityJobDefinitionOutput{})
}
