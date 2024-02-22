// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package forecast

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Represents a dataset group that holds a collection of related datasets
func LookupDatasetGroup(ctx *pulumi.Context, args *LookupDatasetGroupArgs, opts ...pulumi.InvokeOption) (*LookupDatasetGroupResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDatasetGroupResult
	err := ctx.Invoke("aws-native:forecast:getDatasetGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDatasetGroupArgs struct {
	// The Amazon Resource Name (ARN) of the dataset group to delete.
	DatasetGroupArn string `pulumi:"datasetGroupArn"`
}

type LookupDatasetGroupResult struct {
	// An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.
	DatasetArns []string `pulumi:"datasetArns"`
	// The Amazon Resource Name (ARN) of the dataset group to delete.
	DatasetGroupArn *string `pulumi:"datasetGroupArn"`
	// The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the Domain parameter of the CreateDataset operation must match.
	Domain *DatasetGroupDomain `pulumi:"domain"`
	// The tags of Application Insights application.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupDatasetGroupOutput(ctx *pulumi.Context, args LookupDatasetGroupOutputArgs, opts ...pulumi.InvokeOption) LookupDatasetGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDatasetGroupResult, error) {
			args := v.(LookupDatasetGroupArgs)
			r, err := LookupDatasetGroup(ctx, &args, opts...)
			var s LookupDatasetGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDatasetGroupResultOutput)
}

type LookupDatasetGroupOutputArgs struct {
	// The Amazon Resource Name (ARN) of the dataset group to delete.
	DatasetGroupArn pulumi.StringInput `pulumi:"datasetGroupArn"`
}

func (LookupDatasetGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDatasetGroupArgs)(nil)).Elem()
}

type LookupDatasetGroupResultOutput struct{ *pulumi.OutputState }

func (LookupDatasetGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDatasetGroupResult)(nil)).Elem()
}

func (o LookupDatasetGroupResultOutput) ToLookupDatasetGroupResultOutput() LookupDatasetGroupResultOutput {
	return o
}

func (o LookupDatasetGroupResultOutput) ToLookupDatasetGroupResultOutputWithContext(ctx context.Context) LookupDatasetGroupResultOutput {
	return o
}

// An array of Amazon Resource Names (ARNs) of the datasets that you want to include in the dataset group.
func (o LookupDatasetGroupResultOutput) DatasetArns() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupDatasetGroupResult) []string { return v.DatasetArns }).(pulumi.StringArrayOutput)
}

// The Amazon Resource Name (ARN) of the dataset group to delete.
func (o LookupDatasetGroupResultOutput) DatasetGroupArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDatasetGroupResult) *string { return v.DatasetGroupArn }).(pulumi.StringPtrOutput)
}

// The domain associated with the dataset group. When you add a dataset to a dataset group, this value and the value specified for the Domain parameter of the CreateDataset operation must match.
func (o LookupDatasetGroupResultOutput) Domain() DatasetGroupDomainPtrOutput {
	return o.ApplyT(func(v LookupDatasetGroupResult) *DatasetGroupDomain { return v.Domain }).(DatasetGroupDomainPtrOutput)
}

// The tags of Application Insights application.
func (o LookupDatasetGroupResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupDatasetGroupResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDatasetGroupResultOutput{})
}
