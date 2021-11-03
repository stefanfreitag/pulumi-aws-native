// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sagemaker

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::SageMaker::MonitoringSchedule
type MonitoringSchedule struct {
	pulumi.CustomResourceState

	// The time at which the schedule was created.
	CreationTime pulumi.StringOutput    `pulumi:"creationTime"`
	EndpointName pulumi.StringPtrOutput `pulumi:"endpointName"`
	// Contains the reason a monitoring job failed, if it failed.
	FailureReason pulumi.StringPtrOutput `pulumi:"failureReason"`
	// A timestamp that indicates the last time the monitoring job was modified.
	LastModifiedTime pulumi.StringOutput `pulumi:"lastModifiedTime"`
	// Describes metadata on the last execution to run, if there was one.
	LastMonitoringExecutionSummary MonitoringScheduleMonitoringExecutionSummaryPtrOutput `pulumi:"lastMonitoringExecutionSummary"`
	// The Amazon Resource Name (ARN) of the monitoring schedule.
	MonitoringScheduleArn    pulumi.StringOutput            `pulumi:"monitoringScheduleArn"`
	MonitoringScheduleConfig MonitoringScheduleConfigOutput `pulumi:"monitoringScheduleConfig"`
	MonitoringScheduleName   pulumi.StringOutput            `pulumi:"monitoringScheduleName"`
	// The status of a schedule job.
	MonitoringScheduleStatus MonitoringScheduleStatusPtrOutput `pulumi:"monitoringScheduleStatus"`
	// An array of key-value pairs to apply to this resource.
	Tags MonitoringScheduleTagArrayOutput `pulumi:"tags"`
}

// NewMonitoringSchedule registers a new resource with the given unique name, arguments, and options.
func NewMonitoringSchedule(ctx *pulumi.Context,
	name string, args *MonitoringScheduleArgs, opts ...pulumi.ResourceOption) (*MonitoringSchedule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.MonitoringScheduleConfig == nil {
		return nil, errors.New("invalid value for required argument 'MonitoringScheduleConfig'")
	}
	if args.MonitoringScheduleName == nil {
		return nil, errors.New("invalid value for required argument 'MonitoringScheduleName'")
	}
	var resource MonitoringSchedule
	err := ctx.RegisterResource("aws-native:sagemaker:MonitoringSchedule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMonitoringSchedule gets an existing MonitoringSchedule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMonitoringSchedule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MonitoringScheduleState, opts ...pulumi.ResourceOption) (*MonitoringSchedule, error) {
	var resource MonitoringSchedule
	err := ctx.ReadResource("aws-native:sagemaker:MonitoringSchedule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MonitoringSchedule resources.
type monitoringScheduleState struct {
}

type MonitoringScheduleState struct {
}

func (MonitoringScheduleState) ElementType() reflect.Type {
	return reflect.TypeOf((*monitoringScheduleState)(nil)).Elem()
}

type monitoringScheduleArgs struct {
	EndpointName *string `pulumi:"endpointName"`
	// Contains the reason a monitoring job failed, if it failed.
	FailureReason *string `pulumi:"failureReason"`
	// Describes metadata on the last execution to run, if there was one.
	LastMonitoringExecutionSummary *MonitoringScheduleMonitoringExecutionSummary `pulumi:"lastMonitoringExecutionSummary"`
	MonitoringScheduleConfig       MonitoringScheduleConfig                      `pulumi:"monitoringScheduleConfig"`
	MonitoringScheduleName         string                                        `pulumi:"monitoringScheduleName"`
	// The status of a schedule job.
	MonitoringScheduleStatus *MonitoringScheduleStatus `pulumi:"monitoringScheduleStatus"`
	// An array of key-value pairs to apply to this resource.
	Tags []MonitoringScheduleTag `pulumi:"tags"`
}

// The set of arguments for constructing a MonitoringSchedule resource.
type MonitoringScheduleArgs struct {
	EndpointName pulumi.StringPtrInput
	// Contains the reason a monitoring job failed, if it failed.
	FailureReason pulumi.StringPtrInput
	// Describes metadata on the last execution to run, if there was one.
	LastMonitoringExecutionSummary MonitoringScheduleMonitoringExecutionSummaryPtrInput
	MonitoringScheduleConfig       MonitoringScheduleConfigInput
	MonitoringScheduleName         pulumi.StringInput
	// The status of a schedule job.
	MonitoringScheduleStatus MonitoringScheduleStatusPtrInput
	// An array of key-value pairs to apply to this resource.
	Tags MonitoringScheduleTagArrayInput
}

func (MonitoringScheduleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*monitoringScheduleArgs)(nil)).Elem()
}

type MonitoringScheduleInput interface {
	pulumi.Input

	ToMonitoringScheduleOutput() MonitoringScheduleOutput
	ToMonitoringScheduleOutputWithContext(ctx context.Context) MonitoringScheduleOutput
}

func (*MonitoringSchedule) ElementType() reflect.Type {
	return reflect.TypeOf((*MonitoringSchedule)(nil))
}

func (i *MonitoringSchedule) ToMonitoringScheduleOutput() MonitoringScheduleOutput {
	return i.ToMonitoringScheduleOutputWithContext(context.Background())
}

func (i *MonitoringSchedule) ToMonitoringScheduleOutputWithContext(ctx context.Context) MonitoringScheduleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MonitoringScheduleOutput)
}

type MonitoringScheduleOutput struct{ *pulumi.OutputState }

func (MonitoringScheduleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*MonitoringSchedule)(nil))
}

func (o MonitoringScheduleOutput) ToMonitoringScheduleOutput() MonitoringScheduleOutput {
	return o
}

func (o MonitoringScheduleOutput) ToMonitoringScheduleOutputWithContext(ctx context.Context) MonitoringScheduleOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*MonitoringScheduleInput)(nil)).Elem(), &MonitoringSchedule{})
	pulumi.RegisterOutputType(MonitoringScheduleOutput{})
}
