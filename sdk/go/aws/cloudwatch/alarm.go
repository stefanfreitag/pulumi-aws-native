// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cloudwatch

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CloudWatch::Alarm
//
// Deprecated: Alarm is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Alarm struct {
	pulumi.CustomResourceState

	ActionsEnabled                   pulumi.BoolPtrOutput            `pulumi:"actionsEnabled"`
	AlarmActions                     pulumi.StringArrayOutput        `pulumi:"alarmActions"`
	AlarmDescription                 pulumi.StringPtrOutput          `pulumi:"alarmDescription"`
	AlarmName                        pulumi.StringPtrOutput          `pulumi:"alarmName"`
	Arn                              pulumi.StringOutput             `pulumi:"arn"`
	ComparisonOperator               pulumi.StringOutput             `pulumi:"comparisonOperator"`
	DatapointsToAlarm                pulumi.IntPtrOutput             `pulumi:"datapointsToAlarm"`
	Dimensions                       AlarmDimensionArrayOutput       `pulumi:"dimensions"`
	EvaluateLowSampleCountPercentile pulumi.StringPtrOutput          `pulumi:"evaluateLowSampleCountPercentile"`
	EvaluationPeriods                pulumi.IntOutput                `pulumi:"evaluationPeriods"`
	ExtendedStatistic                pulumi.StringPtrOutput          `pulumi:"extendedStatistic"`
	InsufficientDataActions          pulumi.StringArrayOutput        `pulumi:"insufficientDataActions"`
	MetricName                       pulumi.StringPtrOutput          `pulumi:"metricName"`
	Metrics                          AlarmMetricDataQueryArrayOutput `pulumi:"metrics"`
	Namespace                        pulumi.StringPtrOutput          `pulumi:"namespace"`
	OKActions                        pulumi.StringArrayOutput        `pulumi:"oKActions"`
	Period                           pulumi.IntPtrOutput             `pulumi:"period"`
	Statistic                        pulumi.StringPtrOutput          `pulumi:"statistic"`
	Threshold                        pulumi.Float64PtrOutput         `pulumi:"threshold"`
	ThresholdMetricId                pulumi.StringPtrOutput          `pulumi:"thresholdMetricId"`
	TreatMissingData                 pulumi.StringPtrOutput          `pulumi:"treatMissingData"`
	Unit                             pulumi.StringPtrOutput          `pulumi:"unit"`
}

// NewAlarm registers a new resource with the given unique name, arguments, and options.
func NewAlarm(ctx *pulumi.Context,
	name string, args *AlarmArgs, opts ...pulumi.ResourceOption) (*Alarm, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ComparisonOperator == nil {
		return nil, errors.New("invalid value for required argument 'ComparisonOperator'")
	}
	if args.EvaluationPeriods == nil {
		return nil, errors.New("invalid value for required argument 'EvaluationPeriods'")
	}
	var resource Alarm
	err := ctx.RegisterResource("aws-native:cloudwatch:Alarm", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAlarm gets an existing Alarm resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAlarm(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AlarmState, opts ...pulumi.ResourceOption) (*Alarm, error) {
	var resource Alarm
	err := ctx.ReadResource("aws-native:cloudwatch:Alarm", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Alarm resources.
type alarmState struct {
}

type AlarmState struct {
}

func (AlarmState) ElementType() reflect.Type {
	return reflect.TypeOf((*alarmState)(nil)).Elem()
}

type alarmArgs struct {
	ActionsEnabled                   *bool                  `pulumi:"actionsEnabled"`
	AlarmActions                     []string               `pulumi:"alarmActions"`
	AlarmDescription                 *string                `pulumi:"alarmDescription"`
	AlarmName                        *string                `pulumi:"alarmName"`
	ComparisonOperator               string                 `pulumi:"comparisonOperator"`
	DatapointsToAlarm                *int                   `pulumi:"datapointsToAlarm"`
	Dimensions                       []AlarmDimension       `pulumi:"dimensions"`
	EvaluateLowSampleCountPercentile *string                `pulumi:"evaluateLowSampleCountPercentile"`
	EvaluationPeriods                int                    `pulumi:"evaluationPeriods"`
	ExtendedStatistic                *string                `pulumi:"extendedStatistic"`
	InsufficientDataActions          []string               `pulumi:"insufficientDataActions"`
	MetricName                       *string                `pulumi:"metricName"`
	Metrics                          []AlarmMetricDataQuery `pulumi:"metrics"`
	Namespace                        *string                `pulumi:"namespace"`
	OKActions                        []string               `pulumi:"oKActions"`
	Period                           *int                   `pulumi:"period"`
	Statistic                        *string                `pulumi:"statistic"`
	Threshold                        *float64               `pulumi:"threshold"`
	ThresholdMetricId                *string                `pulumi:"thresholdMetricId"`
	TreatMissingData                 *string                `pulumi:"treatMissingData"`
	Unit                             *string                `pulumi:"unit"`
}

// The set of arguments for constructing a Alarm resource.
type AlarmArgs struct {
	ActionsEnabled                   pulumi.BoolPtrInput
	AlarmActions                     pulumi.StringArrayInput
	AlarmDescription                 pulumi.StringPtrInput
	AlarmName                        pulumi.StringPtrInput
	ComparisonOperator               pulumi.StringInput
	DatapointsToAlarm                pulumi.IntPtrInput
	Dimensions                       AlarmDimensionArrayInput
	EvaluateLowSampleCountPercentile pulumi.StringPtrInput
	EvaluationPeriods                pulumi.IntInput
	ExtendedStatistic                pulumi.StringPtrInput
	InsufficientDataActions          pulumi.StringArrayInput
	MetricName                       pulumi.StringPtrInput
	Metrics                          AlarmMetricDataQueryArrayInput
	Namespace                        pulumi.StringPtrInput
	OKActions                        pulumi.StringArrayInput
	Period                           pulumi.IntPtrInput
	Statistic                        pulumi.StringPtrInput
	Threshold                        pulumi.Float64PtrInput
	ThresholdMetricId                pulumi.StringPtrInput
	TreatMissingData                 pulumi.StringPtrInput
	Unit                             pulumi.StringPtrInput
}

func (AlarmArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*alarmArgs)(nil)).Elem()
}

type AlarmInput interface {
	pulumi.Input

	ToAlarmOutput() AlarmOutput
	ToAlarmOutputWithContext(ctx context.Context) AlarmOutput
}

func (*Alarm) ElementType() reflect.Type {
	return reflect.TypeOf((**Alarm)(nil)).Elem()
}

func (i *Alarm) ToAlarmOutput() AlarmOutput {
	return i.ToAlarmOutputWithContext(context.Background())
}

func (i *Alarm) ToAlarmOutputWithContext(ctx context.Context) AlarmOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AlarmOutput)
}

