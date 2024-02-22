// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package gamelift

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::GameLift::MatchmakingRuleSet resource creates an Amazon GameLift (GameLift) matchmaking rule set.
func LookupMatchmakingRuleSet(ctx *pulumi.Context, args *LookupMatchmakingRuleSetArgs, opts ...pulumi.InvokeOption) (*LookupMatchmakingRuleSetResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupMatchmakingRuleSetResult
	err := ctx.Invoke("aws-native:gamelift:getMatchmakingRuleSet", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupMatchmakingRuleSetArgs struct {
	// A unique identifier for the matchmaking rule set.
	Name string `pulumi:"name"`
}

type LookupMatchmakingRuleSetResult struct {
	// The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift matchmaking rule set resource and uniquely identifies it.
	Arn *string `pulumi:"arn"`
	// A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds.
	CreationTime *string `pulumi:"creationTime"`
	// An array of key-value pairs to apply to this resource.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupMatchmakingRuleSetOutput(ctx *pulumi.Context, args LookupMatchmakingRuleSetOutputArgs, opts ...pulumi.InvokeOption) LookupMatchmakingRuleSetResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupMatchmakingRuleSetResult, error) {
			args := v.(LookupMatchmakingRuleSetArgs)
			r, err := LookupMatchmakingRuleSet(ctx, &args, opts...)
			var s LookupMatchmakingRuleSetResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupMatchmakingRuleSetResultOutput)
}

type LookupMatchmakingRuleSetOutputArgs struct {
	// A unique identifier for the matchmaking rule set.
	Name pulumi.StringInput `pulumi:"name"`
}

func (LookupMatchmakingRuleSetOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMatchmakingRuleSetArgs)(nil)).Elem()
}

type LookupMatchmakingRuleSetResultOutput struct{ *pulumi.OutputState }

func (LookupMatchmakingRuleSetResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMatchmakingRuleSetResult)(nil)).Elem()
}

func (o LookupMatchmakingRuleSetResultOutput) ToLookupMatchmakingRuleSetResultOutput() LookupMatchmakingRuleSetResultOutput {
	return o
}

func (o LookupMatchmakingRuleSetResultOutput) ToLookupMatchmakingRuleSetResultOutputWithContext(ctx context.Context) LookupMatchmakingRuleSetResultOutput {
	return o
}

// The Amazon Resource Name (ARN) that is assigned to a Amazon GameLift matchmaking rule set resource and uniquely identifies it.
func (o LookupMatchmakingRuleSetResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMatchmakingRuleSetResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds.
func (o LookupMatchmakingRuleSetResultOutput) CreationTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMatchmakingRuleSetResult) *string { return v.CreationTime }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupMatchmakingRuleSetResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupMatchmakingRuleSetResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMatchmakingRuleSetResultOutput{})
}
