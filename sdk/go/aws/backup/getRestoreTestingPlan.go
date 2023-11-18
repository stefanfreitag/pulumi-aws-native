// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package backup

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::Backup::RestoreTestingPlan Resource Type
func LookupRestoreTestingPlan(ctx *pulumi.Context, args *LookupRestoreTestingPlanArgs, opts ...pulumi.InvokeOption) (*LookupRestoreTestingPlanResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupRestoreTestingPlanResult
	err := ctx.Invoke("aws-native:backup:getRestoreTestingPlan", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupRestoreTestingPlanArgs struct {
	RestoreTestingPlanName string `pulumi:"restoreTestingPlanName"`
}

type LookupRestoreTestingPlanResult struct {
	RecoveryPointSelection     *RestoreTestingPlanRestoreTestingRecoveryPointSelection `pulumi:"recoveryPointSelection"`
	RestoreTestingPlanArn      *string                                                 `pulumi:"restoreTestingPlanArn"`
	ScheduleExpression         *string                                                 `pulumi:"scheduleExpression"`
	ScheduleExpressionTimezone *string                                                 `pulumi:"scheduleExpressionTimezone"`
	StartWindowHours           *int                                                    `pulumi:"startWindowHours"`
	Tags                       []RestoreTestingPlanTag                                 `pulumi:"tags"`
}

func LookupRestoreTestingPlanOutput(ctx *pulumi.Context, args LookupRestoreTestingPlanOutputArgs, opts ...pulumi.InvokeOption) LookupRestoreTestingPlanResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupRestoreTestingPlanResult, error) {
			args := v.(LookupRestoreTestingPlanArgs)
			r, err := LookupRestoreTestingPlan(ctx, &args, opts...)
			var s LookupRestoreTestingPlanResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupRestoreTestingPlanResultOutput)
}

type LookupRestoreTestingPlanOutputArgs struct {
	RestoreTestingPlanName pulumi.StringInput `pulumi:"restoreTestingPlanName"`
}

func (LookupRestoreTestingPlanOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRestoreTestingPlanArgs)(nil)).Elem()
}

type LookupRestoreTestingPlanResultOutput struct{ *pulumi.OutputState }

func (LookupRestoreTestingPlanResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRestoreTestingPlanResult)(nil)).Elem()
}

func (o LookupRestoreTestingPlanResultOutput) ToLookupRestoreTestingPlanResultOutput() LookupRestoreTestingPlanResultOutput {
	return o
}

func (o LookupRestoreTestingPlanResultOutput) ToLookupRestoreTestingPlanResultOutputWithContext(ctx context.Context) LookupRestoreTestingPlanResultOutput {
	return o
}

func (o LookupRestoreTestingPlanResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupRestoreTestingPlanResult] {
	return pulumix.Output[LookupRestoreTestingPlanResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupRestoreTestingPlanResultOutput) RecoveryPointSelection() RestoreTestingPlanRestoreTestingRecoveryPointSelectionPtrOutput {
	return o.ApplyT(func(v LookupRestoreTestingPlanResult) *RestoreTestingPlanRestoreTestingRecoveryPointSelection {
		return v.RecoveryPointSelection
	}).(RestoreTestingPlanRestoreTestingRecoveryPointSelectionPtrOutput)
}

func (o LookupRestoreTestingPlanResultOutput) RestoreTestingPlanArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRestoreTestingPlanResult) *string { return v.RestoreTestingPlanArn }).(pulumi.StringPtrOutput)
}

func (o LookupRestoreTestingPlanResultOutput) ScheduleExpression() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRestoreTestingPlanResult) *string { return v.ScheduleExpression }).(pulumi.StringPtrOutput)
}

func (o LookupRestoreTestingPlanResultOutput) ScheduleExpressionTimezone() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRestoreTestingPlanResult) *string { return v.ScheduleExpressionTimezone }).(pulumi.StringPtrOutput)
}

func (o LookupRestoreTestingPlanResultOutput) StartWindowHours() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupRestoreTestingPlanResult) *int { return v.StartWindowHours }).(pulumi.IntPtrOutput)
}

func (o LookupRestoreTestingPlanResultOutput) Tags() RestoreTestingPlanTagArrayOutput {
	return o.ApplyT(func(v LookupRestoreTestingPlanResult) []RestoreTestingPlanTag { return v.Tags }).(RestoreTestingPlanTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupRestoreTestingPlanResultOutput{})
}
