// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iotwireless

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Wireless Device Import Tasks
func LookupWirelessDeviceImportTask(ctx *pulumi.Context, args *LookupWirelessDeviceImportTaskArgs, opts ...pulumi.InvokeOption) (*LookupWirelessDeviceImportTaskResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupWirelessDeviceImportTaskResult
	err := ctx.Invoke("aws-native:iotwireless:getWirelessDeviceImportTask", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupWirelessDeviceImportTaskArgs struct {
	// Id for Wireless Device Import Task, Returned upon successful start.
	Id string `pulumi:"id"`
}

type LookupWirelessDeviceImportTaskResult struct {
	// Arn for Wireless Device Import Task, Returned upon successful start.
	Arn *string `pulumi:"arn"`
	// CreationDate for import task
	CreationDate *string `pulumi:"creationDate"`
	// Destination Name for import task
	DestinationName *string `pulumi:"destinationName"`
	// Failed Imported Devices Count
	FailedImportedDevicesCount *int `pulumi:"failedImportedDevicesCount"`
	// Id for Wireless Device Import Task, Returned upon successful start.
	Id *string `pulumi:"id"`
	// Initialized Imported Devices Count
	InitializedImportedDevicesCount *int `pulumi:"initializedImportedDevicesCount"`
	// Onboarded Imported Devices Count
	OnboardedImportedDevicesCount *int `pulumi:"onboardedImportedDevicesCount"`
	// Pending Imported Devices Count
	PendingImportedDevicesCount *int `pulumi:"pendingImportedDevicesCount"`
	// sidewalk contain file for created device and role
	Sidewalk *SidewalkProperties `pulumi:"sidewalk"`
	// Status for import task
	Status *WirelessDeviceImportTaskStatus `pulumi:"status"`
	// StatusReason for import task
	StatusReason *string `pulumi:"statusReason"`
	// An array of key-value pairs to apply to this resource.
	Tags []WirelessDeviceImportTaskTag `pulumi:"tags"`
}

func LookupWirelessDeviceImportTaskOutput(ctx *pulumi.Context, args LookupWirelessDeviceImportTaskOutputArgs, opts ...pulumi.InvokeOption) LookupWirelessDeviceImportTaskResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupWirelessDeviceImportTaskResult, error) {
			args := v.(LookupWirelessDeviceImportTaskArgs)
			r, err := LookupWirelessDeviceImportTask(ctx, &args, opts...)
			var s LookupWirelessDeviceImportTaskResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupWirelessDeviceImportTaskResultOutput)
}

type LookupWirelessDeviceImportTaskOutputArgs struct {
	// Id for Wireless Device Import Task, Returned upon successful start.
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupWirelessDeviceImportTaskOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWirelessDeviceImportTaskArgs)(nil)).Elem()
}

type LookupWirelessDeviceImportTaskResultOutput struct{ *pulumi.OutputState }

func (LookupWirelessDeviceImportTaskResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupWirelessDeviceImportTaskResult)(nil)).Elem()
}

func (o LookupWirelessDeviceImportTaskResultOutput) ToLookupWirelessDeviceImportTaskResultOutput() LookupWirelessDeviceImportTaskResultOutput {
	return o
}

func (o LookupWirelessDeviceImportTaskResultOutput) ToLookupWirelessDeviceImportTaskResultOutputWithContext(ctx context.Context) LookupWirelessDeviceImportTaskResultOutput {
	return o
}

func (o LookupWirelessDeviceImportTaskResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupWirelessDeviceImportTaskResult] {
	return pulumix.Output[LookupWirelessDeviceImportTaskResult]{
		OutputState: o.OutputState,
	}
}

// Arn for Wireless Device Import Task, Returned upon successful start.
func (o LookupWirelessDeviceImportTaskResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessDeviceImportTaskResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// CreationDate for import task
func (o LookupWirelessDeviceImportTaskResultOutput) CreationDate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessDeviceImportTaskResult) *string { return v.CreationDate }).(pulumi.StringPtrOutput)
}

// Destination Name for import task
func (o LookupWirelessDeviceImportTaskResultOutput) DestinationName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessDeviceImportTaskResult) *string { return v.DestinationName }).(pulumi.StringPtrOutput)
}

// Failed Imported Devices Count
func (o LookupWirelessDeviceImportTaskResultOutput) FailedImportedDevicesCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupWirelessDeviceImportTaskResult) *int { return v.FailedImportedDevicesCount }).(pulumi.IntPtrOutput)
}

// Id for Wireless Device Import Task, Returned upon successful start.
func (o LookupWirelessDeviceImportTaskResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessDeviceImportTaskResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Initialized Imported Devices Count
func (o LookupWirelessDeviceImportTaskResultOutput) InitializedImportedDevicesCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupWirelessDeviceImportTaskResult) *int { return v.InitializedImportedDevicesCount }).(pulumi.IntPtrOutput)
}

// Onboarded Imported Devices Count
func (o LookupWirelessDeviceImportTaskResultOutput) OnboardedImportedDevicesCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupWirelessDeviceImportTaskResult) *int { return v.OnboardedImportedDevicesCount }).(pulumi.IntPtrOutput)
}

// Pending Imported Devices Count
func (o LookupWirelessDeviceImportTaskResultOutput) PendingImportedDevicesCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupWirelessDeviceImportTaskResult) *int { return v.PendingImportedDevicesCount }).(pulumi.IntPtrOutput)
}

// sidewalk contain file for created device and role
func (o LookupWirelessDeviceImportTaskResultOutput) Sidewalk() SidewalkPropertiesPtrOutput {
	return o.ApplyT(func(v LookupWirelessDeviceImportTaskResult) *SidewalkProperties { return v.Sidewalk }).(SidewalkPropertiesPtrOutput)
}

// Status for import task
func (o LookupWirelessDeviceImportTaskResultOutput) Status() WirelessDeviceImportTaskStatusPtrOutput {
	return o.ApplyT(func(v LookupWirelessDeviceImportTaskResult) *WirelessDeviceImportTaskStatus { return v.Status }).(WirelessDeviceImportTaskStatusPtrOutput)
}

// StatusReason for import task
func (o LookupWirelessDeviceImportTaskResultOutput) StatusReason() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupWirelessDeviceImportTaskResult) *string { return v.StatusReason }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupWirelessDeviceImportTaskResultOutput) Tags() WirelessDeviceImportTaskTagArrayOutput {
	return o.ApplyT(func(v LookupWirelessDeviceImportTaskResult) []WirelessDeviceImportTaskTag { return v.Tags }).(WirelessDeviceImportTaskTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupWirelessDeviceImportTaskResultOutput{})
}
