// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package stepfunctions

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource schema for StateMachineAlias
func LookupStateMachineAlias(ctx *pulumi.Context, args *LookupStateMachineAliasArgs, opts ...pulumi.InvokeOption) (*LookupStateMachineAliasResult, error) {
	var rv LookupStateMachineAliasResult
	err := ctx.Invoke("aws-native:stepfunctions:getStateMachineAlias", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupStateMachineAliasArgs struct {
	// The ARN of the alias.
	Arn string `pulumi:"arn"`
}

type LookupStateMachineAliasResult struct {
	// The ARN of the alias.
	Arn *string `pulumi:"arn"`
	// An optional description of the alias.
	Description          *string                                        `pulumi:"description"`
	RoutingConfiguration []StateMachineAliasRoutingConfigurationVersion `pulumi:"routingConfiguration"`
}

func LookupStateMachineAliasOutput(ctx *pulumi.Context, args LookupStateMachineAliasOutputArgs, opts ...pulumi.InvokeOption) LookupStateMachineAliasResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupStateMachineAliasResult, error) {
			args := v.(LookupStateMachineAliasArgs)
			r, err := LookupStateMachineAlias(ctx, &args, opts...)
			var s LookupStateMachineAliasResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupStateMachineAliasResultOutput)
}

type LookupStateMachineAliasOutputArgs struct {
	// The ARN of the alias.
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupStateMachineAliasOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStateMachineAliasArgs)(nil)).Elem()
}

type LookupStateMachineAliasResultOutput struct{ *pulumi.OutputState }

func (LookupStateMachineAliasResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupStateMachineAliasResult)(nil)).Elem()
}

func (o LookupStateMachineAliasResultOutput) ToLookupStateMachineAliasResultOutput() LookupStateMachineAliasResultOutput {
	return o
}

func (o LookupStateMachineAliasResultOutput) ToLookupStateMachineAliasResultOutputWithContext(ctx context.Context) LookupStateMachineAliasResultOutput {
	return o
}

// The ARN of the alias.
func (o LookupStateMachineAliasResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStateMachineAliasResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// An optional description of the alias.
func (o LookupStateMachineAliasResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupStateMachineAliasResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupStateMachineAliasResultOutput) RoutingConfiguration() StateMachineAliasRoutingConfigurationVersionArrayOutput {
	return o.ApplyT(func(v LookupStateMachineAliasResult) []StateMachineAliasRoutingConfigurationVersion {
		return v.RoutingConfiguration
	}).(StateMachineAliasRoutingConfigurationVersionArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupStateMachineAliasResultOutput{})
}
