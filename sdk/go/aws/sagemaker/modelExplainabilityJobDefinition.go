// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html
type ModelExplainabilityJobDefinition struct {
	pulumi.CustomResourceState

	CreationTime     pulumi.StringOutput `pulumi:"creationTime"`
	JobDefinitionArn pulumi.StringOutput `pulumi:"jobDefinitionArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobdefinitionname
	JobDefinitionName pulumi.StringPtrOutput `pulumi:"jobDefinitionName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobresources
	JobResources ModelExplainabilityJobDefinitionMonitoringResourcesOutput `pulumi:"jobResources"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification
	ModelExplainabilityAppSpecification ModelExplainabilityJobDefinitionModelExplainabilityAppSpecificationOutput `pulumi:"modelExplainabilityAppSpecification"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig
	ModelExplainabilityBaselineConfig ModelExplainabilityJobDefinitionModelExplainabilityBaselineConfigPtrOutput `pulumi:"modelExplainabilityBaselineConfig"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput
	ModelExplainabilityJobInput ModelExplainabilityJobDefinitionModelExplainabilityJobInputOutput `pulumi:"modelExplainabilityJobInput"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjoboutputconfig
	ModelExplainabilityJobOutputConfig ModelExplainabilityJobDefinitionMonitoringOutputConfigOutput `pulumi:"modelExplainabilityJobOutputConfig"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig
	NetworkConfig ModelExplainabilityJobDefinitionNetworkConfigPtrOutput `pulumi:"networkConfig"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-rolearn
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition
	StoppingCondition ModelExplainabilityJobDefinitionStoppingConditionPtrOutput `pulumi:"stoppingCondition"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-tags
	Tags aws.TagArrayOutput `pulumi:"tags"`
}

// NewModelExplainabilityJobDefinition registers a new resource with the given unique name, arguments, and options.
func NewModelExplainabilityJobDefinition(ctx *pulumi.Context,
	name string, args *ModelExplainabilityJobDefinitionArgs, opts ...pulumi.ResourceOption) (*ModelExplainabilityJobDefinition, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.JobResources == nil {
		return nil, errors.New("invalid value for required argument 'JobResources'")
	}
	if args.ModelExplainabilityAppSpecification == nil {
		return nil, errors.New("invalid value for required argument 'ModelExplainabilityAppSpecification'")
	}
	if args.ModelExplainabilityJobInput == nil {
		return nil, errors.New("invalid value for required argument 'ModelExplainabilityJobInput'")
	}
	if args.ModelExplainabilityJobOutputConfig == nil {
		return nil, errors.New("invalid value for required argument 'ModelExplainabilityJobOutputConfig'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	var resource ModelExplainabilityJobDefinition
	err := ctx.RegisterResource("aws-native:SageMaker:ModelExplainabilityJobDefinition", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetModelExplainabilityJobDefinition gets an existing ModelExplainabilityJobDefinition resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetModelExplainabilityJobDefinition(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ModelExplainabilityJobDefinitionState, opts ...pulumi.ResourceOption) (*ModelExplainabilityJobDefinition, error) {
	var resource ModelExplainabilityJobDefinition
	err := ctx.ReadResource("aws-native:SageMaker:ModelExplainabilityJobDefinition", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ModelExplainabilityJobDefinition resources.
type modelExplainabilityJobDefinitionState struct {
}

type ModelExplainabilityJobDefinitionState struct {
}

func (ModelExplainabilityJobDefinitionState) ElementType() reflect.Type {
	return reflect.TypeOf((*modelExplainabilityJobDefinitionState)(nil)).Elem()
}

type modelExplainabilityJobDefinitionArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobdefinitionname
	JobDefinitionName *string `pulumi:"jobDefinitionName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobresources
	JobResources ModelExplainabilityJobDefinitionMonitoringResources `pulumi:"jobResources"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification
	ModelExplainabilityAppSpecification ModelExplainabilityJobDefinitionModelExplainabilityAppSpecification `pulumi:"modelExplainabilityAppSpecification"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig
	ModelExplainabilityBaselineConfig *ModelExplainabilityJobDefinitionModelExplainabilityBaselineConfig `pulumi:"modelExplainabilityBaselineConfig"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput
	ModelExplainabilityJobInput ModelExplainabilityJobDefinitionModelExplainabilityJobInput `pulumi:"modelExplainabilityJobInput"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjoboutputconfig
	ModelExplainabilityJobOutputConfig ModelExplainabilityJobDefinitionMonitoringOutputConfig `pulumi:"modelExplainabilityJobOutputConfig"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig
	NetworkConfig *ModelExplainabilityJobDefinitionNetworkConfig `pulumi:"networkConfig"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-rolearn
	RoleArn string `pulumi:"roleArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition
	StoppingCondition *ModelExplainabilityJobDefinitionStoppingCondition `pulumi:"stoppingCondition"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-tags
	Tags []aws.Tag `pulumi:"tags"`
}

