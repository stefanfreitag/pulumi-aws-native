// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package athena

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::Athena::CapacityReservation
func LookupCapacityReservation(ctx *pulumi.Context, args *LookupCapacityReservationArgs, opts ...pulumi.InvokeOption) (*LookupCapacityReservationResult, error) {
	var rv LookupCapacityReservationResult
	err := ctx.Invoke("aws-native:athena:getCapacityReservation", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupCapacityReservationArgs struct {
	Arn string `pulumi:"arn"`
}

type LookupCapacityReservationResult struct {
	// The number of DPUs Athena has provisioned and allocated for the reservation
	AllocatedDpus                   *int                                                `pulumi:"allocatedDpus"`
	Arn                             *string                                             `pulumi:"arn"`
	CapacityAssignmentConfiguration *CapacityReservationCapacityAssignmentConfiguration `pulumi:"capacityAssignmentConfiguration"`
	// The date and time the reservation was created.
	CreationTime *string `pulumi:"creationTime"`
	// The timestamp when the last successful allocated was made
	LastSuccessfulAllocationTime *string `pulumi:"lastSuccessfulAllocationTime"`
	// The status of the reservation.
	Status *CapacityReservationStatus `pulumi:"status"`
	// An array of key-value pairs to apply to this resource.
	Tags []CapacityReservationTag `pulumi:"tags"`
	// The number of DPUs to request to be allocated to the reservation.
	TargetDpus *int `pulumi:"targetDpus"`
}

func LookupCapacityReservationOutput(ctx *pulumi.Context, args LookupCapacityReservationOutputArgs, opts ...pulumi.InvokeOption) LookupCapacityReservationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCapacityReservationResult, error) {
			args := v.(LookupCapacityReservationArgs)
			r, err := LookupCapacityReservation(ctx, &args, opts...)
			var s LookupCapacityReservationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCapacityReservationResultOutput)
}

type LookupCapacityReservationOutputArgs struct {
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupCapacityReservationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCapacityReservationArgs)(nil)).Elem()
}

type LookupCapacityReservationResultOutput struct{ *pulumi.OutputState }

func (LookupCapacityReservationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCapacityReservationResult)(nil)).Elem()
}

func (o LookupCapacityReservationResultOutput) ToLookupCapacityReservationResultOutput() LookupCapacityReservationResultOutput {
	return o
}

func (o LookupCapacityReservationResultOutput) ToLookupCapacityReservationResultOutputWithContext(ctx context.Context) LookupCapacityReservationResultOutput {
	return o
}

// The number of DPUs Athena has provisioned and allocated for the reservation
func (o LookupCapacityReservationResultOutput) AllocatedDpus() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupCapacityReservationResult) *int { return v.AllocatedDpus }).(pulumi.IntPtrOutput)
}

func (o LookupCapacityReservationResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCapacityReservationResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupCapacityReservationResultOutput) CapacityAssignmentConfiguration() CapacityReservationCapacityAssignmentConfigurationPtrOutput {
	return o.ApplyT(func(v LookupCapacityReservationResult) *CapacityReservationCapacityAssignmentConfiguration {
		return v.CapacityAssignmentConfiguration
	}).(CapacityReservationCapacityAssignmentConfigurationPtrOutput)
}

// The date and time the reservation was created.
func (o LookupCapacityReservationResultOutput) CreationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCapacityReservationResult) *string { return v.CreationTime }).(pulumi.StringPtrOutput)
}

// The timestamp when the last successful allocated was made
func (o LookupCapacityReservationResultOutput) LastSuccessfulAllocationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCapacityReservationResult) *string { return v.LastSuccessfulAllocationTime }).(pulumi.StringPtrOutput)
}

// The status of the reservation.
func (o LookupCapacityReservationResultOutput) Status() CapacityReservationStatusPtrOutput {
	return o.ApplyT(func(v LookupCapacityReservationResult) *CapacityReservationStatus { return v.Status }).(CapacityReservationStatusPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupCapacityReservationResultOutput) Tags() CapacityReservationTagArrayOutput {
	return o.ApplyT(func(v LookupCapacityReservationResult) []CapacityReservationTag { return v.Tags }).(CapacityReservationTagArrayOutput)
}

// The number of DPUs to request to be allocated to the reservation.
func (o LookupCapacityReservationResultOutput) TargetDpus() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupCapacityReservationResult) *int { return v.TargetDpus }).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCapacityReservationResultOutput{})
}
