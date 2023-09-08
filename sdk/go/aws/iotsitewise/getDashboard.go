// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iotsitewise

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::IoTSiteWise::Dashboard
func LookupDashboard(ctx *pulumi.Context, args *LookupDashboardArgs, opts ...pulumi.InvokeOption) (*LookupDashboardResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDashboardResult
	err := ctx.Invoke("aws-native:iotsitewise:getDashboard", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDashboardArgs struct {
	// The ID of the dashboard.
	DashboardId string `pulumi:"dashboardId"`
}

type LookupDashboardResult struct {
	// The ARN of the dashboard.
	DashboardArn *string `pulumi:"dashboardArn"`
	// The dashboard definition specified in a JSON literal.
	DashboardDefinition *string `pulumi:"dashboardDefinition"`
	// A description for the dashboard.
	DashboardDescription *string `pulumi:"dashboardDescription"`
	// The ID of the dashboard.
	DashboardId *string `pulumi:"dashboardId"`
	// A friendly name for the dashboard.
	DashboardName *string `pulumi:"dashboardName"`
	// A list of key-value pairs that contain metadata for the dashboard.
	Tags []DashboardTag `pulumi:"tags"`
}

func LookupDashboardOutput(ctx *pulumi.Context, args LookupDashboardOutputArgs, opts ...pulumi.InvokeOption) LookupDashboardResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDashboardResult, error) {
			args := v.(LookupDashboardArgs)
			r, err := LookupDashboard(ctx, &args, opts...)
			var s LookupDashboardResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDashboardResultOutput)
}

type LookupDashboardOutputArgs struct {
	// The ID of the dashboard.
	DashboardId pulumi.StringInput `pulumi:"dashboardId"`
}

func (LookupDashboardOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDashboardArgs)(nil)).Elem()
}

type LookupDashboardResultOutput struct{ *pulumi.OutputState }

func (LookupDashboardResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDashboardResult)(nil)).Elem()
}

func (o LookupDashboardResultOutput) ToLookupDashboardResultOutput() LookupDashboardResultOutput {
	return o
}

func (o LookupDashboardResultOutput) ToLookupDashboardResultOutputWithContext(ctx context.Context) LookupDashboardResultOutput {
	return o
}

func (o LookupDashboardResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupDashboardResult] {
	return pulumix.Output[LookupDashboardResult]{
		OutputState: o.OutputState,
	}
}

// The ARN of the dashboard.
func (o LookupDashboardResultOutput) DashboardArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDashboardResult) *string { return v.DashboardArn }).(pulumi.StringPtrOutput)
}

// The dashboard definition specified in a JSON literal.
func (o LookupDashboardResultOutput) DashboardDefinition() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDashboardResult) *string { return v.DashboardDefinition }).(pulumi.StringPtrOutput)
}

// A description for the dashboard.
func (o LookupDashboardResultOutput) DashboardDescription() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDashboardResult) *string { return v.DashboardDescription }).(pulumi.StringPtrOutput)
}

// The ID of the dashboard.
func (o LookupDashboardResultOutput) DashboardId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDashboardResult) *string { return v.DashboardId }).(pulumi.StringPtrOutput)
}

// A friendly name for the dashboard.
func (o LookupDashboardResultOutput) DashboardName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDashboardResult) *string { return v.DashboardName }).(pulumi.StringPtrOutput)
}

// A list of key-value pairs that contain metadata for the dashboard.
func (o LookupDashboardResultOutput) Tags() DashboardTagArrayOutput {
	return o.ApplyT(func(v LookupDashboardResult) []DashboardTag { return v.Tags }).(DashboardTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDashboardResultOutput{})
}
