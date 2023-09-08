// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package devopsguru

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// This resource schema represents the ResourceCollection resource in the Amazon DevOps Guru.
func LookupResourceCollection(ctx *pulumi.Context, args *LookupResourceCollectionArgs, opts ...pulumi.InvokeOption) (*LookupResourceCollectionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupResourceCollectionResult
	err := ctx.Invoke("aws-native:devopsguru:getResourceCollection", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupResourceCollectionArgs struct {
	// The type of ResourceCollection
	ResourceCollectionType ResourceCollectionType `pulumi:"resourceCollectionType"`
}

type LookupResourceCollectionResult struct {
	ResourceCollectionFilter *ResourceCollectionFilter `pulumi:"resourceCollectionFilter"`
	// The type of ResourceCollection
	ResourceCollectionType *ResourceCollectionType `pulumi:"resourceCollectionType"`
}

func LookupResourceCollectionOutput(ctx *pulumi.Context, args LookupResourceCollectionOutputArgs, opts ...pulumi.InvokeOption) LookupResourceCollectionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupResourceCollectionResult, error) {
			args := v.(LookupResourceCollectionArgs)
			r, err := LookupResourceCollection(ctx, &args, opts...)
			var s LookupResourceCollectionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupResourceCollectionResultOutput)
}

type LookupResourceCollectionOutputArgs struct {
	// The type of ResourceCollection
	ResourceCollectionType ResourceCollectionTypeInput `pulumi:"resourceCollectionType"`
}

func (LookupResourceCollectionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResourceCollectionArgs)(nil)).Elem()
}

type LookupResourceCollectionResultOutput struct{ *pulumi.OutputState }

func (LookupResourceCollectionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResourceCollectionResult)(nil)).Elem()
}

func (o LookupResourceCollectionResultOutput) ToLookupResourceCollectionResultOutput() LookupResourceCollectionResultOutput {
	return o
}

func (o LookupResourceCollectionResultOutput) ToLookupResourceCollectionResultOutputWithContext(ctx context.Context) LookupResourceCollectionResultOutput {
	return o
}

func (o LookupResourceCollectionResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupResourceCollectionResult] {
	return pulumix.Output[LookupResourceCollectionResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupResourceCollectionResultOutput) ResourceCollectionFilter() ResourceCollectionFilterPtrOutput {
	return o.ApplyT(func(v LookupResourceCollectionResult) *ResourceCollectionFilter { return v.ResourceCollectionFilter }).(ResourceCollectionFilterPtrOutput)
}

// The type of ResourceCollection
func (o LookupResourceCollectionResultOutput) ResourceCollectionType() ResourceCollectionTypePtrOutput {
	return o.ApplyT(func(v LookupResourceCollectionResult) *ResourceCollectionType { return v.ResourceCollectionType }).(ResourceCollectionTypePtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupResourceCollectionResultOutput{})
}
