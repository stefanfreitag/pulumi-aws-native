// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package evidently

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Evidently::Project
func LookupProject(ctx *pulumi.Context, args *LookupProjectArgs, opts ...pulumi.InvokeOption) (*LookupProjectResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupProjectResult
	err := ctx.Invoke("aws-native:evidently:getProject", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupProjectArgs struct {
	Arn string `pulumi:"arn"`
}

type LookupProjectResult struct {
	AppConfigResource *ProjectAppConfigResourceObject `pulumi:"appConfigResource"`
	Arn               *string                         `pulumi:"arn"`
	DataDelivery      *ProjectDataDeliveryObject      `pulumi:"dataDelivery"`
	Description       *string                         `pulumi:"description"`
	// An array of key-value pairs to apply to this resource.
	Tags []ProjectTag `pulumi:"tags"`
}

func LookupProjectOutput(ctx *pulumi.Context, args LookupProjectOutputArgs, opts ...pulumi.InvokeOption) LookupProjectResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupProjectResult, error) {
			args := v.(LookupProjectArgs)
			r, err := LookupProject(ctx, &args, opts...)
			var s LookupProjectResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupProjectResultOutput)
}

type LookupProjectOutputArgs struct {
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupProjectOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupProjectArgs)(nil)).Elem()
}

type LookupProjectResultOutput struct{ *pulumi.OutputState }

func (LookupProjectResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupProjectResult)(nil)).Elem()
}

func (o LookupProjectResultOutput) ToLookupProjectResultOutput() LookupProjectResultOutput {
	return o
}

func (o LookupProjectResultOutput) ToLookupProjectResultOutputWithContext(ctx context.Context) LookupProjectResultOutput {
	return o
}

func (o LookupProjectResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupProjectResult] {
	return pulumix.Output[LookupProjectResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupProjectResultOutput) AppConfigResource() ProjectAppConfigResourceObjectPtrOutput {
	return o.ApplyT(func(v LookupProjectResult) *ProjectAppConfigResourceObject { return v.AppConfigResource }).(ProjectAppConfigResourceObjectPtrOutput)
}

func (o LookupProjectResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProjectResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupProjectResultOutput) DataDelivery() ProjectDataDeliveryObjectPtrOutput {
	return o.ApplyT(func(v LookupProjectResult) *ProjectDataDeliveryObject { return v.DataDelivery }).(ProjectDataDeliveryObjectPtrOutput)
}

func (o LookupProjectResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProjectResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupProjectResultOutput) Tags() ProjectTagArrayOutput {
	return o.ApplyT(func(v LookupProjectResult) []ProjectTag { return v.Tags }).(ProjectTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupProjectResultOutput{})
}
