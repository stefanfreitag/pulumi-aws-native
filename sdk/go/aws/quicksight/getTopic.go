// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package quicksight

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of the AWS::QuickSight::Topic Resource Type.
func LookupTopic(ctx *pulumi.Context, args *LookupTopicArgs, opts ...pulumi.InvokeOption) (*LookupTopicResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupTopicResult
	err := ctx.Invoke("aws-native:quicksight:getTopic", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupTopicArgs struct {
	AwsAccountId string `pulumi:"awsAccountId"`
	TopicId      string `pulumi:"topicId"`
}

type LookupTopicResult struct {
	Arn         *string                `pulumi:"arn"`
	DataSets    []TopicDatasetMetadata `pulumi:"dataSets"`
	Description *string                `pulumi:"description"`
	Name        *string                `pulumi:"name"`
}

func LookupTopicOutput(ctx *pulumi.Context, args LookupTopicOutputArgs, opts ...pulumi.InvokeOption) LookupTopicResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTopicResult, error) {
			args := v.(LookupTopicArgs)
			r, err := LookupTopic(ctx, &args, opts...)
			var s LookupTopicResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTopicResultOutput)
}

type LookupTopicOutputArgs struct {
	AwsAccountId pulumi.StringInput `pulumi:"awsAccountId"`
	TopicId      pulumi.StringInput `pulumi:"topicId"`
}

func (LookupTopicOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTopicArgs)(nil)).Elem()
}

type LookupTopicResultOutput struct{ *pulumi.OutputState }

func (LookupTopicResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTopicResult)(nil)).Elem()
}

func (o LookupTopicResultOutput) ToLookupTopicResultOutput() LookupTopicResultOutput {
	return o
}

func (o LookupTopicResultOutput) ToLookupTopicResultOutputWithContext(ctx context.Context) LookupTopicResultOutput {
	return o
}

func (o LookupTopicResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupTopicResult] {
	return pulumix.Output[LookupTopicResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupTopicResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTopicResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupTopicResultOutput) DataSets() TopicDatasetMetadataArrayOutput {
	return o.ApplyT(func(v LookupTopicResult) []TopicDatasetMetadata { return v.DataSets }).(TopicDatasetMetadataArrayOutput)
}

func (o LookupTopicResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTopicResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupTopicResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTopicResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTopicResultOutput{})
}
