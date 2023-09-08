// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package route53

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Route53::RecordSet
func LookupRecordSet(ctx *pulumi.Context, args *LookupRecordSetArgs, opts ...pulumi.InvokeOption) (*LookupRecordSetResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupRecordSetResult
	err := ctx.Invoke("aws-native:route53:getRecordSet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupRecordSetArgs struct {
	Id string `pulumi:"id"`
}

type LookupRecordSetResult struct {
	AliasTarget       *RecordSetAliasTarget       `pulumi:"aliasTarget"`
	CidrRoutingConfig *RecordSetCidrRoutingConfig `pulumi:"cidrRoutingConfig"`
	Comment           *string                     `pulumi:"comment"`
	Failover          *string                     `pulumi:"failover"`
	GeoLocation       *RecordSetGeoLocation       `pulumi:"geoLocation"`
	HealthCheckId     *string                     `pulumi:"healthCheckId"`
	Id                *string                     `pulumi:"id"`
	MultiValueAnswer  *bool                       `pulumi:"multiValueAnswer"`
	Region            *string                     `pulumi:"region"`
	ResourceRecords   []string                    `pulumi:"resourceRecords"`
	SetIdentifier     *string                     `pulumi:"setIdentifier"`
	Ttl               *string                     `pulumi:"ttl"`
	Type              *string                     `pulumi:"type"`
	Weight            *int                        `pulumi:"weight"`
}

func LookupRecordSetOutput(ctx *pulumi.Context, args LookupRecordSetOutputArgs, opts ...pulumi.InvokeOption) LookupRecordSetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupRecordSetResult, error) {
			args := v.(LookupRecordSetArgs)
			r, err := LookupRecordSet(ctx, &args, opts...)
			var s LookupRecordSetResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupRecordSetResultOutput)
}

type LookupRecordSetOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupRecordSetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRecordSetArgs)(nil)).Elem()
}

type LookupRecordSetResultOutput struct{ *pulumi.OutputState }

func (LookupRecordSetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRecordSetResult)(nil)).Elem()
}

func (o LookupRecordSetResultOutput) ToLookupRecordSetResultOutput() LookupRecordSetResultOutput {
	return o
}

func (o LookupRecordSetResultOutput) ToLookupRecordSetResultOutputWithContext(ctx context.Context) LookupRecordSetResultOutput {
	return o
}

func (o LookupRecordSetResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupRecordSetResult] {
	return pulumix.Output[LookupRecordSetResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupRecordSetResultOutput) AliasTarget() RecordSetAliasTargetPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *RecordSetAliasTarget { return v.AliasTarget }).(RecordSetAliasTargetPtrOutput)
}

func (o LookupRecordSetResultOutput) CidrRoutingConfig() RecordSetCidrRoutingConfigPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *RecordSetCidrRoutingConfig { return v.CidrRoutingConfig }).(RecordSetCidrRoutingConfigPtrOutput)
}

func (o LookupRecordSetResultOutput) Comment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *string { return v.Comment }).(pulumi.StringPtrOutput)
}

func (o LookupRecordSetResultOutput) Failover() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *string { return v.Failover }).(pulumi.StringPtrOutput)
}

func (o LookupRecordSetResultOutput) GeoLocation() RecordSetGeoLocationPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *RecordSetGeoLocation { return v.GeoLocation }).(RecordSetGeoLocationPtrOutput)
}

func (o LookupRecordSetResultOutput) HealthCheckId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *string { return v.HealthCheckId }).(pulumi.StringPtrOutput)
}

func (o LookupRecordSetResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupRecordSetResultOutput) MultiValueAnswer() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *bool { return v.MultiValueAnswer }).(pulumi.BoolPtrOutput)
}

func (o LookupRecordSetResultOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *string { return v.Region }).(pulumi.StringPtrOutput)
}

func (o LookupRecordSetResultOutput) ResourceRecords() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupRecordSetResult) []string { return v.ResourceRecords }).(pulumi.StringArrayOutput)
}

func (o LookupRecordSetResultOutput) SetIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *string { return v.SetIdentifier }).(pulumi.StringPtrOutput)
}

func (o LookupRecordSetResultOutput) Ttl() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *string { return v.Ttl }).(pulumi.StringPtrOutput)
}

func (o LookupRecordSetResultOutput) Type() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *string { return v.Type }).(pulumi.StringPtrOutput)
}

func (o LookupRecordSetResultOutput) Weight() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupRecordSetResult) *int { return v.Weight }).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupRecordSetResultOutput{})
}
