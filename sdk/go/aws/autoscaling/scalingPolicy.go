// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package autoscaling

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::AutoScaling::ScalingPolicy
//
// Deprecated: ScalingPolicy is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type ScalingPolicy struct {
	pulumi.CustomResourceState

	AdjustmentType                 pulumi.StringPtrOutput                               `pulumi:"adjustmentType"`
	AutoScalingGroupName           pulumi.StringOutput                                  `pulumi:"autoScalingGroupName"`
	Cooldown                       pulumi.StringPtrOutput                               `pulumi:"cooldown"`
	EstimatedInstanceWarmup        pulumi.IntPtrOutput                                  `pulumi:"estimatedInstanceWarmup"`
	MetricAggregationType          pulumi.StringPtrOutput                               `pulumi:"metricAggregationType"`
	MinAdjustmentMagnitude         pulumi.IntPtrOutput                                  `pulumi:"minAdjustmentMagnitude"`
	PolicyType                     pulumi.StringPtrOutput                               `pulumi:"policyType"`
	PredictiveScalingConfiguration ScalingPolicyPredictiveScalingConfigurationPtrOutput `pulumi:"predictiveScalingConfiguration"`
	ScalingAdjustment              pulumi.IntPtrOutput                                  `pulumi:"scalingAdjustment"`
	StepAdjustments                ScalingPolicyStepAdjustmentArrayOutput               `pulumi:"stepAdjustments"`
	TargetTrackingConfiguration    ScalingPolicyTargetTrackingConfigurationPtrOutput    `pulumi:"targetTrackingConfiguration"`
}

// NewScalingPolicy registers a new resource with the given unique name, arguments, and options.
func NewScalingPolicy(ctx *pulumi.Context,
	name string, args *ScalingPolicyArgs, opts ...pulumi.ResourceOption) (*ScalingPolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AutoScalingGroupName == nil {
		return nil, errors.New("invalid value for required argument 'AutoScalingGroupName'")
	}
	var resource ScalingPolicy
	err := ctx.RegisterResource("aws-native:autoscaling:ScalingPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetScalingPolicy gets an existing ScalingPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetScalingPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ScalingPolicyState, opts ...pulumi.ResourceOption) (*ScalingPolicy, error) {
	var resource ScalingPolicy
	err := ctx.ReadResource("aws-native:autoscaling:ScalingPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ScalingPolicy resources.
type scalingPolicyState struct {
}

type ScalingPolicyState struct {
}

func (ScalingPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*scalingPolicyState)(nil)).Elem()
}

type scalingPolicyArgs struct {
	AdjustmentType                 *string                                      `pulumi:"adjustmentType"`
	AutoScalingGroupName           string                                       `pulumi:"autoScalingGroupName"`
	Cooldown                       *string                                      `pulumi:"cooldown"`
	EstimatedInstanceWarmup        *int                                         `pulumi:"estimatedInstanceWarmup"`
	MetricAggregationType          *string                                      `pulumi:"metricAggregationType"`
	MinAdjustmentMagnitude         *int                                         `pulumi:"minAdjustmentMagnitude"`
	PolicyType                     *string                                      `pulumi:"policyType"`
	PredictiveScalingConfiguration *ScalingPolicyPredictiveScalingConfiguration `pulumi:"predictiveScalingConfiguration"`
	ScalingAdjustment              *int                                         `pulumi:"scalingAdjustment"`
	StepAdjustments                []ScalingPolicyStepAdjustment                `pulumi:"stepAdjustments"`
	TargetTrackingConfiguration    *ScalingPolicyTargetTrackingConfiguration    `pulumi:"targetTrackingConfiguration"`
}

// The set of arguments for constructing a ScalingPolicy resource.
type ScalingPolicyArgs struct {
	AdjustmentType                 pulumi.StringPtrInput
	AutoScalingGroupName           pulumi.StringInput
	Cooldown                       pulumi.StringPtrInput
	EstimatedInstanceWarmup        pulumi.IntPtrInput
	MetricAggregationType          pulumi.StringPtrInput
	MinAdjustmentMagnitude         pulumi.IntPtrInput
	PolicyType                     pulumi.StringPtrInput
	PredictiveScalingConfiguration ScalingPolicyPredictiveScalingConfigurationPtrInput
	ScalingAdjustment              pulumi.IntPtrInput
	StepAdjustments                ScalingPolicyStepAdjustmentArrayInput
	TargetTrackingConfiguration    ScalingPolicyTargetTrackingConfigurationPtrInput
}

func (ScalingPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*scalingPolicyArgs)(nil)).Elem()
}

type ScalingPolicyInput interface {
	pulumi.Input

	ToScalingPolicyOutput() ScalingPolicyOutput
	ToScalingPolicyOutputWithContext(ctx context.Context) ScalingPolicyOutput
}

func (*ScalingPolicy) ElementType() reflect.Type {
	return reflect.TypeOf((*ScalingPolicy)(nil))
}

func (i *ScalingPolicy) ToScalingPolicyOutput() ScalingPolicyOutput {
	return i.ToScalingPolicyOutputWithContext(context.Background())
}

func (i *ScalingPolicy) ToScalingPolicyOutputWithContext(ctx context.Context) ScalingPolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ScalingPolicyOutput)
}

type ScalingPolicyOutput struct{ *pulumi.OutputState }

func (ScalingPolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ScalingPolicy)(nil))
}

func (o ScalingPolicyOutput) ToScalingPolicyOutput() ScalingPolicyOutput {
	return o
}

func (o ScalingPolicyOutput) ToScalingPolicyOutputWithContext(ctx context.Context) ScalingPolicyOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ScalingPolicyOutput{})
}
