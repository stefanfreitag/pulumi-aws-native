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

// Create and manage FUOTA tasks.
func LookupFuotaTask(ctx *pulumi.Context, args *LookupFuotaTaskArgs, opts ...pulumi.InvokeOption) (*LookupFuotaTaskResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupFuotaTaskResult
	err := ctx.Invoke("aws-native:iotwireless:getFuotaTask", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupFuotaTaskArgs struct {
	// FUOTA task id. Returned after successful create.
	Id string `pulumi:"id"`
}

type LookupFuotaTaskResult struct {
	// FUOTA task arn. Returned after successful create.
	Arn *string `pulumi:"arn"`
	// Multicast group to associate. Only for update request.
	AssociateMulticastGroup *string `pulumi:"associateMulticastGroup"`
	// Wireless device to associate. Only for update request.
	AssociateWirelessDevice *string `pulumi:"associateWirelessDevice"`
	// FUOTA task description
	Description *string `pulumi:"description"`
	// Multicast group to disassociate. Only for update request.
	DisassociateMulticastGroup *string `pulumi:"disassociateMulticastGroup"`
	// Wireless device to disassociate. Only for update request.
	DisassociateWirelessDevice *string `pulumi:"disassociateWirelessDevice"`
	// FUOTA task firmware update image binary S3 link
	FirmwareUpdateImage *string `pulumi:"firmwareUpdateImage"`
	// FUOTA task firmware IAM role for reading S3
	FirmwareUpdateRole *string `pulumi:"firmwareUpdateRole"`
	// FUOTA task status. Returned after successful read.
	FuotaTaskStatus *string `pulumi:"fuotaTaskStatus"`
	// FUOTA task id. Returned after successful create.
	Id *string `pulumi:"id"`
	// FUOTA task LoRaWAN
	LoRaWan *FuotaTaskLoRaWan `pulumi:"loRaWan"`
	// Name of FUOTA task
	Name *string `pulumi:"name"`
	// A list of key-value pairs that contain metadata for the FUOTA task.
	Tags []FuotaTaskTag `pulumi:"tags"`
}

func LookupFuotaTaskOutput(ctx *pulumi.Context, args LookupFuotaTaskOutputArgs, opts ...pulumi.InvokeOption) LookupFuotaTaskResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupFuotaTaskResult, error) {
			args := v.(LookupFuotaTaskArgs)
			r, err := LookupFuotaTask(ctx, &args, opts...)
			var s LookupFuotaTaskResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupFuotaTaskResultOutput)
}

type LookupFuotaTaskOutputArgs struct {
	// FUOTA task id. Returned after successful create.
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupFuotaTaskOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFuotaTaskArgs)(nil)).Elem()
}

type LookupFuotaTaskResultOutput struct{ *pulumi.OutputState }

func (LookupFuotaTaskResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupFuotaTaskResult)(nil)).Elem()
}

func (o LookupFuotaTaskResultOutput) ToLookupFuotaTaskResultOutput() LookupFuotaTaskResultOutput {
	return o
}

func (o LookupFuotaTaskResultOutput) ToLookupFuotaTaskResultOutputWithContext(ctx context.Context) LookupFuotaTaskResultOutput {
	return o
}

func (o LookupFuotaTaskResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupFuotaTaskResult] {
	return pulumix.Output[LookupFuotaTaskResult]{
		OutputState: o.OutputState,
	}
}

// FUOTA task arn. Returned after successful create.
func (o LookupFuotaTaskResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// Multicast group to associate. Only for update request.
func (o LookupFuotaTaskResultOutput) AssociateMulticastGroup() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) *string { return v.AssociateMulticastGroup }).(pulumi.StringPtrOutput)
}

// Wireless device to associate. Only for update request.
func (o LookupFuotaTaskResultOutput) AssociateWirelessDevice() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) *string { return v.AssociateWirelessDevice }).(pulumi.StringPtrOutput)
}

// FUOTA task description
func (o LookupFuotaTaskResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Multicast group to disassociate. Only for update request.
func (o LookupFuotaTaskResultOutput) DisassociateMulticastGroup() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) *string { return v.DisassociateMulticastGroup }).(pulumi.StringPtrOutput)
}

// Wireless device to disassociate. Only for update request.
func (o LookupFuotaTaskResultOutput) DisassociateWirelessDevice() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) *string { return v.DisassociateWirelessDevice }).(pulumi.StringPtrOutput)
}

// FUOTA task firmware update image binary S3 link
func (o LookupFuotaTaskResultOutput) FirmwareUpdateImage() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) *string { return v.FirmwareUpdateImage }).(pulumi.StringPtrOutput)
}

// FUOTA task firmware IAM role for reading S3
func (o LookupFuotaTaskResultOutput) FirmwareUpdateRole() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) *string { return v.FirmwareUpdateRole }).(pulumi.StringPtrOutput)
}

// FUOTA task status. Returned after successful read.
func (o LookupFuotaTaskResultOutput) FuotaTaskStatus() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) *string { return v.FuotaTaskStatus }).(pulumi.StringPtrOutput)
}

// FUOTA task id. Returned after successful create.
func (o LookupFuotaTaskResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// FUOTA task LoRaWAN
func (o LookupFuotaTaskResultOutput) LoRaWan() FuotaTaskLoRaWanPtrOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) *FuotaTaskLoRaWan { return v.LoRaWan }).(FuotaTaskLoRaWanPtrOutput)
}

// Name of FUOTA task
func (o LookupFuotaTaskResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// A list of key-value pairs that contain metadata for the FUOTA task.
func (o LookupFuotaTaskResultOutput) Tags() FuotaTaskTagArrayOutput {
	return o.ApplyT(func(v LookupFuotaTaskResult) []FuotaTaskTag { return v.Tags }).(FuotaTaskTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupFuotaTaskResultOutput{})
}
