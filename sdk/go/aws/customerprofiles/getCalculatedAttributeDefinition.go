// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package customerprofiles

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A calculated attribute definition for Customer Profiles
func LookupCalculatedAttributeDefinition(ctx *pulumi.Context, args *LookupCalculatedAttributeDefinitionArgs, opts ...pulumi.InvokeOption) (*LookupCalculatedAttributeDefinitionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupCalculatedAttributeDefinitionResult
	err := ctx.Invoke("aws-native:customerprofiles:getCalculatedAttributeDefinition", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupCalculatedAttributeDefinitionArgs struct {
	CalculatedAttributeName string `pulumi:"calculatedAttributeName"`
	DomainName              string `pulumi:"domainName"`
}

type LookupCalculatedAttributeDefinitionResult struct {
	AttributeDetails *CalculatedAttributeDefinitionAttributeDetails `pulumi:"attributeDetails"`
	Conditions       *CalculatedAttributeDefinitionConditions       `pulumi:"conditions"`
	// The timestamp of when the calculated attribute definition was created.
	CreatedAt   *string `pulumi:"createdAt"`
	Description *string `pulumi:"description"`
	DisplayName *string `pulumi:"displayName"`
	// The timestamp of when the calculated attribute definition was most recently edited.
	LastUpdatedAt *string                                 `pulumi:"lastUpdatedAt"`
	Statistic     *CalculatedAttributeDefinitionStatistic `pulumi:"statistic"`
	Tags          []aws.Tag                               `pulumi:"tags"`
}

func LookupCalculatedAttributeDefinitionOutput(ctx *pulumi.Context, args LookupCalculatedAttributeDefinitionOutputArgs, opts ...pulumi.InvokeOption) LookupCalculatedAttributeDefinitionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCalculatedAttributeDefinitionResult, error) {
			args := v.(LookupCalculatedAttributeDefinitionArgs)
			r, err := LookupCalculatedAttributeDefinition(ctx, &args, opts...)
			var s LookupCalculatedAttributeDefinitionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCalculatedAttributeDefinitionResultOutput)
}

type LookupCalculatedAttributeDefinitionOutputArgs struct {
	CalculatedAttributeName pulumi.StringInput `pulumi:"calculatedAttributeName"`
	DomainName              pulumi.StringInput `pulumi:"domainName"`
}

func (LookupCalculatedAttributeDefinitionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCalculatedAttributeDefinitionArgs)(nil)).Elem()
}

type LookupCalculatedAttributeDefinitionResultOutput struct{ *pulumi.OutputState }

func (LookupCalculatedAttributeDefinitionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCalculatedAttributeDefinitionResult)(nil)).Elem()
}

func (o LookupCalculatedAttributeDefinitionResultOutput) ToLookupCalculatedAttributeDefinitionResultOutput() LookupCalculatedAttributeDefinitionResultOutput {
	return o
}

func (o LookupCalculatedAttributeDefinitionResultOutput) ToLookupCalculatedAttributeDefinitionResultOutputWithContext(ctx context.Context) LookupCalculatedAttributeDefinitionResultOutput {
	return o
}

func (o LookupCalculatedAttributeDefinitionResultOutput) AttributeDetails() CalculatedAttributeDefinitionAttributeDetailsPtrOutput {
	return o.ApplyT(func(v LookupCalculatedAttributeDefinitionResult) *CalculatedAttributeDefinitionAttributeDetails {
		return v.AttributeDetails
	}).(CalculatedAttributeDefinitionAttributeDetailsPtrOutput)
}

func (o LookupCalculatedAttributeDefinitionResultOutput) Conditions() CalculatedAttributeDefinitionConditionsPtrOutput {
	return o.ApplyT(func(v LookupCalculatedAttributeDefinitionResult) *CalculatedAttributeDefinitionConditions {
		return v.Conditions
	}).(CalculatedAttributeDefinitionConditionsPtrOutput)
}

// The timestamp of when the calculated attribute definition was created.
func (o LookupCalculatedAttributeDefinitionResultOutput) CreatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCalculatedAttributeDefinitionResult) *string { return v.CreatedAt }).(pulumi.StringPtrOutput)
}

func (o LookupCalculatedAttributeDefinitionResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCalculatedAttributeDefinitionResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupCalculatedAttributeDefinitionResultOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCalculatedAttributeDefinitionResult) *string { return v.DisplayName }).(pulumi.StringPtrOutput)
}

// The timestamp of when the calculated attribute definition was most recently edited.
func (o LookupCalculatedAttributeDefinitionResultOutput) LastUpdatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCalculatedAttributeDefinitionResult) *string { return v.LastUpdatedAt }).(pulumi.StringPtrOutput)
}

func (o LookupCalculatedAttributeDefinitionResultOutput) Statistic() CalculatedAttributeDefinitionStatisticPtrOutput {
	return o.ApplyT(func(v LookupCalculatedAttributeDefinitionResult) *CalculatedAttributeDefinitionStatistic {
		return v.Statistic
	}).(CalculatedAttributeDefinitionStatisticPtrOutput)
}

func (o LookupCalculatedAttributeDefinitionResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupCalculatedAttributeDefinitionResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCalculatedAttributeDefinitionResultOutput{})
}