// The set of arguments for constructing a ModelExplainabilityJobDefinition resource.
type ModelExplainabilityJobDefinitionArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobdefinitionname
	JobDefinitionName pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-jobresources
	JobResources ModelExplainabilityJobDefinitionMonitoringResourcesInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityappspecification
	ModelExplainabilityAppSpecification ModelExplainabilityJobDefinitionModelExplainabilityAppSpecificationInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilitybaselineconfig
	ModelExplainabilityBaselineConfig ModelExplainabilityJobDefinitionModelExplainabilityBaselineConfigPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjobinput
	ModelExplainabilityJobInput ModelExplainabilityJobDefinitionModelExplainabilityJobInputInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-modelexplainabilityjoboutputconfig
	ModelExplainabilityJobOutputConfig ModelExplainabilityJobDefinitionMonitoringOutputConfigInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-networkconfig
	NetworkConfig ModelExplainabilityJobDefinitionNetworkConfigPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-rolearn
	RoleArn pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-stoppingcondition
	StoppingCondition ModelExplainabilityJobDefinitionStoppingConditionPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelexplainabilityjobdefinition.html#cfn-sagemaker-modelexplainabilityjobdefinition-tags
	Tags aws.TagArrayInput
}

func (ModelExplainabilityJobDefinitionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*modelExplainabilityJobDefinitionArgs)(nil)).Elem()
}

type ModelExplainabilityJobDefinitionInput interface {
	pulumi.Input

	ToModelExplainabilityJobDefinitionOutput() ModelExplainabilityJobDefinitionOutput
	ToModelExplainabilityJobDefinitionOutputWithContext(ctx context.Context) ModelExplainabilityJobDefinitionOutput
}

func (*ModelExplainabilityJobDefinition) ElementType() reflect.Type {
	return reflect.TypeOf((*ModelExplainabilityJobDefinition)(nil))
}

func (i *ModelExplainabilityJobDefinition) ToModelExplainabilityJobDefinitionOutput() ModelExplainabilityJobDefinitionOutput {
	return i.ToModelExplainabilityJobDefinitionOutputWithContext(context.Background())
}

func (i *ModelExplainabilityJobDefinition) ToModelExplainabilityJobDefinitionOutputWithContext(ctx context.Context) ModelExplainabilityJobDefinitionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ModelExplainabilityJobDefinitionOutput)
}

type ModelExplainabilityJobDefinitionOutput struct{ *pulumi.OutputState }

func (ModelExplainabilityJobDefinitionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ModelExplainabilityJobDefinition)(nil))
}

func (o ModelExplainabilityJobDefinitionOutput) ToModelExplainabilityJobDefinitionOutput() ModelExplainabilityJobDefinitionOutput {
	return o
}

func (o ModelExplainabilityJobDefinitionOutput) ToModelExplainabilityJobDefinitionOutputWithContext(ctx context.Context) ModelExplainabilityJobDefinitionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ModelExplainabilityJobDefinitionOutput{})
}