type AlarmOutput struct{ *pulumi.OutputState }

func (AlarmOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Alarm)(nil)).Elem()
}

func (o AlarmOutput) ToAlarmOutput() AlarmOutput {
	return o
}

func (o AlarmOutput) ToAlarmOutputWithContext(ctx context.Context) AlarmOutput {
	return o
}

func (o AlarmOutput) ActionsEnabled() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.BoolPtrOutput { return v.ActionsEnabled }).(pulumi.BoolPtrOutput)
}

func (o AlarmOutput) AlarmActions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringArrayOutput { return v.AlarmActions }).(pulumi.StringArrayOutput)
}

func (o AlarmOutput) AlarmDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringPtrOutput { return v.AlarmDescription }).(pulumi.StringPtrOutput)
}

func (o AlarmOutput) AlarmName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringPtrOutput { return v.AlarmName }).(pulumi.StringPtrOutput)
}

func (o AlarmOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o AlarmOutput) ComparisonOperator() pulumi.StringOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringOutput { return v.ComparisonOperator }).(pulumi.StringOutput)
}

func (o AlarmOutput) DatapointsToAlarm() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.IntPtrOutput { return v.DatapointsToAlarm }).(pulumi.IntPtrOutput)
}

func (o AlarmOutput) Dimensions() AlarmDimensionArrayOutput {
	return o.ApplyT(func(v *Alarm) AlarmDimensionArrayOutput { return v.Dimensions }).(AlarmDimensionArrayOutput)
}

func (o AlarmOutput) EvaluateLowSampleCountPercentile() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringPtrOutput { return v.EvaluateLowSampleCountPercentile }).(pulumi.StringPtrOutput)
}

func (o AlarmOutput) EvaluationPeriods() pulumi.IntOutput {
	return o.ApplyT(func(v *Alarm) pulumi.IntOutput { return v.EvaluationPeriods }).(pulumi.IntOutput)
}

func (o AlarmOutput) ExtendedStatistic() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringPtrOutput { return v.ExtendedStatistic }).(pulumi.StringPtrOutput)
}

func (o AlarmOutput) InsufficientDataActions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringArrayOutput { return v.InsufficientDataActions }).(pulumi.StringArrayOutput)
}

func (o AlarmOutput) MetricName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringPtrOutput { return v.MetricName }).(pulumi.StringPtrOutput)
}

func (o AlarmOutput) Metrics() AlarmMetricDataQueryArrayOutput {
	return o.ApplyT(func(v *Alarm) AlarmMetricDataQueryArrayOutput { return v.Metrics }).(AlarmMetricDataQueryArrayOutput)
}

func (o AlarmOutput) Namespace() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringPtrOutput { return v.Namespace }).(pulumi.StringPtrOutput)
}

func (o AlarmOutput) OKActions() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringArrayOutput { return v.OKActions }).(pulumi.StringArrayOutput)
}

func (o AlarmOutput) Period() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.IntPtrOutput { return v.Period }).(pulumi.IntPtrOutput)
}

func (o AlarmOutput) Statistic() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringPtrOutput { return v.Statistic }).(pulumi.StringPtrOutput)
}

func (o AlarmOutput) Threshold() pulumi.Float64PtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.Float64PtrOutput { return v.Threshold }).(pulumi.Float64PtrOutput)
}

func (o AlarmOutput) ThresholdMetricId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringPtrOutput { return v.ThresholdMetricId }).(pulumi.StringPtrOutput)
}

func (o AlarmOutput) TreatMissingData() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringPtrOutput { return v.TreatMissingData }).(pulumi.StringPtrOutput)
}

func (o AlarmOutput) Unit() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Alarm) pulumi.StringPtrOutput { return v.Unit }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AlarmInput)(nil)).Elem(), &Alarm{})
	pulumi.RegisterOutputType(AlarmOutput{})
}
