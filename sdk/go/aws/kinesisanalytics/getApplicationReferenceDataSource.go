// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kinesisanalytics

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::KinesisAnalytics::ApplicationReferenceDataSource
func LookupApplicationReferenceDataSource(ctx *pulumi.Context, args *LookupApplicationReferenceDataSourceArgs, opts ...pulumi.InvokeOption) (*LookupApplicationReferenceDataSourceResult, error) {
	var rv LookupApplicationReferenceDataSourceResult
	err := ctx.Invoke("aws-native:kinesisanalytics:getApplicationReferenceDataSource", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupApplicationReferenceDataSourceArgs struct {
	Id string `pulumi:"id"`
}

type LookupApplicationReferenceDataSourceResult struct {
	Id                  *string                                            `pulumi:"id"`
	ReferenceDataSource *ApplicationReferenceDataSourceReferenceDataSource `pulumi:"referenceDataSource"`
}

func LookupApplicationReferenceDataSourceOutput(ctx *pulumi.Context, args LookupApplicationReferenceDataSourceOutputArgs, opts ...pulumi.InvokeOption) LookupApplicationReferenceDataSourceResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupApplicationReferenceDataSourceResult, error) {
			args := v.(LookupApplicationReferenceDataSourceArgs)
			r, err := LookupApplicationReferenceDataSource(ctx, &args, opts...)
			var s LookupApplicationReferenceDataSourceResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupApplicationReferenceDataSourceResultOutput)
}

type LookupApplicationReferenceDataSourceOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupApplicationReferenceDataSourceOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApplicationReferenceDataSourceArgs)(nil)).Elem()
}

type LookupApplicationReferenceDataSourceResultOutput struct{ *pulumi.OutputState }

func (LookupApplicationReferenceDataSourceResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApplicationReferenceDataSourceResult)(nil)).Elem()
}

func (o LookupApplicationReferenceDataSourceResultOutput) ToLookupApplicationReferenceDataSourceResultOutput() LookupApplicationReferenceDataSourceResultOutput {
	return o
}

func (o LookupApplicationReferenceDataSourceResultOutput) ToLookupApplicationReferenceDataSourceResultOutputWithContext(ctx context.Context) LookupApplicationReferenceDataSourceResultOutput {
	return o
}

func (o LookupApplicationReferenceDataSourceResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationReferenceDataSourceResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupApplicationReferenceDataSourceResultOutput) ReferenceDataSource() ApplicationReferenceDataSourceReferenceDataSourcePtrOutput {
	return o.ApplyT(func(v LookupApplicationReferenceDataSourceResult) *ApplicationReferenceDataSourceReferenceDataSource {
		return v.ReferenceDataSource
	}).(ApplicationReferenceDataSourceReferenceDataSourcePtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupApplicationReferenceDataSourceResultOutput{})
}
