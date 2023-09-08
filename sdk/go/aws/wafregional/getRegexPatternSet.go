// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package wafregional

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::WAFRegional::RegexPatternSet
func LookupRegexPatternSet(ctx *pulumi.Context, args *LookupRegexPatternSetArgs, opts ...pulumi.InvokeOption) (*LookupRegexPatternSetResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupRegexPatternSetResult
	err := ctx.Invoke("aws-native:wafregional:getRegexPatternSet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupRegexPatternSetArgs struct {
	Id string `pulumi:"id"`
}

type LookupRegexPatternSetResult struct {
	Id                  *string  `pulumi:"id"`
	RegexPatternStrings []string `pulumi:"regexPatternStrings"`
}

func LookupRegexPatternSetOutput(ctx *pulumi.Context, args LookupRegexPatternSetOutputArgs, opts ...pulumi.InvokeOption) LookupRegexPatternSetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupRegexPatternSetResult, error) {
			args := v.(LookupRegexPatternSetArgs)
			r, err := LookupRegexPatternSet(ctx, &args, opts...)
			var s LookupRegexPatternSetResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupRegexPatternSetResultOutput)
}

type LookupRegexPatternSetOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupRegexPatternSetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRegexPatternSetArgs)(nil)).Elem()
}

type LookupRegexPatternSetResultOutput struct{ *pulumi.OutputState }

func (LookupRegexPatternSetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRegexPatternSetResult)(nil)).Elem()
}

func (o LookupRegexPatternSetResultOutput) ToLookupRegexPatternSetResultOutput() LookupRegexPatternSetResultOutput {
	return o
}

func (o LookupRegexPatternSetResultOutput) ToLookupRegexPatternSetResultOutputWithContext(ctx context.Context) LookupRegexPatternSetResultOutput {
	return o
}

func (o LookupRegexPatternSetResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupRegexPatternSetResult] {
	return pulumix.Output[LookupRegexPatternSetResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupRegexPatternSetResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRegexPatternSetResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupRegexPatternSetResultOutput) RegexPatternStrings() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupRegexPatternSetResult) []string { return v.RegexPatternStrings }).(pulumi.StringArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupRegexPatternSetResultOutput{})
}
