// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Glue::DataQualityRuleset
func LookupDataQualityRuleset(ctx *pulumi.Context, args *LookupDataQualityRulesetArgs, opts ...pulumi.InvokeOption) (*LookupDataQualityRulesetResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDataQualityRulesetResult
	err := ctx.Invoke("aws-native:glue:getDataQualityRuleset", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDataQualityRulesetArgs struct {
	Id string `pulumi:"id"`
}

type LookupDataQualityRulesetResult struct {
	ClientToken *string `pulumi:"clientToken"`
	Description *string `pulumi:"description"`
	Id          *string `pulumi:"id"`
	Name        *string `pulumi:"name"`
	Ruleset     *string `pulumi:"ruleset"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::DataQualityRuleset` for more information about the expected schema for this property.
	Tags        interface{}                               `pulumi:"tags"`
	TargetTable *DataQualityRulesetDataQualityTargetTable `pulumi:"targetTable"`
}

func LookupDataQualityRulesetOutput(ctx *pulumi.Context, args LookupDataQualityRulesetOutputArgs, opts ...pulumi.InvokeOption) LookupDataQualityRulesetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDataQualityRulesetResult, error) {
			args := v.(LookupDataQualityRulesetArgs)
			r, err := LookupDataQualityRuleset(ctx, &args, opts...)
			var s LookupDataQualityRulesetResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDataQualityRulesetResultOutput)
}

type LookupDataQualityRulesetOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupDataQualityRulesetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataQualityRulesetArgs)(nil)).Elem()
}

type LookupDataQualityRulesetResultOutput struct{ *pulumi.OutputState }

func (LookupDataQualityRulesetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDataQualityRulesetResult)(nil)).Elem()
}

func (o LookupDataQualityRulesetResultOutput) ToLookupDataQualityRulesetResultOutput() LookupDataQualityRulesetResultOutput {
	return o
}

func (o LookupDataQualityRulesetResultOutput) ToLookupDataQualityRulesetResultOutputWithContext(ctx context.Context) LookupDataQualityRulesetResultOutput {
	return o
}

func (o LookupDataQualityRulesetResultOutput) ClientToken() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataQualityRulesetResult) *string { return v.ClientToken }).(pulumi.StringPtrOutput)
}

func (o LookupDataQualityRulesetResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataQualityRulesetResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupDataQualityRulesetResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataQualityRulesetResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupDataQualityRulesetResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataQualityRulesetResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupDataQualityRulesetResultOutput) Ruleset() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDataQualityRulesetResult) *string { return v.Ruleset }).(pulumi.StringPtrOutput)
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::DataQualityRuleset` for more information about the expected schema for this property.
func (o LookupDataQualityRulesetResultOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupDataQualityRulesetResult) interface{} { return v.Tags }).(pulumi.AnyOutput)
}

func (o LookupDataQualityRulesetResultOutput) TargetTable() DataQualityRulesetDataQualityTargetTablePtrOutput {
	return o.ApplyT(func(v LookupDataQualityRulesetResult) *DataQualityRulesetDataQualityTargetTable { return v.TargetTable }).(DataQualityRulesetDataQualityTargetTablePtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDataQualityRulesetResultOutput{})
}
