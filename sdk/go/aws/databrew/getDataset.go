// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package databrew

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for AWS::DataBrew::Dataset.
func LookupDataset(ctx *pulumi.Context, args *LookupDatasetArgs, opts ...pulumi.InvokeOption) (*LookupDatasetResult, error) {
	var rv LookupDatasetResult
	err := ctx.Invoke("aws-native:databrew:getDataset", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDatasetArgs struct {
	// Dataset name
	Name string `pulumi:"name"`
}

type LookupDatasetResult struct {
	// Dataset format
	Format *DatasetFormat `pulumi:"format"`
	// Format options for dataset
	FormatOptions *DatasetFormatOptions `pulumi:"formatOptions"`
	// Input
	Input *DatasetInputType `pulumi:"input"`
	// PathOptions
	PathOptions *DatasetPathOptions `pulumi:"pathOptions"`
}

func LookupDatasetOutput(ctx *pulumi.Context, args LookupDatasetOutputArgs, opts ...pulumi.InvokeOption) LookupDatasetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDatasetResult, error) {
			args := v.(LookupDatasetArgs)
			r, err := LookupDataset(ctx, &args, opts...)
			var s LookupDatasetResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDatasetResultOutput)
}

type LookupDatasetOutputArgs struct {
	// Dataset name
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupDatasetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDatasetArgs)(nil)).Elem()
}

type LookupDatasetResultOutput struct{ *pulumi.OutputState }

func (LookupDatasetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDatasetResult)(nil)).Elem()
}

func (o LookupDatasetResultOutput) ToLookupDatasetResultOutput() LookupDatasetResultOutput {
	return o
}

func (o LookupDatasetResultOutput) ToLookupDatasetResultOutputWithContext(ctx context.Context) LookupDatasetResultOutput {
	return o
}

// Dataset format
func (o LookupDatasetResultOutput) Format() DatasetFormatPtrOutput {
	return o.ApplyT(func(v LookupDatasetResult) *DatasetFormat { return v.Format }).(DatasetFormatPtrOutput)
}

// Format options for dataset
func (o LookupDatasetResultOutput) FormatOptions() DatasetFormatOptionsPtrOutput {
	return o.ApplyT(func(v LookupDatasetResult) *DatasetFormatOptions { return v.FormatOptions }).(DatasetFormatOptionsPtrOutput)
}

// Input
func (o LookupDatasetResultOutput) Input() DatasetInputTypePtrOutput {
	return o.ApplyT(func(v LookupDatasetResult) *DatasetInputType { return v.Input }).(DatasetInputTypePtrOutput)
}

// PathOptions
func (o LookupDatasetResultOutput) PathOptions() DatasetPathOptionsPtrOutput {
	return o.ApplyT(func(v LookupDatasetResult) *DatasetPathOptions { return v.PathOptions }).(DatasetPathOptionsPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDatasetResultOutput{})
}
