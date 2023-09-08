// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package internetmonitor

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Represents a monitor, which defines the monitoring boundaries for measurements that Internet Monitor publishes information about for an application
func LookupMonitor(ctx *pulumi.Context, args *LookupMonitorArgs, opts ...pulumi.InvokeOption) (*LookupMonitorResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupMonitorResult
	err := ctx.Invoke("aws-native:internetmonitor:getMonitor", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupMonitorArgs struct {
	MonitorName string `pulumi:"monitorName"`
}

type LookupMonitorResult struct {
	CreatedAt                       *string                                 `pulumi:"createdAt"`
	HealthEventsConfig              *MonitorHealthEventsConfig              `pulumi:"healthEventsConfig"`
	InternetMeasurementsLogDelivery *MonitorInternetMeasurementsLogDelivery `pulumi:"internetMeasurementsLogDelivery"`
	MaxCityNetworksToMonitor        *int                                    `pulumi:"maxCityNetworksToMonitor"`
	ModifiedAt                      *string                                 `pulumi:"modifiedAt"`
	MonitorArn                      *string                                 `pulumi:"monitorArn"`
	ProcessingStatus                *MonitorProcessingStatusCode            `pulumi:"processingStatus"`
	ProcessingStatusInfo            *string                                 `pulumi:"processingStatusInfo"`
	Resources                       []string                                `pulumi:"resources"`
	Status                          *MonitorConfigState                     `pulumi:"status"`
	Tags                            []MonitorTag                            `pulumi:"tags"`
	TrafficPercentageToMonitor      *int                                    `pulumi:"trafficPercentageToMonitor"`
}

func LookupMonitorOutput(ctx *pulumi.Context, args LookupMonitorOutputArgs, opts ...pulumi.InvokeOption) LookupMonitorResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupMonitorResult, error) {
			args := v.(LookupMonitorArgs)
			r, err := LookupMonitor(ctx, &args, opts...)
			var s LookupMonitorResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupMonitorResultOutput)
}

type LookupMonitorOutputArgs struct {
	MonitorName pulumi.StringInput `pulumi:"monitorName"`
}

func (LookupMonitorOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMonitorArgs)(nil)).Elem()
}

type LookupMonitorResultOutput struct{ *pulumi.OutputState }

func (LookupMonitorResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMonitorResult)(nil)).Elem()
}

func (o LookupMonitorResultOutput) ToLookupMonitorResultOutput() LookupMonitorResultOutput {
	return o
}

func (o LookupMonitorResultOutput) ToLookupMonitorResultOutputWithContext(ctx context.Context) LookupMonitorResultOutput {
	return o
}

func (o LookupMonitorResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupMonitorResult] {
	return pulumix.Output[LookupMonitorResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupMonitorResultOutput) CreatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMonitorResult) *string { return v.CreatedAt }).(pulumi.StringPtrOutput)
}

func (o LookupMonitorResultOutput) HealthEventsConfig() MonitorHealthEventsConfigPtrOutput {
	return o.ApplyT(func(v LookupMonitorResult) *MonitorHealthEventsConfig { return v.HealthEventsConfig }).(MonitorHealthEventsConfigPtrOutput)
}

func (o LookupMonitorResultOutput) InternetMeasurementsLogDelivery() MonitorInternetMeasurementsLogDeliveryPtrOutput {
	return o.ApplyT(func(v LookupMonitorResult) *MonitorInternetMeasurementsLogDelivery {
		return v.InternetMeasurementsLogDelivery
	}).(MonitorInternetMeasurementsLogDeliveryPtrOutput)
}

func (o LookupMonitorResultOutput) MaxCityNetworksToMonitor() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupMonitorResult) *int { return v.MaxCityNetworksToMonitor }).(pulumi.IntPtrOutput)
}

func (o LookupMonitorResultOutput) ModifiedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMonitorResult) *string { return v.ModifiedAt }).(pulumi.StringPtrOutput)
}

func (o LookupMonitorResultOutput) MonitorArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMonitorResult) *string { return v.MonitorArn }).(pulumi.StringPtrOutput)
}

func (o LookupMonitorResultOutput) ProcessingStatus() MonitorProcessingStatusCodePtrOutput {
	return o.ApplyT(func(v LookupMonitorResult) *MonitorProcessingStatusCode { return v.ProcessingStatus }).(MonitorProcessingStatusCodePtrOutput)
}

func (o LookupMonitorResultOutput) ProcessingStatusInfo() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMonitorResult) *string { return v.ProcessingStatusInfo }).(pulumi.StringPtrOutput)
}

func (o LookupMonitorResultOutput) Resources() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupMonitorResult) []string { return v.Resources }).(pulumi.StringArrayOutput)
}

func (o LookupMonitorResultOutput) Status() MonitorConfigStatePtrOutput {
	return o.ApplyT(func(v LookupMonitorResult) *MonitorConfigState { return v.Status }).(MonitorConfigStatePtrOutput)
}

func (o LookupMonitorResultOutput) Tags() MonitorTagArrayOutput {
	return o.ApplyT(func(v LookupMonitorResult) []MonitorTag { return v.Tags }).(MonitorTagArrayOutput)
}

func (o LookupMonitorResultOutput) TrafficPercentageToMonitor() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupMonitorResult) *int { return v.TrafficPercentageToMonitor }).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMonitorResultOutput{})
}
